# 💰 Expense Tracker with Analytics (Python)

A **clean, scalable Python expense tracker** that evolves from simple file-based storage to a full SQLite-backed system with **analytics and visualizations**. This project demonstrates real-world software engineering practices including data modeling, persistence layers, and clean architecture.

---

## 🚀 Features

### Core

* Add, edit, delete expenses
* Expense categories (Food, Travel, Study, Gym, etc.)
* Notes & date-based entries

### Budgets

* Monthly budgets per category
* Overspending alerts

### Storage (Progressive)

* CSV storage
* JSON storage
* SQLite database (production-ready)

### Analytics

* Monthly spending trends
* Category-wise expense breakdown
* Budget vs actual spending comparison

---

## 🧠 What You’ll Learn

* Python data structures & OOP
* File handling → database migration
* SQL & SQLite integration
* Data aggregation & analysis
* Clean architecture & modular design
* Data visualization with Matplotlib

---

## 🗂️ Project Structure

```
expense_tracker/
│
├── app.py                     # Entry point
│
├── models/
│   └── expense.py             # Expense data model
│
├── services/
│   ├── expense_service.py     # Expense logic (CRUD)
│   ├── budget_service.py      # Budget calculations
│
├── storage/
│   ├── csv_store.py           # CSV persistence
│   ├── json_store.py          # JSON persistence
│   ├── db_store.py            # SQLite persistence
│
├── analytics/
│   └── charts.py              # Data visualization
│
├── utils/
│   └── date_utils.py          # Date helpers
│
└── data/
    └── expenses.db            # SQLite database
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/expense-tracker-python.git
cd expense-tracker-python
pip install -r requirements.txt
```

**Dependencies**

* Python 3.9+
* matplotlib
* pandas

---

## ▶️ Usage

```bash
python app.py
```

Menu options:

* Add expense
* View expenses
* Edit / delete expense
* Set monthly budget
* View analytics

---

## 📊 Analytics Preview

* 📈 Monthly spending line chart
* 🥧 Category-wise pie chart
* 📊 Budget vs actual bar chart

---

## 🧪 Data Migration Path

1. Start with CSV storage
2. Migrate to JSON for structured data
3. Upgrade to SQLite for scalability

This mirrors **real-world backend evolution**.

---

## 🔮 Future Enhancements

* User authentication
* Export reports as PDF
* REST API using Flask / FastAPI
* Web or GUI interface
* Cloud database integration

---

## 📌 Why This Project Matters

✔ Demonstrates backend thinking
✔ Shows data → database → analytics flow
✔ Recruiter-friendly & resume-ready
✔ Scalable and production-inspired design

---

## 📜 License

MIT License

---

### ⭐ If you find this project useful, consider giving it a star!
