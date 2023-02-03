class sigleton():
    __instance = None
    @staticmethod
    def get_instance():
        if sigleton.__instance is None:
            sigleton('ram', 20)
        return sigleton.__instance

    def __init__(self, name, age):
        if sigleton.__instance is not None:
            raise "exception"
        else:
            self.name=name
            self.age=age
    def show_data(self):
        print(f'{self.name} {self.age}')

if __name__ == '__main__':
    obj = sigleton('jaya', 22)
    print(obj)
    ll = obj.get_instance()
    print(ll)