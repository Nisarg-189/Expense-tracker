class Expense:
    def __init__(self, eid, date, amount, category, note):
        self.id = eid
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "note": self.note
        }