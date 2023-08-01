import turtle
from math import sqrt, pow


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_point_in_rectangle(self, rectangle):
        if rectangle.point_1.x < self.x < rectangle.point_2.x and rectangle.point_1.y < self.y < rectangle.point_2.y:
            return True
        else:
            return False

    def distance(self, point):
        dist = sqrt(pow((self.x - point.x), 2) - pow((self.y - point.y), 2))
        return dist

    def __str__(self):
        return f"The co-ordinates are x:{self.x} and y:{self.y}"


class GUIPoint(Point):

    def draw(self, canvas, size=5, color="red"):
        # Go to the point
        canvas.penup()
        canvas.goto(25, 50)

        # Draw the point
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, point_1, upper_right):
        self.point_1 = point_1
        self.point_2 = upper_right

    def area(self):
        width = self.point_2.x - self.point_1.x
        height = self.point_2.y - self.point_1.y

        return width * height


class GUIRectangle(Rectangle):

    def draw(self, canvas):

        # Go to a certain coordinate
        canvas.penup()
        canvas.goto(self.point_1.x, self.point_1.y)

        # Draw the rectangle
        canvas.pendown()
        for i in range(2):
            canvas.forward(self.point_2.x - self.point_1.x)
            canvas.left(90)
            canvas.forward(self.point_2.y - self.point_1.y)
            canvas.left(90)