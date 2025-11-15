import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.title("💰 DailyBudgetPro – Expense Tracker")

# Load or initialize data
def load_data():
    try:
        return pd.read_csv("expenses.csv")
    except:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])


def save_data(df):
    df.to_csv("expenses.csv", index=False)


df = load_data()

st.sidebar.header("Add New Expense")

# Input fields for adding expenses
date = st.sidebar.date_input("Select Date", datetime.today())
category = st.sidebar.selectbox(
    "Select Category",
    ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]
)
amount = st.sidebar.number_input("Amount (₹)", min_value=0.0, format="%.2f")
description = st.sidebar.text_input("Description")

if st.sidebar.button("Add Expense"):
    new_entry = {
        "Date": date.strftime("%Y-%m-%d"),
        "Category": category,
        "Amount": amount,
        "Description": description
    }

    # FIXED: pandas append() removed → using concat
    new_row = pd.DataFrame([new_entry])
    df = pd.concat([df, new_row], ignore_index=True)

    save_data(df)
    st.success("Expense Added Successfully!")

st.header("📘 Expense History")
st.dataframe(df)

# Total Expense
if not df.empty:
    st.subheader("💵 Total Spent: ₹" + str(df["Amount"].sum()))

# Category-wise Pie Chart
st.subheader("📊 Expense Breakdown by Category")

if not df.empty:
    category_totals = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%")
    ax.axis("equal")
    st.pyplot(fig)

# Download CSV
st.download_button(
    label="⬇ Download Expense Report",
    data=df.to_csv(index=False),
    file_name="DailyBudgetPro_Report.csv",
    mime="text/csv"
)
