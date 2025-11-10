from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkToPostgres") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.1") \
    .getOrCreate()

from pyspark.sql.functions import current_timestamp

data = [(3, "Nina", "Maluku", 70000),
        (4, "Dino", "Bali", 90000)]
columns = ["customer_id", "customer_name", "city", "amount"]

df = spark.createDataFrame(data, columns).withColumn("load_time", current_timestamp())

url = "jdbc:postgresql://localhost:5432/prod_purwadika"
properties = {
    "user": "prod_airflow",
    "password": "prod_airflow",
    "driver": "org.postgresql.Driver"
}

df.write.jdbc(
    url=url,
    table="public.name_meet24",
    mode="append", 
    properties=properties
)

print("data berhasil write ke postgresql")