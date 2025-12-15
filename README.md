# 💰 Expense Tracker (Python – JSON Storage)

A clean, menu‑driven **CLI expense tracker** built with Python that allows users to manage daily expenses, set budgets, and generate spending analytics. The project uses **JSON-based persistence** and follows a **modular, scalable architecture** suitable for real‑world backend extensions.


---


## 🚀 Features

* Add, view, and delete expenses
* Automatic ID reindexing after deletion (no gaps)
* Expense categorization (Food, Travel, Study, etc.)
* Monthly budgets per category
* Colored terminal interface for better UX
* Spending analytics with charts saved as images


---


## 🗂️ Project Structure (JSON‑Only)

```
expense_tracker/
│
├── app.py
│
├── models/
│   └── expense.py
│
├── services/
│   ├── expense_service.py
│   └── budget_service.py
│
├── storage/
│   └── json_store.py
│
├── analytics/
│   └── charts.py
│
├── utils/
│   └── date_utils.py
│
├── data/
│   ├── expenses.json
│   └── charts/
│       └── monthly_spending.png
│
└── requirements.txt
```


---

## ⚙️ Installation


```bash
git clone https://github.com/yourusername/expense-tracker-python.git
cd expense-tracker-python
pip install -r requirements.txt
```

**Requirements**

* Python 3.9+
* colorama
* pandas
* matplotlib


---


## ▶️ Usage

Run the application:

```bash
python app.py
```

Menu options:

* Add Expense
* View Expenses
* Delete Expense
* Set Budget
* Show Analytics
* Exit

Expenses are stored persistently in `data/expenses.json`.


---


## 📊 Analytics

* Monthly spending trend is generated using Pandas and Matplotlib
* Charts are **saved as image files** instead of opening GUI windows
* This ensures compatibility with:

  * GitHub Codespaces
  * VS Code terminal
  * Server / headless environments

Generated charts are stored in:

```
data/charts/
```

Example:

* `monthly_spending.png`


---


## 🎨 Terminal Experience

* Cyan → headers
* Green → success messages
* Yellow → warnings
* Red → errors / exit

The colored CLI improves clarity and usability without external UI frameworks.


---


⭐ If you find this project useful, feel free to star the repository.
