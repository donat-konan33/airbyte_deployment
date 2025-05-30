We intend in this to have a strong analytics architecture with:

- Airbyte : our data integration tool
- Minio : Our data lake where to store data from airbyte (here it will be our warehouse since Spark/Iceberg )
- Apache Iceberg/Spark : our own data distributed transformation engine
- dbt : brings granularity of transformtions

Here no need connecting to a data warehouse and load data. All transformations are achieved into the Data Lake.

Project in progress ...
