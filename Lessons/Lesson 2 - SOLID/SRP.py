

# Принцип единственной ответственности (Single Responsibility Principle, SRP)
#
# Принцип единственной ответственности гласит, что класс должен иметь одну и
# только одну причину для изменения. Это означает, что класс должен
# выполнять только одну функцию или задачу в системе, иметь одну область
# ответственности, и следовательно, только один мотив для изменения.
#
# Цель SRP — упростить компоненты системы, делая их легче для понимания,
# тестирования, отладки и обслуживания. Классы, соблюдающие SRP, обычно
# меньше и чище, и их легче изменять, поскольку изменения в одной части
# системы влияют на меньшее количество других частей.


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name


class UserManager:
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user.name = new_name

    def save_user(self):
        with open(f'{self.user.id}.txt', 'w') as f:
            f.write(f'Name: {self.user.name}')


user_manager = UserManager(User(1, 'John Doe'))
user_manager.change_user_name('Jane Doe')
user_manager.save_user()

# В этом примере UserManager имеет две причины для изменения:
#
#     Изменение способа управления информацией пользователя.
#     Изменение механизма сохранения данных пользователя.


class UserProfile:
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user.name = new_name


class UserDataStorage:
    def save_user(self, user):
        with open(f'{user.id}.txt', 'w') as f:
            f.write(f'Name: {user.name}')


class UserDatabaseStorage:
    def save_user_database(self, user):
        with conn:
            conn.insert(table_users, user)


user = User(1, 'John Doe')
profile = UserProfile(user)
profile.change_user_name('Jane Doe')

# storage = UserDataStorage()
storage = UserDatabaseStorage()
storage.save_user_database(user)
