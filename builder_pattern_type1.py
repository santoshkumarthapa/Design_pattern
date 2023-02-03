# Builder Design pattern is creational design pattern
# In this design pattern we are creating complex object with help of director
# We are not creating complex object in one go rather outsourcing the object creation 
# Example there could many laptop product out there but there than crating each laptop by its own class
# create a setter class to place confifuration 

class Laptop():
    def __init__(self):
        self.name = None
        self.ram = None
        self.colour = None
        self.rom = None
    def __str__(self):
        return f'this is laptop with these many configuratios {self.name} {self.ram} {self.colour} {self.rom}'
    
class builder():
    def __init__(self, laptop=Laptop()):
        self.laptop = laptop
        
    def setName(self, name):
        self.laptop.name = name
        return self   
    
    def setRam(self, ram):
        self.laptop.ram = ram
        return self

    def setColour(self, colour):
        self.laptop.colour=colour
        return self

    def setRom(self,rom):
        self.laptop.rom = rom
        return self

    def build(self):
        return self.laptop


if __name__ == '__main__':
    obj = builder()
    obj.setName('Dell').setRam(2).setColour('red').setRom(500)
    print(obj.build())
    ll = obj.setName('Lenovo').setRam(4).setColour('Metalic gray').setRom('1 Terabyte').build()
    print(ll)


    obj2 = builder(ll)
    obj2.setRam(8)
    print(obj2.build())