import json
import os

class JSONStore:
    def __init__(self, filepath):
        self.filepath = filepath
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump({"expenses": [], "budgets": {}}, f)


    def load_all(self):
        with open(self.filepath, "r") as f:
            return json.load(f)
        

    def save_all(self, data):
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4) 

    
    def load_expenses(self):
        return self.load_all()["expenses"]
    
    def save_expenses(self, expenses):
        data = self.load_all()
        data["expenses"] = expenses
        self.save_all(data)

        