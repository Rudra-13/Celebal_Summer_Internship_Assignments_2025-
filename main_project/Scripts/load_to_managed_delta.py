from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CustomerDeltaIngestion") \
    .config("spark.sql.warehouse.dir", "./delta_warehouse") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Example: Read CSV
df = spark.read.option("header", "true").csv("./adls_gen2/customers.csv")

# Save as Managed Delta Table
df.write.format("delta").mode("overwrite").saveAsTable("customers_csv")
