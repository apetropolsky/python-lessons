# Определение миксинов
#
# Миксины — это классы, которые предоставляют методы для использования
# другими классами без необходимости становиться их базовым классом.
#
# Миксины позволяют программистам добавлять функциональность
# к классам способом, который поддерживает чистую композицию и
# избегает проблем множественного наследования.

# Цель использования миксинов
#
# Миксины используются для расширения функциональности классов
# путём добавления методов и свойств,
# которые логически не привязаны к основной иерархии наследования класса:
#
#     Обеспечивают возможность повторного использования кода.
#     Помогают избежать дублирования кода.
#     Предоставляют чёткое разделение функциональности по классам.

# Пример миксина для логирования
#
# Рассмотрим миксин, который добавляет функциональность логирования в
# любой класс, который его использует:


class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")


class DB:
    def data_operation(self, data):
        pass


class DatabaseOracle(LoggerMixin, DB):
    def data_operation(self, data):
        self.log(f"Operating on {data}")


db = DatabaseOracle()
db.data_operation("some data")


# Миксин для JSON сериализации
#
# Этот миксин добавляет методы для сериализации и десериализации
# объектов класса в JSON:


import json


class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)


class Contact(JsonMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


contact = Contact("John Doe", "john@example.com")
json_str = contact.to_json()
new_contact = Contact.from_json(json_str)

print(json_str)  # Выводит JSON строку
print(new_contact.name, new_contact.email)  # Выводит "John Doe john@example.com"


# Миксины могут значительно повысить гибкость системы,
# позволяя смешивать и сочетать нужные функции по мере необходимости,
# добавляя горизонтальное масштабирование и
# уменьшая зависимость от жёстких иерархий наследования.
