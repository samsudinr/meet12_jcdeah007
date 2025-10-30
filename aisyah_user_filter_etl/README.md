# Aisyah User Filter ETL

A simple ETL pipeline in Python to extract, filter, and combine `userName` data from CSV log files related to BPJS verification.

The pipeline processes two folders of CSV logs, extracts the `userName` field from JSON-like columns, removes duplicates, and generates the final list of users who are in not-verified but not in verified.

---

## Project Structure

aisyah_user_filter_etl/
├─ extract.py
├─ transform.py
├─ load.py
├─ main.py
├─ README.md
├─ mixed_not_verify_bpjs/
└─ mixed_verify_bpjs/

---

## Prerequisites

- Python 3.x
- pandas library

---

## How to Run

1. Place your CSV files in the folders:

   - mixed_not_verify_bpjs/ → CSVs of users not verified
   - mixed_verify_bpjs/ → CSVs of users verified

2. Run the ETL pipeline:

python main.py

3. Outputs generated:

- combined_username.csv → combined userName from mixed_not_verify_bpjs
- combined_username_bpjs.csv → combined userName from mixed_verify_bpjs
- clean_non_verify_bpjs_usernames.txt → userName that are only in not-verified folder, one per line, no header

---

## ETL Process

1. Extract

   - Reads all CSV files from the input folders
   - Extracts the `userName` field from the JSON-like column `http.request.body.original`
   - Removes duplicate names within each folder

2. Transform

   - Filters userNames that are present in mixed_not_verify_bpjs but not present in mixed_verify_bpjs

3. Load
   - Saves the combined CSVs for each folder
   - Saves the final filtered result as a TXT file (one name per line, no header)

---
