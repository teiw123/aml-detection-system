# AML Verification System

## 🚀 Overview
This project is a simple Anti-Money Laundering (AML) detection system built using Python and SQLite.  
It analyzes transaction data and identifies suspicious financial behavior using rule-based logic.

---

## ✅ Features
- Detects high-frequency transactions (possible structuring)
- Detects large-value transactions
- Flags suspicious accounts automatically
- SQLite database integration
- Modular Python backend
- Includes test suite

---

## 🧠 AML Detection Rules
The system flags accounts based on:

1. High transaction frequency (≥ 5 transactions)
2. Large total transaction value (> 800)
3. Repeated same-value transactions (structuring)

---

## 📁 Project Structure