from colorama import Fore
from datetime import date
from models.expense import Expense

class ExpenseServices:
    def __init__(self, store):
        self.store = store

    def add_expense(self):

        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Note: ")

        
        expenses = self.store.load_expenses()
        eid = len(expenses) + 1

        expense = Expense(
            eid,
            str(date.today()),
            amount, 
            category,
            note
        )


        expenses.append(expense.to_dict())
        self.store.save_expenses(expenses)


        print(Fore.GREEN + "✅ Expense added successfully! ")


    def view_expenses(self):
        expenses = self.store.load_expenses()
        print(Fore.CYAN + "\n----EXPENSES----")
        for e in expenses:
            print(f"{e['id']} | {e['date']} | ₹{e['amount']} | {e['category']} | {e['note']}")

    
    def delete_expense(self):
        expenses = self.store.load_expenses()
        eid = int(input("Enter expense ID to delete: "))
        
        new_expenses = [e for e in expenses if e["id"] != eid]
        
        if len(new_expenses) == len(expenses):
            print(Fore.RED + "❌ Expense ID not found")
            return

    # 🔁 Reassign IDs
        for index, expense in enumerate(new_expenses, start=1):
            expense["id"] = index
            
        self.store.save_expenses(new_expenses)
        print(Fore.YELLOW + "⚠ Expense deleted and IDs updated")

   