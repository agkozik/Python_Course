class Base:
    name = "Sasha"
    age = 36


    def print_hello(self):
        print("Hello, from Base")


class Child(Base):
    def print_hello(self):
        print("Hello, from Child")

    def ask_some(self):
        print("How are you?")


child1 = Child()
child1.print_hello()
child1.ask_some()
base1 = Base()
print(base1.__getattribute__("name"))
print(base1.__getattribute__("age"))


