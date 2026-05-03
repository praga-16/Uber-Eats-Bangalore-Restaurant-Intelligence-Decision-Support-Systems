import streamlit as st
import sqlite3
import pandas as pd

# Connect DB
conn = sqlite3.connect("restaurant.db")

st.set_page_config(page_title="Uber Eats Dashboard", layout="wide")

st.title("🍔 Uber Eats Restaurant Intelligence Dashboard")

# Load data
df = pd.read_sql("SELECT * FROM restaurants", conn)

# Sidebar Filters
st.sidebar.header("🔍 Filters")

location = st.sidebar.selectbox("Select Location", ["All"] + sorted(df["location"].dropna().unique()))

filtered_df = df.copy()

if location != "All":
    filtered_df = filtered_df[filtered_df["location"] == location]

# Display Data
st.subheader("📊 Restaurant Data")
st.dataframe(filtered_df)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Restaurants", len(filtered_df))
col2.metric("Avg Rating", round(filtered_df["rate"].mean(), 2))
col3.metric("Avg Cost", round(filtered_df["cost"].mean(), 2))

# ---------------- BUSINESS INSIGHTS ---------------- #

st.subheader("🧠 Business Insights")

question = st.selectbox("Choose Analysis", [
    "Top Rated Locations",
    "Most Restaurants (Saturation)",
    "Cost vs Rating",
    "Best Price Range"
])

if question == "Top Rated Locations":
    query = """
    SELECT location, AVG(rate) as avg_rating
    FROM restaurants
    GROUP BY location
    ORDER BY avg_rating DESC
    LIMIT 10;
    """

elif question == "Most Restaurants (Saturation)":
    query = """
    SELECT location, COUNT(*) as total
    FROM restaurants
    GROUP BY location
    ORDER BY total DESC
    LIMIT 10;
    """

elif question == "Cost vs Rating":
    query = """
    SELECT cost, AVG(rate) as avg_rating
    FROM restaurants
    GROUP BY cost
    ORDER BY cost;
    """

elif question == "Best Price Range":
    query = """
    SELECT 
        CASE 
            WHEN cost < 500 THEN 'Low'
            WHEN cost BETWEEN 500 AND 1000 THEN 'Mid'
            ELSE 'Premium'
        END as price_category,
        AVG(rate) as avg_rating
    FROM restaurants
    GROUP BY price_category;
    """

result = pd.read_sql(query, conn)

st.dataframe(result)

conn.close()