import io
import pickle
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from typing import List, Tuple
from google.cloud import storage
import asyncio
import time
import re
from google.cloud.exceptions import GoogleCloudError


def get_name_of_blob(gs_path: List[str]) -> List[str]:
    """
    from gcs path find the name of file
    """
    new_list = [path.split("/")[-1] for path in gs_path]
    return new_list


def retrieve_diff_date(files_name: List[str]):
    """
    get different files according to the date of extraction
    """

    pattern = r'^\d{4}_\d{2}_\d{2}$' # give only this pattern `YYYY_MM_DD`
    date_list = [file_name[:10] for file_name in files_name if re.search(pattern, file_name[:10]) != None]
    different_date = set(date_list)
    return different_date


def concat_data_by_date(dates: List[str], client:storage.Client, bucket_name:str, prefix:str) -> pd.DataFrame:
    """
    date format like `YYYY_MM_DD`
    prefix like ``staging/weather_1/``
    goal: concatenate with pandas

    """
    bucket = client.bucket(bucket_name)
    list_of_blobs = bucket.list_blobs(prefix=prefix) # <google.api_core.page_iterator.HTTPIterator object at 0x7fe50d141d00>
    list_of_blobs = list(list_of_blobs)              # convert to list of blobs

    for date in dates:
        df = None
        for blob in list_of_blobs:
            if date in blob.name:
                df1 = read_parquet_from_blob(blob) # read blob from GCS
                if df is None:
                    df = df1
                else:
                    df = pd.concat([df, df1], ignore_index=True)
        # convert DataFrame Parquet format in memory (local storageless)
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, index=False)
        parquet_buffer.seek(0)

        # store staging data according to the date specified
        destination_blob_name = prefix + date.replace("_", "-") + "_airbyte.parquet"
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(parquet_buffer, content_type='application/octet-stream')
        print(f"✅ merging up ! new merged file recorded to: gs://{bucket_name}/{destination_blob_name}")

        if df is None:
            print(f"No files matching with date {date} specified.")
            return


def choose_first(address):
    """
    choose the first element from string separated by comma
    """
    # head,*tail = Iter.split(",") # or head = Iter.split(",")[0] for iterable using
    # let's vectorize this calculation task
    return np.vectorize(lambda x: x.split(',')[0])(address)

def read_parquet_from_blob(blob: storage.Blob) -> pd.DataFrame:
    """
    read parquet from a bucket blob and return dataframe
    """
    data = blob.download_as_bytes()
    table = pq.read_table(io.BytesIO(data))
    return table.to_pandas()


def create_table_from_airbyte_data(client: storage.Client, dates: set, bucket: str, source_prefix: str , staging_prefix: str) -> None:
    """
    create table from data extracted by airbyte that comes with json format

    """
    # connection to the bucket
    bucket = client.bucket(bucket)
    list_of_blobs = list(bucket.list_blobs(prefix=source_prefix))
    for date in dates:
        df = None
        for blob in list_of_blobs:
            date = date.replace("_", "-")
            if date in blob.name:
                df = read_parquet_from_blob(blob)
                df.drop(['_airbyte_additional_properties', '_airbyte_emitted_at'], axis=1, inplace=True)

                df_exploded = df.explode(column='days')
                df_days = pd.json_normalize(df_exploded['days'])
                df = df_exploded.drop(columns=["days",]).reset_index(drop=True).join(df_days)
                df["department"] = choose_first(df["resolvedAddress"].values)
                df.drop(columns=["_airbyte_additional_properties", ], inplace=True)
                output_path = f"{staging_prefix}france_weather_" + date + ".parquet"

                # convert DataFrame Parquet format in memory (local storageless)
                parquet_buffer = io.BytesIO()
                df.to_parquet(parquet_buffer, index=False)
                parquet_buffer.seek(0)

                # store staging data according to the date specified
                blob = bucket.blob(output_path)
                blob.upload_from_file(parquet_buffer, content_type='application/octet-stream')


def merge_gcs_files_by_date(diff_date: Tuple[str], client: storage.Client, bucket_name: str, prefix: str):
    """
    merge file with same format inplace.

    :param bucket_name: gcs bucket name
    :param destination_blob_name:
    goal : use a gcs object method named `.compose()`, it should help to combine (concatenate) the files with same formats and same structure
    """
    bucket = client.bucket(bucket_name)
    list_of_blobs = bucket.list_blobs(prefix=prefix)
    list_of_blobs = list(list_of_blobs)

    # retrieve existing dates from files name and retrieve object sources
    for date in diff_date:
        destination_blob_name = prefix + date + "-airbyte.parquet"
        destination_blob = bucket.blob(destination_blob_name)
        destination_blob.content_type = 'application/octet-stream'
        gather_date_blobs = [blob for blob in list_of_blobs if date in blob.name]

        destination_generation_match_precondition = 0

        # merge files
        destination_blob.compose(gather_date_blobs, if_generation_match=destination_generation_match_precondition)
        print(f"✅ merging up ! new file recorded : gs://{bucket_name}/{destination_blob_name}")

def delete_chunked_data(client: storage.Client, bucket_name: str, prefix:str):
    """
    """
    try:
        key_word = "airbyte"
        bucket = client.bucket(bucket_name)
        blobs_to_delete = [blob for blob in bucket.list_blobs(prefix=prefix) if key_word not in blob.name]

        if blobs_to_delete:
            bucket.delete_blobs(blobs_to_delete)
            for blob in blobs_to_delete:
                print(f"✅ Blob gs://{bucket_name}/{blob.name} deleted")
        else:
            print("✅ No blob matching criteria specified above.")
    except GoogleCloudError as e:
        print(f"❌ A erreor occured when deleting blobs : {e}")


### asynchroneous function
async def read_parquet_from_gcs(client: storage.Client, bucket_name, file_name):
    """read Parquet file from GCS in asynchroneous mode via asyncio.to_thread()."""
    print(f"Reading file {file_name}...")
    start_time = time.perf_counter()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # load data asynchroneously in memory as gcs storage doesn't allow this type of operation
    file_data = await asyncio.to_thread(blob.download_as_bytes)

    # read parquet to dataframe format
    table = pq.read_table(io.BytesIO(file_data))
    df = table.to_pandas()

    print(f"Read {file_name} with {df.shape[0]} rows in {time.perf_counter() - start_time:.2f} seconds.")
    return df

async def process_parquet_files(client:storage.Client, bucket_name:str, file_names:List[str]) -> pd.DataFrame:
    """read and concatenate bucket files asynchroneously."""
    total_start_time = time.perf_counter()

    # Créer les tâches pour lire les fichiers
    tasks = [read_parquet_from_gcs(client, bucket_name, file_name) for file_name in file_names]

    # Exécuter les tâches en parallèle
    results = await asyncio.gather(*tasks)

    # Concaténer les DataFrames
    final_df = pd.concat(results, ignore_index=True)

    print(f"Processed all files in {time.perf_counter() - total_start_time:.2f} seconds.")
    return final_df


def get_file_names(client: storage.Client , bucket_name:str, prefix:str) -> List[str]:
    """
    get file names from a bucket
    """
    bucket = client.bucket(bucket_name)
    list_of_blobs = list(bucket.list_blobs(prefix=prefix))
    return [blob.name for blob in list_of_blobs]

def run_async(client:storage.Client, bucket_name:str, file_names:List[str]):
    """
    file names are list of files in the bucket to read and concatenate into staging/weather_1/ folder in the bucket specified
    """
    final_df = asyncio.run(process_parquet_files(client, bucket_name, file_names))
    return final_df
