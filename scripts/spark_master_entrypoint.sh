#!/usr/bin/env bash

# checkout SPARK_MODE "master"
if [ "$SPARK_MODE" == "master" ]; then
  echo "Démarrage du Spark Master avec Thrift Server"

  # Démarrage du Spark Thrift Server
  /opt/bitnami/spark/sbin/start-thriftserver.sh \
    --master spark://spark-master:7077 \
    --conf spark.sql.warehouse.dir=/opt/bitnami/spark/warehouse

else
  echo "Error : SPARK_MODE must be equal to 'master' for Thrift Server start up."
  exit 1
fi

# display Spark logs
tail -f /opt/bitnami/spark/logs/*
