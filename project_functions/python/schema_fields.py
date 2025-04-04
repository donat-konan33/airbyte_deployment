old_data_schema_field = [
    {"name": "name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "communes", "type": "STRING", "mode": "NULLABLE"},
    {"name": "regions", "type": "STRING", "mode": "NULLABLE"},
    {"name": "pays", "type": "STRING", "mode": "NULLABLE"},
    {"name": "datetime", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "tempmax", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "tempmin", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "temp", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "feelslikemax", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "feelslikemin", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "feelslike", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "dew", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "humidity", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "precip", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "precipprob", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "precipcover", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "preciptype", "type": "STRING", "mode": "NULLABLE"},
    {"name": "snow", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "snowdepth", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "windgust", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "windspeed", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "winddir", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "sealevelpressure", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "cloudcover", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "visibility", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "solarradiation", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "solarenergy", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "uvindex", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "severerisk", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "sunrise", "type": "STRING", "mode": "NULLABLE"},
    {"name": "sunset", "type": "STRING", "mode": "NULLABLE"},
    {"name": "timeofday", "type": "STRING", "mode": "NULLABLE"},
    {"name": "moonphase", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "conditions", "type": "STRING", "mode": "NULLABLE"},
    {"name": "description", "type": "STRING", "mode": "NULLABLE"},
    {"name": "icon", "type": "STRING", "mode": "NULLABLE"},
    {"name": "stations", "type": "STRING", "mode": "NULLABLE"}
]

regdep_france_raw_schema_field = [
    {"name": "geo_point_2d", "type": "GEOGRAPHY", "mode": "NULLABLE"},
    {"name": "geo_shape", "type": "GEOGRAPHY", "mode": "NULLABLE"},
    {"name": "reg_code", "type": "STRING", "mode": "NULLABLE"},
    {"name": "reg_name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dep_current_code", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dep_name_upper", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dep_status", "type": "STRING", "mode": "NULLABLE"}
]

mun_dep_france_raw_schema_field = [
    {"name": "municipality", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dep_name_upper", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dep_code", "type": "STRING", "mode": "NULLABLE"}
]

new_data_schema_field = [
    {"name": "_airbyte_ab_id", "type": "STRING", "mode": "NULLABLE"},
    {"name": "latitude", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "longitude", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "resolvedAddress", "type": "STRING", "mode": "NULLABLE"},
    {"name": "cloudcover", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "conditions", "type": "STRING", "mode": "NULLABLE"},
    {"name": "datetime", "type": "STRING", "mode": "NULLABLE"},
    {"name": "datetimeEpoch", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "description", "type": "STRING", "mode": "NULLABLE"},
    {"name": "dew", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "feelslike", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "feelslikemax", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "feelslikemin", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "humidity", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "icon", "type": "STRING", "mode": "NULLABLE"},
    {"name": "moonphase", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "precip", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "precipcover", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "precipprob", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "preciptype", "type": "STRING", "mode": "NULLABLE"},
    {"name": "pressure", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "severerisk", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "snow", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "snowdepth", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "solarenergy", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "solarradiation", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "source", "type": "STRING", "mode": "NULLABLE"},
    {"name": "stations", "type": "STRING", "mode": "NULLABLE"},
    {"name": "sunrise", "type": "STRING", "mode": "NULLABLE"},
    {"name": "sunriseEpoch", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "sunset", "type": "STRING", "mode": "NULLABLE"},
    {"name": "sunsetEpoch", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "temp", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "tempmax", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "tempmin", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "uvindex", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "visibility", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "winddir", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "windgust", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "windspeed", "type": "FLOAT", "mode": "NULLABLE"},
    {"name": "department", "type": "STRING", "mode": "NULLABLE"}
]
