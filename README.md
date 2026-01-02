# Expense Fraud Detection Pipeline

## 📌 Project Overview
This project implements an end-to-end **Expense Fraud Detection Pipeline** using **MySQL, Python, and Microsoft Excel**.  
The goal is to identify suspicious expense claims using rule-based fraud detection and generate a business-friendly report.

---

## 🛠️ Technologies Used
- **MySQL** – Data storage and cleaning
- **Python (Pandas)** – Fraud detection logic
- **Microsoft Excel** – Final reporting and validation
- **Git & GitHub** – Version control

---

## 🔄 Workflow
1. Expense data is stored and cleaned in **MySQL**
2. Python connects to MySQL and reads cleaned data
3. Fraud detection rules are applied using Pandas
4. Suspicious claims are flagged with a fraud score
5. Final results are exported to **Excel**

---

## 🚨 Fraud Detection Rules Implemented
- High-value expense claims
- Duplicate claims by the same employee on the same day
- Expense claims submitted on weekends

---

## 📊 Output
- An Excel file `Flagged_Expense_Claims.xlsx` containing:
  - Fraud flags
  - Fraud scores
  - Suspicious expense records

---

## ▶️ How to Run the Project
1. Start MySQL server and ensure the database is available
2. Update MySQL credentials in `fraud_detection.py`
3. Run the script:
   ```bash
   python fraud_detection.py
