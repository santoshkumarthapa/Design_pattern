# iterator is function that give us feature to ietar over to object
# to implement interator class we need to have __iter__ and __next__ function in custome class

class custom_itrator():
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n**2
            self.n+=1
            return result
        else:
            raise('stop inerating ')
    
obj = custom_itrator(3)

i = iter(obj)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))