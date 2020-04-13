# class Base(object):
#     def method(self):
#         print("Callable Method class: ", __class__.__name__)
#         print("Instance class: ", type(self).__name__)
#
#
# class Child(Base):
#     pass
#
# if __name__ == '__main__':
#     base_instance = Base()
#     base_instance.method()
#
#     child = Child()
#     child.method()
# ------------------------------------------------------------------
class A:
    def method(self):
        print("A class method was called")


class B(A):
    pass


class C(A):
    def method(self):
        print("C class method was called ")


class D(B, C):
    pass


obj = D()
obj.method()
# посмотреть порядок вызова в иерархии наследования
print(D.mro())
