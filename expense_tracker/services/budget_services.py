from colorama import Fore

class BudgetServices:
    def __init__(self, store):
        self.store = store

    def set_budget(self):
        category = input("Category: ")
        limit = float(input("Monthly limit: "))

        data = self.store.load_all()
        data["budgets"][category] = limit
        self.store.save_all(data)

        print(Fore.GREEN + "Budget set successfully!")
        