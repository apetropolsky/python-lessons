# Принцип подстановки Лисков (Liskov Substitution Principle, LSP)
#
# LSP гласит, что объекты в программе должны быть заменяемы на экземпляры их
# подтипов без изменения желаемых свойств программы. Это значит, что если
# класс S является подклассом класса T, то объекты класса T могут быть заменены
# объектами класса S без нарушения работы программы.
#
# Цель LSP — обеспечивать ситуацию, когда подклассы могут служить заменой для
# своих суперклассов, что улучшает модульность и повторное использование кода.
# Этот принцип подчеркивает важность совместимости интерфейсов,
# чтобы наследование использовалось правильно для обеспечения большей
# гибкости и переиспользуемости кода.


# Рассмотрим класс Rectangle и его подкласс Square. По логике, квадрат
# является частным случаем прямоугольника, но если в программе прямоугольник
# может изменять ширину и высоту независимо, замена его на объект квадрата
# может вызвать неправильное поведение.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height


# В этом случае, изменение ширины или высоты квадрата изменяет оба
# измерения, что нарушает ожидаемое поведение для прямоугольника.
#
# Чтобы соблюдать LSP, лучше избегать наследования между Rectangle и Square
# и вместо этого рассмотреть другие подходы, например, использование
# композиции или другой абстракции.


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size**2

