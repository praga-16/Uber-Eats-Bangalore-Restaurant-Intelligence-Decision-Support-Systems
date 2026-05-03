import pandas as pd
import os

# Correct file path (your case)
file_path = "Uber_Eats_data.csv"

# Load dataset
df = pd.read_csv(file_path)

print("✅ File loaded successfully")

# ---------------- CLEANING ---------------- #

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = [col.lower().strip() for col in df.columns]

print("Columns:", df.columns)

# Identify columns (adjust if needed after print)
rate_col = [col for col in df.columns if "rate" in col][0]
cost_col = [col for col in df.columns if "cost" in col][0]
name_col = [col for col in df.columns if "name" in col][0]
location_col = [col for col in df.columns if "location" in col][0]

# Clean rating
df[rate_col] = df[rate_col].astype(str).str.replace("/5", "")
df[rate_col] = pd.to_numeric(df[rate_col], errors="coerce")

# Clean cost
df[cost_col] = df[cost_col].astype(str).str.replace(",", "")
df[cost_col] = pd.to_numeric(df[cost_col], errors="coerce")

# Keep only required columns
df = df[[name_col, location_col, rate_col, cost_col]]

# Rename clean columns
df.columns = ["name", "location", "rate", "cost"]

# Create processed folder if not exists
os.makedirs("data/processed", exist_ok=True)

# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("✅ Data cleaned & saved to data/processed/")