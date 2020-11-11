import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, length=0, sides=0):
        self.sides = sides
        self.length = length

    def show(self):
        for i in range(self.sides):
            t.forward(self.length)
            t.right(90)


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")


class square(polygon):
    def show(self):
        for i in range(4):
            t.forward(self.length)
            t.right(90)


class pentagon(polygon):
    def show(self):
        for i in range(5):
            t.forward(self.length)
            t.right(72)


class hexagon(polygon):
    def show(self):
        for i in range(6):
            t.forward(self.length)
            t.right(60)


class octagon(polygon):
    def show(self):
        for i in range(8):
            t.forward(self.length)
            t.right(45)


class triangle(polygon):
    def show(self):
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)


hex1 = triangle(100)
hex1.info()
hex1.show()
