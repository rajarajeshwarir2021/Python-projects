import numpy as np
from PIL import Image


class Rectangle:
    """
    Class that crates a rectangle from given co-ordinates with the give width, height and color.
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draws itself into the the canvas"""
        # Change a slice of the array with new values
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    """
    Class that crates a square from given co-ordinates with the give width, height and color.
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the the canvas"""
        # Change a slice of the array with new values
        canvas.data[self.x:self.x + self.side, self.y: self.y + self.side] = self.color