from abc import ABCMeta, abstractstaticmethod


class Product():
    def __init__(self):
        self.name = None
        self.ram = None
        self.colour = None
        self.rom = None

    def __str__(self):
        return f'this is laptop with these many configuratios {self.name} {self.ram} {self.colour} {self.rom}'


class builderInterface(metaclass=ABCMeta):
    @abstractstaticmethod
    def setColore():
        "set colour"

    @abstractstaticmethod
    def setName():
        "set Name"

    @abstractstaticmethod
    def setRom():
        "set Rom"

    @abstractstaticmethod
    def setRam():
        "set Ram"

    @abstractstaticmethod
    def build():
        "return object"


class builder(builderInterface):
    def __init__(self, product=Product()):
        self.product = product

    def setColore(self, colore):
        self.product.colour = colore
        return self

    def setName(self, name):
        self.product.name = name
        return self

    def setRom(self, rom):
        self.product.rom = rom
        return self

    def setRam(self, ram):
        self.product.ram = ram
        return self

    def build(self):
        return self.product


obj = builder()
obj.setName('Dell').setColore('Red').setRam('2').setRom('200 GB')
print(obj.build())
