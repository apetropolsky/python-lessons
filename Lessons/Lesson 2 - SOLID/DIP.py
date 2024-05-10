# Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)

# DIP предлагает две основные идеи:
#
#     1. Модули высокого уровня не должны зависеть от модулей низкого уровня.
#     Оба типа модулей должны зависеть от абстракций.
#
#     2. Абстракции не должны зависеть от деталей. Детали должны зависеть от
#     абстракций.
#
# Этот принцип направлен на уменьшение прямых зависимостей между
# компонентами программы, что позволяет упростить модификацию и
# масштабирование приложения.

# Цель DIP — обеспечение гибкости и масштабируемости системы путем
# инвертирования зависимостей. Это снижает взаимное влияние изменений в
# различных частях программы, упрощает тестирование и поддержку.


# Рассмотрим систему, где класс высокого уровня
# прямо зависит от класса низкого уровня.

class LightBulb:
    def enable(self):
        print("LightBulb: turned on")

    def disable(self):
        print("LightBulb: turned off")


class ElectricPowerSwitch:
    def __init__(self):
        self.lightBulb = LightBulb()
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.disable()
            self.on = False
        else:
            self.lightBulb.enable()
            self.on = True

# В этом примере ElectricPowerSwitch зависит напрямую
# от конкретной детали — LightBulb, что затрудняет замену источника света
# на другой тип устройства без изменения переключателя.

# Чтобы следовать DIP, необходимо определить абстракцию, от которой будут
# зависеть модули как высокого, так и низкого уровня.

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def enable(self):
        raise NotImplementedError

    @abstractmethod
    def disable(self):
        raise NotImplementedError


class LightBulb(Switchable):
    def enable(self):
        print("LightBulb: turned on")

    def disable(self):
        print("LightBulb: turned off")


class Fan(Switchable):
    def enable(self):
        print("Fan: turned on")

    def disable(self):
        print("Fan: turned off")


class ElectricPowerSwitch:
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.disable()
            self.on = False
        else:
            self.client.enable()
            self.on = True


fan = Fan()
bulb = LightBulb()
switch = ElectricPowerSwitch(bulb)

switch.press()

# В этом примере ElectricPowerSwitch теперь зависит от абстракции Switchable,
# что позволяет легко подключить любое устройство
# (например, LightBulb или Fan), следующее этой абстракции,
# не изменяя код переключателя.

# Соблюдение принципа инверсии зависимостей делает систему более гибкой
# и устойчивой к изменениям, так как добавление новой функциональности
# или изменение существующей не требует изменений в других частях программы,
# что значительно упрощает процесс разработки и поддержки. Это особенно важно
# в крупных и сложных системах, где изменения могут вызывать серьезные
# побочные эффекты.
