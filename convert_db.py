import sqlite3
import pandas as pd

conn = sqlite3.connect("chicago.db")

# Check what tables exist in the database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("Tables found:", tables)

# Read the data and export to CSV
df = pd.read_sql("SELECT * FROM crimes", conn)
df.to_csv("chicago.csv", index=False)

print(f"Done! Saved {len(df):,} rows to chicago.csv")
conn.close()