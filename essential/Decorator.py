class MyObject:
    class_attribute = 8

    def __init__(self):
        self.data_attribute = 42

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)


# -------------------------------------------------------

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle ({})".format(self.radius)

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    circle = Circle(20)
    print(circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)


if __name__ == "__main__":
    MyObject.static_method()
    obj = MyObject()
    obj.instance_method()
    obj.static_method()
    main()


# ------------------------------------------------------
def decorator(fn):
    def decorated_fn(*args, **kwargs):
        print('Enter decorated function')
        fn(*args, **kwargs)
        print('End of decorated function')

    return decorated_fn

@decorator # аннотация заменяет вот такой код: print_hello = decorator(print_hello)

def print_hello():
    print('Hello')

print_hello()

# ---------------------------------------------------------
def make_decorator(string):
    def decorator(fn):
        def decorated_fn(*args, **kwargs):
            print(string)
            fn(*args, **kwargs)
        return decorated_fn
    return decorator

@make_decorator('First decorator')
@make_decorator('Second decorator')
def print_hello():
    print('Hello')


print_hello()