import sys
import sqlite3
import pandas as pd
import subprocess

if len(sys.argv) < 2:
    print("Usage: python ingest.py <path_to_dataset>")
    sys.exit(1)

file_path = sys.argv[1]
print("Loading dataset from:", file_path)

try:
    conn = sqlite3.connect(file_path)

    # check what tables exist
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
    print("Tables found:", tables['name'].tolist())

    table_name = tables['name'].iloc[0]

    # load only 100,000 rows to avoid memory crash
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()

    df.to_csv("data_raw.csv", index=False, encoding='utf-8', errors='replace')
    print("Saved as data_raw.csv -", len(df), "rows loaded")

    subprocess.run(["python3", "preprocessing.py", "data_raw.csv"])

except Exception as e:
    print("Something went wrong:", e)