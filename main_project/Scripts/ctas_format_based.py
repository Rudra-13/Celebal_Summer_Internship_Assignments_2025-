formats = ["avro", "parquet", "orc", "delta"]

for fmt in formats:
    df = spark.read.format(fmt).load(f"./adls_gen2/customers.{fmt}")
    table_name = f"customers_{fmt}"
    df.createOrReplaceTempView("temp_view")
    spark.sql(f"""
        CREATE OR REPLACE TABLE {table_name}
        USING DELTA
        AS SELECT * FROM temp_view
    """)
