import sys
import numpy as np
from PIL import Image


class Canvas:
    """
    Class that creates a canvas of given width, height and color.
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create 3D numpy array of zeroes,then replace zeros with value
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0,0,0] with the user given values for color
        if self.color == "white":
            self.data[:] = [255, 255, 255]
        elif self.color == "black":
            self.data[:] = [0, 0, 0]
        else:
            print("Please choose a valid color.")
            sys.exit()

    def make(self, filepath):
        """Converts the current arry into an image file"""
        img = Image.fromarray(self.data, "RGB")
        img.save(f"{filepath}.png")
