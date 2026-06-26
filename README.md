# AML Detection System

## 🚀 Overview
This project is an Anti-Money Laundering (AML) detection system built using Python and SQLite.  
It analyzes transaction data and identifies suspicious financial behavior using both **rule-based logic** and optional **machine learning models**.

## ✅ Features
- Detects high-frequency transactions (possible structuring)
- Detects large-value transactions
- Flags suspicious accounts automatically
- SQLite database integration
- Modular Python backend
- Includes test suite
- Optional ML-based risk scoring
- Dashboard visualization

## 🧠 AML Detection Rules
The system flags accounts based on:
1. High transaction frequency (≥ 5 transactions)
2. Large total transaction value (> 800)
3. Repeated same-value transactions (structuring)

## 📁 Project Structure
- `main.py` → core detection logic  
- `database/` → SQLite schema and data  
- `models/` → ML models (optional)  
- `tests/` → unit tests  

## ⚙️ Installation
```bash
git clone https://github.com/teiw123/aml-detection-system.git
cd aml-detection-system
pip install -r requirements.txt
git clone https://github.com/teiw123/aml-detection-system.git
cd aml-detection-system
pip install -r requirements.txt
python main.py
