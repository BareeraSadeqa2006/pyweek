import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

st.title("Loan EMI Calculator")
st.write("Calculate your Monthly EMI, Total Interest, and Amortization Schedule")

# Inputs
loan = st.number_input("Enter Loan Amount (₹)", min_value=1000, step=1000)
rate = st.number_input("Annual Interest Rate (%)", min_value=1.0, step=0.1)
years = st.number_input("Loan Tenure (Years)", min_value=1, step=1)

if loan and rate and years:

    r = rate / (12 * 100)  # monthly interest rate
    n = years * 12  # total months

    # EMI formula
    emi = loan * r * (math.pow((1 + r), n)) / (math.pow((1 + r), n) - 1)

    st.subheader(f"Monthly EMI: ₹{emi:.2f}")

    total_payment = emi * n
    total_interest = total_payment - loan

    st.write(f"**Total Interest:** ₹{total_interest:.2f}")
    st.write(f"**Total Amount Paid:** ₹{total_payment:.2f}")

    # ----------------------------
    # Amortization Table
    # ----------------------------
    balance = loan
    data = []

    for month in range(1, n + 1):
        interest_paid = balance * r
        principal_paid = emi - interest_paid
        balance -= principal_paid
        data.append([month, emi, principal_paid, interest_paid, max(balance, 0)])

    df = pd.DataFrame(data, columns=["Month", "EMI", "Principal", "Interest", "Balance"])

    st.subheader("Amortization Schedule")
    st.dataframe(df)

   
    st.subheader("Interest vs Principal Chart")

    plt.figure(figsize=(8, 4))
    plt.plot(df["Month"], df["Principal"])
    plt.plot(df["Month"], df["Interest"])
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.title("Interest vs Principal Over Time")
    st.pyplot(plt)

