# 🍔 Uber Eats Bangalore Restaurant Intelligence & Decision Support System

## 📌 Overview
This project is an end-to-end **data analytics and decision support system** built to analyze restaurant data from Bangalore and extract actionable business insights.

It simulates a real-world analytics system used by food delivery platforms like Uber Eats or Zomato to support decisions such as:
- Where to expand
- Which restaurants to onboard
- Optimal pricing strategies
- Customer satisfaction analysis

---

## 🎯 Objectives
- Perform data cleaning and preprocessing on raw restaurant data  
- Store structured data in a relational database (SQLite)  
- Use SQL queries to extract business insights  
- Build an interactive dashboard using Streamlit  
- Provide a decision support system for stakeholders  

---

## 🏗️ Project Architecture
```

Raw CSV Data
↓
Data Cleaning (Pandas)
↓
Feature Engineering
↓
SQLite Database
↓
SQL Queries
↓
Streamlit Dashboard

```
---

## 🛠️ Tech Stack

| Category       | Tools Used    |
|----------------|---------------|
| Programming    | Python        |
| Data Handling  | Pandas, NumPy |
| Database       | SQLite        |
| Visualization  | Streamlit     |
| Query Language | SQL           |

---


## 🔄 Data Pipeline

### 1. Data Cleaning
- Removed duplicates
- Handled missing values
- Standardized column formats
- Converted ratings and cost to numeric values

### 2. Feature Engineering
- Derived price categories (Low, Mid, Premium)
- Structured columns for analysis

### 3. Database Integration
- Stored cleaned data into SQLite
- Designed schema for restaurant analytics

### 4. SQL Analytics
- Aggregations using `GROUP BY`
- Filtering using `WHERE`
- Categorization using `CASE WHEN`

---

## 📊 Dashboard Features

### 🔍 Filters
- Location-based filtering
- Dynamic dataset exploration

### 📈 Metrics
- Total restaurants
- Average rating
- Average cost

### 🧠 Business Insights
- Top-rated locations
- Market saturation analysis
- Cost vs rating trends
- Optimal pricing strategy

---

## 📸 Screenshots 

### Dashboard View
<img width="1918" height="1025" alt="image" src="https://github.com/user-attachments/assets/b5ebf204-ec44-4a6c-8282-67475db9c37f" />


### Insights View
<img width="1917" height="1024" alt="image" src="https://github.com/user-attachments/assets/eb9372ed-3057-4bf9-a0e4-6594faf02eb4" />

---

## 🧠 Key Business 

- Which locations have the highest-rated restaurants?
- Which areas are over-saturated with restaurants?
- What is the relationship between cost and rating?
- What price range yields the highest customer satisfaction?
- Which locations are ideal for premium restaurant expansion?

---

## 📈 Key Insights

- Mid-priced restaurants tend to have higher average ratings  
- Some locations are highly saturated, reducing entry potential  
- Higher cost does not always guarantee better ratings  
- Certain areas show strong potential for premium dining  

---

## 🚀 How to Run the Project

### 1. Clone Repository
```bash
git clone https://github.com/praga-16/Uber-Eats-Bangalore-Restaurant-Intelligence-Decision-Support-Systems.git
cd Uber-Eats-Bangalore-Restaurant-Intelligence-Decision-Support-Systems
2. Install Dependencies
pip install pandas numpy streamlit
3. Run Data Pipeline
python scripts/data_cleaning.py
python scripts/db_insert.py
4. Launch Dashboard
```
streamlit run app.py
```
```

## 🔥 Highlights
End-to-end pipeline (CSV → SQL → Dashboard)
Real-world business problem solving
SQL-driven analytics (not hardcoded)
Scalable and modular architecture
Industry-relevant insights
## 🚀 Future Enhancements
Machine learning model for rating prediction
Restaurant recommendation system
Real-time data integration
Cloud deployment (Streamlit Cloud / AWS)
Interactive visual analytics
## 👨‍💻 Author

Pragatheesvaran A B
📧 pragatheesvaranab@gmail.com

🔗 GitHub: https://github.com/praga-16

🔗 Portfolio: https://pragatheesvaranab.vercel.app
