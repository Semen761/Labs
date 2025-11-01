class Expense:
    def __init__(self, category, amount, description=""):
        self.category = category
        self.amount = amount
        self.description = description

class Category:
    def __init__(self, name):
        self.name = name