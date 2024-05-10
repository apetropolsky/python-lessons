# Принцип открытости/закрытости (Open/Closed Principle, OCP)
#
# Принцип открытости/закрытости, один из пяти основных принципов SOLID,
# утверждает, что программные сущности (классы, модули, функции и т.д.)
# должны быть открыты для расширения, но закрыты для модификации. Это
# означает, что существующий код можно расширять новыми функциями без
# изменения уже существующего кода.
#
# Цель OCP — создать систему, которая будет устойчива к изменениям и легка в
# поддержке, позволяя разработчикам добавлять новую функциональность без
# нарушения существующего поведения системы.


class Notification:
    def __init__(self, user_contacts):
        self.user_contacts = user_contacts

    def send(self, message):
        print(f"Sending email to {self.user_contacts}: {message}")


# При добавлении SMS-уведомления, класс Notification требует модификации

# Улучшенный пример с соблюдением OCP
#
# Чтобы следовать OCP, мы можем определить общий интерфейс для всех типов
# уведомлений и расширять его для конкретных способов уведомления.


from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def __init__(self, user_email):
        self.user_email = user_email

    def send(self, message):
        print(f"Sending email to {self.user_email}: {message}")


class SMSNotification(Notification):
    def __init__(self, user_phone):
        self.user_phone = user_phone

    def send(self, message):
        print(f"Sending SMS to {self.user_phone}: {message}")


class DataStorage(ABC):
    def save_user(self, user):
        raise NotImplementedError


class UserDataStorage(DataStorage):
    def save_user(self, user):
        with open(f'{user.id}.txt', 'w') as f:
            f.write(f'Name: {user.name}')


class UserDatabaseStorage(DataStorage):
    def save_user(self, user):
        with conn:
            conn.insert(table_users, user)

