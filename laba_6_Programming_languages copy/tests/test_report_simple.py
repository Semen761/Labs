def add_expense_command(storage, amount, category, description):
    expense, error = storage.add_expense(amount, category, description)
    if error:
        return f"Ошибка: {error}"
    return f"Добавлено: {expense['amount']} руб. на {expense['category']}"

def list_expenses_command(storage):
    expenses = storage.get_all_expenses()
    if not expenses:
        return "Расходы отсутствуют."
    lines = ["Расходы:"]
    for e in expenses:
        lines.append(f"- {e['amount']} руб. на {e['category']}: {e['description']}")
    return "\n".join(lines)