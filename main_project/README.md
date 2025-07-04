# Celebal Summer Internship Main Project - 2025

This project performs structured ingestion and processing of customer data using **PySpark on Databricks**, simulating the loading from Azure Data Lake Storage Gen2. The goal is to process various file formats and create **Delta tables**, validating they each contain **500 customer records**.

---

## 📂 Project Structure


main_project/
├── adls_gen2(simulated)/ # Customer data in various formats (CSV, JSON, Parquet, etc.)
├── Scripts/ # PySpark scripts for loading and processing
├── json_templates/ # ADLS linked service config (for ADF or Databricks mount)
├── screenshots/ # Validation proof screenshots




---

## 🚀 Steps Covered (as per assignment)

1. **Load sample customer data** into simulated ADLS Gen2 (`adls_gen2(simulated)/`)
2. **Connect** to Databricks and read files using PySpark
3. **Create managed Delta tables** using:
   - **CTAS** for: `.avro`, `.parquet`, `.orc`, `.delta`
   - **Temporary View + CTAS** for: `.csv`, `.json`, `.tsv`, `.txt`, `.xml`, `.xlsx`
4. **Validate each Delta table** to ensure it contains **exactly 500 rows**

---

## 🧠 Script Descriptions (in `/Scripts`)

| Script File                     | Purpose                                                                 |
|---------------------------------|-------------------------------------------------------------------------|
| `load_to_managed_delta.py`      | Loads data into a **managed Delta table** (not external)               |
| `ctas_format_based.py`          | Handles CTAS for AVRO, PARQUET, ORC, and DELTA                         |
| `tempview_ctas_text_formats.py` | Reads CSV, JSON, TSV, TXT, XML, XLSX with schema → TempView → CTAS     |
| `validate_row_count.py`         | Generic function to validate Delta tables have **500 rows** each       |

---

## 📦 Required Packages

- `pyspark`
- `openpyxl` or `com.crealytics.spark.excel` (for `.xlsx`)
- `spark-xml` (for `.xml` files)
- Databricks runtime with Delta Lake support

> Make sure you're running on Databricks or a PySpark environment with the above JARs installed.

---

## 🖼️ Screenshots (Proof of Count = 500)

All Delta tables were successfully created and validated to contain **exactly 500 customer records**.

| Format     | Screenshot                      | Count |
|------------|----------------------------------|--------|
| CSV        | ✅ `customers_CSV_count.png`      | 500    |
| JSON       | ✅ `customers_JSON_count.png`     | 500    |
| TSV        | ✅ `customers_TSV_count.png`      | 500    |
| TXT        | ✅ `customers_TXT_count.png`      | 500    |
| XML        | ✅ `customers_XML_count.png`      | 500    |
| Others     | Validated via Spark console or logs | 500   |

---

## 🧪 Running the Validation

```bash
# Run this script in Databricks or PySpark environment
python validate_row_count.py
