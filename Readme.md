# 🛒 GMart Retail Sales Analytics & Business Intelligence System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

An **end-to-end Retail Sales Analytics project** that analyzes transactional data to generate **business insights**, track **sales performance**, and build a **comprehensive analytics dashboard**.

This project simulates how retail businesses:

* Monitor sales trends 📈
* Understand customer behavior 🧠
* Optimize pricing and discounts 💰
* Improve business decision-making

---

## 🎯 Key Objectives

* Analyze sales performance across time, categories, and cities
* Identify top-performing products and regions
* Understand customer purchasing patterns
* Evaluate the impact of discounts on revenue
* Generate actionable business insights

---

## 🏗️ Project Architecture

```text
Data → Cleaning → Feature Engineering → EDA → Visualization → Database → Insights
```

---

## 📂 Project Structure

```text
gmart-sales-analytics/
│
├── data/
│   └── Gmart_sales_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── visualization.py
│   ├── database.py
│   └── insights.py
│
├── gmart_sales_dashboard.png
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Features

✔️ Data Cleaning & Preprocessing

✔️ Feature Engineering (Time Features, Metro vs Non-Metro Classification)

✔️ Exploratory Data Analysis (EDA)

✔️ Sales Analytics Dashboard

✔️ MySQL Database Integration

✔️ Business Insights Generation

---

## 📊 Dashboard

![GMart Sales Dashboard](gmart_sales_analytics.png)

### Insights from Dashboard:

* 📌 Certain product categories dominate overall revenue
* 📌 Metro cities contribute significantly higher sales
* 📌 High discounts do not always translate into higher revenue
* 📌 Customer spending follows a skewed distribution (few high-value customers)

---

## 🛠️ Tech Stack

| Category       | Tools Used    |
| -------------- | ------------- |
| Language       | Python        |
| Data Analysis  | Pandas        |
| Visualization  | Matplotlib    |
| Database       | MySQL         |
| ORM            | SQLAlchemy    |
| Env Management | python-dotenv |

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
DB_CONNECTION=mysql+mysqlconnector://username:password@localhost/dataanalysisproject
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/gmart-sales-analytics.git
cd gmart-sales-analytics
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Dataset

Place your dataset inside:

```text
data/Gmart_sales_data.csv
```

### 4️⃣ Setup Environment Variables

Create `.env` file and configure your database credentials

### 5️⃣ Run Project

```bash
python main.py
```

---

## 📈 Output

* 📊 Sales Analytics Dashboard
* 📉 Category & City Performance Analysis
* 🧠 Customer Spending Insights
* 🗄️ Data stored in MySQL (optional)

---

## 🔍 Key Business Insights

* A few product categories contribute the majority of total revenue
* Metro cities outperform non-metro regions in sales performance
* High discount percentages can reduce profitability margins
* Top 20% of customers contribute a significant portion of total revenue (Pareto Principle)

---

## 📬 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/varun-sai-kedarisetty-bb86bb23b/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Visit%20Profile-blue?style=for-the-badge&logo=linkedin" />
  </a>
</p>

---
