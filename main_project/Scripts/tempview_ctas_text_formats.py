text_formats = {
    "csv": "option('delimiter', ',')",
    "tsv": "option('delimiter', '\t')",
    "json": "",
    "xml": ".format('com.databricks.spark.xml').option('rowTag', 'customer')",
    "xlsx": ".format('com.crealytics.spark.excel').option('header', 'true')",
    "txt": "option('delimiter', '|')"
}

for fmt, options in text_formats.items():
    path = f"./adls_gen2/customers.{fmt}"
    if "xml" in fmt or "xlsx" in fmt:
        df = spark.read.format(fmt).load(path)
    else:
        df = spark.read.option("header", "true").load(path)

    df.createOrReplaceTempView("temp_view")
    spark.sql(f"""
        CREATE OR REPLACE TABLE customers_{fmt}
        USING DELTA
        AS SELECT * FROM temp_view
    """)
