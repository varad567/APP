"""
Experiment 12 - Exploratory Data Analysis on Customer Churn dataset (CO-4)
Identify significant patterns and clean the data for further analysis.
If 'customer_churn.csv' is not present, a sample dataset is generated.
"""
import os
import numpy as np
import pandas as pd

file_name = "customer_churn.csv"

# ---------- Create sample dataset if file not available ----------
if not os.path.exists(file_name):
    np.random.seed(1)
    n = 200
    df = pd.DataFrame({
        "CustomerID": range(1, n + 1),
        "Gender": np.random.choice(["Male", "Female"], n),
        "Age": np.random.randint(18, 70, n).astype(float),
        "Tenure": np.random.randint(0, 72, n),
        "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.5, 0.3, 0.2]),
        "MonthlyCharges": np.random.uniform(20, 120, n).round(2),
    })
    df["TotalCharges"] = (df["MonthlyCharges"] * df["Tenure"]).round(2)
    churn_prob = np.where(df["Contract"] == "Month-to-month", 0.45, 0.10)
    df["Churn"] = np.where(np.random.rand(n) < churn_prob, "Yes", "No")
    # Add some missing values and duplicates to clean later
    df.loc[np.random.choice(n, 8, replace=False), "Age"] = np.nan
    df.loc[np.random.choice(n, 5, replace=False), "MonthlyCharges"] = np.nan
    df = pd.concat([df, df.head(3)], ignore_index=True)
    df.to_csv(file_name, index=False)

df = pd.read_csv(file_name)

# ---------- 1. Understand the data ----------
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())

# ---------- 2. Data cleaning ----------
print("\nMissing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].mean())
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)

print("\nAfter cleaning -> Shape:", df.shape)
print("Missing values left:", df.isnull().sum().sum())

# ---------- 3. Patterns ----------
print("\nChurn distribution (%):\n", (df["Churn"].value_counts(normalize=True) * 100).round(2))
print("\nChurn rate by Contract (%):\n",
      (df.groupby("Contract")["Churn"].apply(lambda s: (s == "Yes").mean() * 100)).round(2))
print("\nChurn rate by Gender (%):\n",
      (df.groupby("Gender")["Churn"].apply(lambda s: (s == "Yes").mean() * 100)).round(2))
print("\nAverage values by Churn:\n",
      df.groupby("Churn")[["Tenure", "MonthlyCharges", "TotalCharges"]].mean().round(2))

df["ChurnFlag"] = (df["Churn"] == "Yes").astype(int)
print("\nCorrelation with churn:\n",
      df[["Age", "Tenure", "MonthlyCharges", "TotalCharges", "ChurnFlag"]].corr()["ChurnFlag"].round(3))

# ---------- 4. Save cleaned data ----------
df.to_csv("customer_churn_cleaned.csv", index=False)
print("\nCleaned data saved to 'customer_churn_cleaned.csv'")
