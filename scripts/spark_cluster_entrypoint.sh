#!/usr/bin/env bash

# checkout SPARK_MODE "master"
if [ "$SPARK_MODE" == "master" ]; then
  echo "Startup Spark Master and Thrift Server"

  # start Spark Thrift Server
  /opt/bitnami/spark/sbin/start-thriftserver.sh \
    --master spark://spark-master:7077 \
    --conf spark.sql.catalogImplementation=hive

elif [ "$SPARK_MODE" == "worker" ]; then
  echo "Startup Spark Worker"

  # Démarrage du Spark Worker
  /opt/bitnami/spark/sbin/start-slave.sh \
    spark://spark-master:7077

else
  echo "Error : SPARK_MODE must be equal to 'master' or 'worker'."
  exit 1
fi


# display Spark logs
tail -f /opt/bitnami/spark/logs/*
