class Category:
    def __init__(self, name):
        self.name = name


class Expense:
    def __init__(self, amount, category, description):
        # НАМЕРЕННАЯ ОШИБКА: amount и category перепутаны!
        self.category = amount      # ❌ должно быть self.amount = amount
        self.amount = category      # ❌ должно быть self.category = category
        self.description = description

    def __str__(self):
        return f"Расход: {self.amount} руб. на {self.category} ({self.description})"
      
      
class Category:
    def __init__(self, name):
        self.name = name

class Expense:
    def __init__(self, amount, category, description):
        # ❌ НАМЕРЕННАЯ ОШИБКА для задания №2
        self.category = amount    # должно быть: self.amount = amount
        self.amount = category    # должно быть: self.category = category
        self.description = description

    def __str__(self):
        return f"Расход: {self.amount} руб. на {self.category} ({self.description})"