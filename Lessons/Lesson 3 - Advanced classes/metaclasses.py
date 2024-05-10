# ДИСКЛЕЙМЕР:
#
#       Метаклассы это глубокая магия, о которой 99% пользователей даже
#       не нужно задумываться. Если вы думаете, нужно ли вам их использовать —
#       вам не нужно (люди, которым они реально нужны, точно знают,
#       зачем они им, и не нуждаются в объяснениях, почему).
#                                           ~ уже известный нам Тим Питерс
#
# И по факту реально так и есть. Эта ебанина в подавляющем большинстве
# случаев никому не нужна и с высокой долей вероятности код, написанный с
# применением метаклассов написан так потому, что кто-то хотел выебнуться.

# Определение метаклассов
#
# Метаклассы в Python — это классы классов. Они определяют правила и поведение
# других классов, так же как обычные классы определяют поведение
# своих объектов (экземпляров).
#
# Метаклассы предоставляют мощный инструмент для
# продвинутого программирования, позволяя влиять на создание и поведение
# классов на этапе их определения.

# Метаклассы позволяют:
#
#     Изменять классы непосредственно перед их созданием.
#     Взаимодействовать с атрибутами класса до его использования.
#     Регистрировать или модифицировать классы при их определении.
#     Применять шаблоны проектирования, такие как Singleton,
#       без изменения самих классов.
#
# Одной из самых распространенных задач для метаклассов
# является контроль и модификация атрибутов класса:


class Meta(type):

    def __new__(mcs, name, bases, dct):
        # Добавим новый атрибут к классу
        dct['class_id'] = f"Class_{name.upper()}"
        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=Meta):
    x = 5


print(MyClass.class_id)  # Вывод: Class_MYCLASS

# В этом примере метакласс Meta добавляет атрибут class_id каждому классу,
# который использует этот метакласс. Метод __new__ используется для интервенции
# в процесс создания класса.
#
# Применение метакласса для паттерна Singleton
#
# Метакласс может быть использован для реализации паттерна проектирования
# Singleton, который ограничивает создание экземпляров класса одним объектом:


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass


class OtherSingletonClass(metaclass=SingletonMeta):
    pass


obj1 = SingletonClass()
obj2 = SingletonClass()
obj3 = OtherSingletonClass()
obj4 = OtherSingletonClass()

print(obj1 is obj2)  # Вывод: True
print(obj3 is obj4)  # Вывод: True
print(obj1 is obj3)  # Вывод: False

# В этом примере SingletonMeta контролирует создание экземпляров
# SingletonClass и OtherSingletoneClass, гарантируя, что всякий раз для
# любого из этих классов будет возвращаться один и тот же объект, но для
# разных классов — разные.
