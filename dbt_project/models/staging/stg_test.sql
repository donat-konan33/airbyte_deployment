{{ config(
    materialized='table',
    file_format='iceberg'
)
}}

select *
from {{ source( 'raw_data', 'depcode') }}
