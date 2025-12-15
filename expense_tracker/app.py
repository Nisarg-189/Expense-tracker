from colorama import Fore, init
from services.expense_services import ExpenseServices
from services.budget_services import BudgetServices
from analytics.charts import show_monthly_trend
from storage.json_storage import JSONStore

init(autoreset=True)

store = JSONStore("data/expenses.json")
expense_service = ExpenseServices(store)
budget_service = BudgetServices(store)

def menu():
    print(Fore.CYAN + "\n===== EXPENSE TRACKER =====")
    print(Fore.YELLOW + "1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Set Budget")
    print("5. Show Analytics")
    print("6. Exit")

while True:
    menu()
    choice = input(Fore.GREEN + "Enter choice: ")

    if choice == "1":
        expense_service.add_expense()
    elif choice == "2":
        expense_service.view_expenses()
    elif choice == "3":
        expense_service.delete_expense()
    elif choice == "4":
        budget_service.set_budget()
    elif choice == "5":
        show_monthly_trend(store.load_expenses())
    elif choice == "6":
        print(Fore.RED + "Exiting... Bye bro 👋")
        break
    else:
        print(Fore.RED + "Invalid choice!")
