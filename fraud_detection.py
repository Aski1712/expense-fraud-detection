import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql.11@@1705",
    database="expense_fraud"
)

query = "SELECT * FROM cleaned_expense_claims"
df = pd.read_sql(query, conn)

print(df)

conn.close()

# -------- FRAUD RULES --------

# Rule 1: High amount expenses
df['high_amount_flag'] = df['amount'] > 10000

# Rule 2: Duplicate claims by same employee on same day
df['duplicate_claim_flag'] = df.duplicated(
    subset=['employee_id', 'expense_date'],
    keep=False
)

# Rule 3: Weekend expense claims
df['expense_day'] = pd.to_datetime(df['expense_date']).dt.day_name()
df['weekend_flag'] = df['expense_day'].isin(['Saturday', 'Sunday'])

# Fraud score
df['fraud_score'] = (
    df['high_amount_flag'].astype(int) +
    df['duplicate_claim_flag'].astype(int) +
    df['weekend_flag'].astype(int)
)

# Filter suspicious claims
fraud_df = df[df['fraud_score'] > 0]

print("\n🚨 Flagged Fraud Cases:")
print(fraud_df)

# Export to Excel
fraud_df.to_excel("Flagged_Expense_Claims.xlsx", index=False)

print("\n✅ Excel report generated: Flagged_Expense_Claims.xlsx")

