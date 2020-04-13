class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def show_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run: ', self.can_run)
        print('Can fly: ', self.can_fly)
        print('-----------------------')


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegus(Horse, Bird):
    pass


animal = Animal()
horse = Horse()
bird = Bird()
pegas = Pegus()

animal.show_abilities()
horse.show_abilities()
bird.show_abilities()
pegas.show_abilities()

print(isinstance(pegas, Animal))
print(isinstance(pegas, Horse))



# class Base:
#     def method(self):
#         print("Base class method: ", type(self).__name__, 'instance')
#
# class Child(Base):
#     def method(self):
#         super().method()
#         print("Child class method: ", type(self).__name__, 'instance')
#
#
# base_instance = Base()
# base_instance.method()
#
# child_instance = Child()
# child_instance.method()