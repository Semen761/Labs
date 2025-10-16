def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user):
            if user['role'] in allowed_roles:
                return func(user)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None
        return wrapper
    return decorator

@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"

@require_role(["admin", "manager"])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки сохранены"

@require_role(["user", "admin", "manager"])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные показаны"

пользователи = [
    {"name": "Админ", "role": "admin"},
    {"name": "Менеджер", "role": "manager"}, 
    {"name": "Обычный пользователь", "role": "user"},
    {"name": "Гость", "role": "guest"}
]

print("Тестируем доступ к удалению базы данных:")
for user in пользователи:
    print(f"\nПользователь: {user['name']} (роль: {user['role']})")
    delete_database(user)

print("\nТестируем доступ к изменению настроек:")
for user in пользователи:
    print(f"\nПользователь: {user['name']} (роль: {user['role']})")
    edit_settings(user)

print("\nТестируем доступ к просмотру данных:")
for user in пользователи:
    print(f"\nПользователь: {user['name']} (роль: {user['role']})")
    view_data(user)

