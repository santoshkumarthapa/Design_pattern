def singleton(class_instance):
    instance={}
    def get_instace(*arg, **kwarg):
        if class_instance not in instance:
            instance[class_instance] = class_instance(*arg, **kwarg)
        return instance[class_instance]
    return get_instace
@singleton
class TDConnectios:
    def __init__(self):
        print("Teradata connection")

if __name__ == "__main__":
    obj1 = TDConnectios()
    obj2 = TDConnectios()
    print(obj1,obj2)
    print(obj1==obj2)