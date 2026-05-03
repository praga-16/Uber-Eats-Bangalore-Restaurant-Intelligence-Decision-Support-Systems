import sqlite3
import pandas as pd
import os

# Check if cleaned file exists
file_path = "data/processed/cleaned_data.csv"

if not os.path.exists(file_path):
    raise Exception("❌ Run data_cleaning.py first")

# Load cleaned data
df = pd.read_csv(file_path)

# Connect to SQLite DB
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    name TEXT,
    location TEXT,
    rate REAL,
    cost REAL
)
""")

# Insert data
df.to_sql("restaurants", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✅ Data inserted into restaurant.db successfully!")