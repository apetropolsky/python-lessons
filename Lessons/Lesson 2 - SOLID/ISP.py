# Принцип разделения интерфейса (Interface Segregation Principle, ISP)
#
# ISP утверждает, что клиенты не должны быть вынуждены зависеть от
# интерфейсов, которыми они не пользуются.

# Этот принцип направлен на сокращение ненужных зависимостей между классами,
# предотвращая ситуации, когда изменения в одном классе могут привести к
# ненужным изменениям в других классах, которые используют тот же интерфейс.

# Цель ISP — создать такие интерфейсы, которые описывают только те методы,
# которые реально нужны их клиентам. Это приводит к созданию более мелких и
# более специализированных интерфейсов, что улучшает модульность
# кода и его гибкость.


class Device:
    def print(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Device):
    def print(self, document):
        print("Print", document)

    def scan(self, document):
        print("Scan", document)

    def fax(self, document):
        print("Fax", document)


class SimplePrinter(Device):
    def print(self, document):
        print("Print", document)

    def scan(self, document):
        raise NotImplementedError("This printer cannot scan")

    def fax(self, document):
        raise NotImplementedError("This printer cannot fax")


# Чтобы соответствовать ISP, можно разделить Device на несколько интерфейсов,
# каждый из которых будет отвечать за одну функциональность.

class Printer:
    def print(self, document):
        raise NotImplementedError


class Scanner:
    def scan(self, document):
        raise NotImplementedError


class Fax:
    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Print", document)

    def scan(self, document):
        print("Scan", document)

    def fax(self, document):
        print("Fax", document)


class SimplePrinter(Printer):
    def print(self, document):
        print("Print", document)


# Method Resolution Order
