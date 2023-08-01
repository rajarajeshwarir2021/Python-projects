import turtle
from random import randint
from backend import Point, GUIPoint, GUIRectangle

if __name__ == '__main__':

    # Create rectangle object
    gui_rectangle = GUIRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

    # Print rectangle co-ordinates
    print("Rectangle Coordinates: ", gui_rectangle.point_1.x, ",", gui_rectangle.point_1.y, "and",
          gui_rectangle.point_2.x, ",", gui_rectangle.point_2.y)

    # Get point and area from user
    user_point = GUIPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
    user_area = float(input("Guess rectangle area: "))

    # Print out the game result
    print("Your point was inside rectangle: ", user_point.is_point_in_rectangle(gui_rectangle))
    print("Your area was off by: ", gui_rectangle.area() - user_area)

    # Draw the result
    my_turtle = turtle.Turtle()
    gui_rectangle.draw(canvas=my_turtle)
    user_point.draw(canvas=my_turtle)
    turtle.done()
