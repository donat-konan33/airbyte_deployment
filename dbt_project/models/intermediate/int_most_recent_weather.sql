{{
  config(
    materialized="view"
  )
}}

select
  record_id,
  dates,
  FORMAT_DATE('%A', dates) AS weekday_name,
  datetimeEpoch,
  department,
  LOWER(TRIM(
        REGEXP_REPLACE(
                REGEXP_REPLACE(
                          NORMALIZE(department, NFD), r'\pM', ''),
                   r'[^A-Za-z0-9]', '')
                   )
  )

  AS department_lower,
  locations,
  latitude,
  longitude,
  ST_GEOGPOINT(longitude, latitude) AS geo_point_2d,
  {{ convert_mj_per_m2_to_kwh_per_m2('solarenergy') }} AS solarenergy_kwhpm2,
  solarradiation,
  uvindex,
  temp,
  tempmax,
  tempmin,
  feelslike,
  feelslikemax,
  feelslikemin,
  precip,
  precipprob,
  precipcover,
  snow,
  snowdepth_filled,
  dew,
  humidity,
  winddir,
  windspeed,
  windgust,
  pressure,
  severerisk,
  icon,
  cloudcover,
  conditions,
  moonphase,
  CASE
      WHEN moonphase=0                    THEN 'new moon'
      WHEN moonphase BETWEEN 0 AND 0.25   THEN 'waxing crescent'
      WHEN moonphase=0.25                 THEN 'first quarter'
      WHEN moonphase BETWEEN 0.25 AND 0.5 THEN 'waxing gibbous'
      WHEN moonphase=0.5                  THEN 'full moon'
      WHEN moonphase BETWEEN 0.5 AND 0.75 THEN 'waning gibbous'
      WHEN moonphase=0.75                 THEN 'last quarter'
      ELSE 'waning crescent'
  END AS moonphase_label,
  descriptions,
  sunrise_time,
  sunset_time,
  source,
  sunriseEpoch,
  sunsetEpoch,

from {{ref('stg_most_recent_weather')}}
