def validate_delta_table(table_name, expected_rows=500):
    df = spark.sql(f"SELECT COUNT(*) AS cnt FROM {table_name}")
    actual = df.collect()[0]["cnt"]
    return actual == expected_rows

tables = ["customers_csv", "customers_tsv", "customers_json", "customers_xml", 
          "customers_xlsx", "customers_txt", "customers_parquet", "customers_avro"]

for tbl in tables:
    result = validate_delta_table(tbl)
    print(f"✅ {tbl}: Validated" if result else f"❌ {tbl}: Row count mismatch")
