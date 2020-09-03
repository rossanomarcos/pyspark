# -*- coding: utf-8 -*-
"""Spark_Installation_on_Colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10n_cNyB482MZtKnxrPjl7zBwv8T3nP6s

# Colab is a Linux environment. 

# You can execute Linux commands from Colab notebook with a "!" prefix

## Install JDK
"""

!apt-get install openjdk-8-jdk-headless -qq > /dev/null

"""## Get Spark installer (Check the path on Spark.org)"""

!wget -q https://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.6.tgz

"""## Check if the file is copied"""

!ls

"""## Untar the Spark installer"""

!tar -xvf spark-2.4.3-bin-hadoop2.6.tgz

"""## Check the spark folder after untar"""

!ls

"""## Install findspark - a Python library to find Spark"""

!pip install -q findspark

"""## Set environment variables
Set Java and Spark Home based on location where they are stored
"""

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.3-bin-hadoop2.6"

"""## Create a local Spark Session"""

import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

"""## Test Installation"""

df = spark.createDataFrame([{"Google": "Colab","Spark": "Scala"} ,{"Google": "Dataproc","Spark":"Python"}])
df.show()

