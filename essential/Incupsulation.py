class MyObject:

    # constructor
    def __init__(self):
        self.__attribute = 0

    # getter
    @property
    def attribute(self):
        return self.__attribute

    # setter
    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__attribute = value


obj = MyObject()
print(obj.attribute)

obj.attribute = 20
print(obj.attribute)
print(obj.attribute)
