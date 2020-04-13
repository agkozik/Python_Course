class Figure:
    side = 0.0

    def __init__(self, side):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)


class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)


square = Square(5)
square.draw()

tri = Triangle(8)
tri.draw()
