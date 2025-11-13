"""
Модуль моделей данных.

Содержит классы для представления основных сущностей приложения.
"""


class Expense:
    """Класс для представления расхода.

    Attributes:
        category (str): Категория расхода
        amount (float): Сумма расхода
        description (str): Описание расхода
    """

    def __init__(self, category, amount, description=""):
        """Инициализирует объект расхода.

        Args:
            category (str): Категория расхода
            amount (float): Сумма расхода
            description (str, optional): Описание расхода. По умолчанию "".
        """
        self.category = category
        self.amount = amount
        self.description = description


class Category:
    """Класс для представления категории расходов.

    Attributes:
        name (str): Название категории
    """

    def __init__(self, name):
        """Инициализирует объект категории.

        Args:
            name (str): Название категории
        """
        self.name = name