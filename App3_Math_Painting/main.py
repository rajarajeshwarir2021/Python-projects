from canvas import Canvas
from shapes import Rectangle, Square

if __name__ == '__main__':
    # Get canvas width and height from the user
    canvas_width = int(input("Enter canvas width: "))
    canvas_height = int(input("Enter canvas height: "))

    # Make dictionary of color codes and prompt for color
    #colors = {"white": (255,255,255), "black": (0,0,0)}
    canvas_color = input("Enter canvas color (white or black): ")

    # Create a canvas with the user data
    canvas = Canvas(canvas_width, canvas_height, canvas_color)

    while True:
        shape_type = input("What do you like to draw? Enter quit to quit. ").lower()

        if shape_type == "rectangle":
            rect_x = int(input("Enter x of the rectangle: "))
            rect_y = int(input("Enter y of the rectangle: "))
            rect_width = int(input("Enter the width of the rectangle: "))
            rect_height = int(input("Enter the height of the rectangle: "))
            rect_cr = int(input("How much red should the rectangle have? "))
            rect_cg = int(input("How much green should the rectangle have? "))
            rect_cb = int(input("How much blue should the rectangle have? "))
            rect_shape = Rectangle(rect_x, rect_y, rect_width, rect_height, [rect_cr, rect_cg, rect_cb])
            rect_shape.draw(canvas)

        elif shape_type == "square":
            sqr_x = int(input("Enter x of the square: "))
            sqr_y = int(input("Enter y of the square: "))
            sqr_side = int(input("Enter the side of the square: "))
            sqr_cr = int(input("How much red should the square have? "))
            sqr_cg = int(input("How much green should the square have? "))
            sqr_cb = int(input("How much blue should the square have? "))
            sqr_shape = Square(sqr_x, sqr_y, sqr_side, [sqr_cr, sqr_cg, sqr_cb])
            sqr_shape.draw(canvas)

        elif shape_type == "quit":
            break

        else:
            print("Please give a valid shape")

    # Save the Canvas
    canvas.make("output")


