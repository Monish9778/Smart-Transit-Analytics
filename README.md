# 🚍 Smart Transit Analytics

Smart Transit Analytics is an **end-to-end data analytics and machine learning project** that analyzes **public transport usage and route efficiency** to identify inefficient routes and improve urban transit planning.



---

## 📌 Project Overview

Public transport systems generate large volumes of operational data but often lack data-driven insights to optimize routes, fuel usage, and passenger flow.

This project:
- Analyzes public transport usage data
- Calculates route efficiency metrics
- Uses machine learning to classify route performance
- Visualizes insights using an interactive dashboard

---

## 🎯 Problem Statement

Urban public transport authorities face challenges such as:
- Inefficient routes with low passenger utilization
- High fuel consumption
- Longer travel times
- Lack of analytical tools to evaluate route performance

**Goal:**  
Build a data-driven analytics system to evaluate and improve public transport route efficiency.

---

## ✅ Solution Approach

1. Generate / collect public transport data
2. Clean and preprocess the dataset
3. Perform exploratory data analysis (EDA)
4. Calculate efficiency KPIs
5. Apply machine learning for route clustering
6. Visualize insights using a dashboard

---

---

## 📊 Dataset Description

The dataset represents daily public transport route operations.

### Columns:
- `route_id` – Unique route identifier  
- `bus_id` – Vehicle identifier  
- `date` – Operation date  
- `passenger_count` – Number of passengers  
- `route_distance_km` – Distance of the route (km)  
- `travel_time_min` – Travel time (minutes)  
- `fuel_consumed_liters` – Fuel consumed  

---

## 🤖 Machine Learning Model

- **Algorithm:** K-Means Clustering  
- **Purpose:** Group routes into efficiency categories
- **Clusters:**
  - High Efficiency
  - Medium Efficiency
  - Low Efficiency

This helps transport planners focus on poorly performing routes.

---

## 📊 Dashboard Features

Built using **Streamlit**:
- Route-wise passenger analysis
- Efficiency comparison
- Interactive tables and charts
- Easy-to-understand insights for decision-making

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

## 📦 Installation & Usage

###  Install Dependencies
pip install -r requirements.txt


###  Run Dashboard
streamlit run dashboard/app.py


---

## 📈 Project Outcomes

- Identified inefficient transport routes
- Improved understanding of passenger utilization
- Highlighted fuel and time inefficiencies
- Demonstrated complete data analytics workflow

---

## 🚀 Future Enhancements

- Predict passenger demand
- Add GPS-based route optimization
- Include real-time data streaming
- Deploy dashboard to Streamlit Cloud
 





