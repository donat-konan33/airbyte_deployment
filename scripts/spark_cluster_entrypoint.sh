#!/usr/bin/env bash

# checkout SPARK_MODE "master"
if [ "$SPARK_MODE" == "master" ]; then
  echo "Startup Spark Master and Thrift Server"

  $SPARK_HOME/sbin/start-master.sh
  # start Spark Thrift Server
  $SPARK_HOME/sbin/start-thriftserver.sh \
    --master spark://spark-master:7077 \
    --jars $SPARK_HOME/jars/iceberg-spark3-runtime.jar

elif [ "$SPARK_MODE" == "worker" ]; then
  echo "Startup Spark Worker"

  # Démarrage du Spark Worker
  $SPARK_HOME/sbin/start-worker.sh \
    spark://spark-master:7077

else
  echo "Error : SPARK_MODE must be equal to 'master' or 'worker'."
  exit 1
fi


# display Spark logs
tail -f $SPARK_HOME/logs/*
