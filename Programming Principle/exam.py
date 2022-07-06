import turtle
 
# CONSTANTS
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 500
WINDOW_BACKGROUND_COLOR = "orange"
LENGTH_AXIS = 400
TICKS_COLOR = "red"
TICKS_SIZE = 10
TICKS_LABEL_FONT = ("Verdana", 12, "bold")
 
TICKS_Y = 6  # number of ticks on Y axis
TICKS_Y_UNITS = 4  # 4 units between ticks on Y axis (0, 4, 8, ...)
TICKS_Y_LEFT_MARGIN = -40  # spacing between ticks and labels on Y axis
SPACING_Y = LENGTH_AXIS / (TICKS_Y - 1)  # spacing between ticks on Y axis
 
ORIGIN_POINT_X = -200
ORIGIN_POINT_Y = -200
 
# STEPS BREAKDOWN
 
# INPUT NUMBER OF POINTS
n = int(input("Enter number of points: "))
 
if n <= 0:
    exit()
 
spacing_x = (LENGTH_AXIS / n)
 
# SETUP SCREEN, TURTLE
sc = turtle.Screen()
tt = turtle.Turtle()
tt.shape("square")
 
sc.screensize(WINDOW_SIZE_X, WINDOW_SIZE_Y, WINDOW_BACKGROUND_COLOR)
# hide turtle
tt.hideturtle()
tt.speed(0)
 
# DRAW X-Y AXIS with ticks and labels
 
tt.penup()
tt.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)
tt.pendown()
tt.goto(ORIGIN_POINT_X + LENGTH_AXIS, ORIGIN_POINT_Y)
tt.penup()
tt.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)
tt.pendown()
tt.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y + LENGTH_AXIS)
tt.penup()
tt.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)
 
for i in range(TICKS_Y):
    y = ORIGIN_POINT_Y + SPACING_Y * i
    tt.goto(ORIGIN_POINT_X, y)
    tt.dot(TICKS_SIZE, TICKS_COLOR)
    tt.goto(ORIGIN_POINT_X + TICKS_Y_LEFT_MARGIN, y)
    tt.write(i * TICKS_Y_UNITS, font=TICKS_LABEL_FONT)
 
for i in range(n):
    tt.goto(ORIGIN_POINT_X + spacing_x * (i + 1), ORIGIN_POINT_Y)
    tt.dot(TICKS_SIZE, TICKS_COLOR)
 
# INPUT FOR n data points
for i in range(n):
    if i == 1:  # start drawing line between points after the first
        tt.pendown()
 
    dy = int(input("Enter a data point: "))
 
    # calculate spacing from origin
    px = (i + 1) * spacing_x
    py = dy * SPACING_Y / 4
 
    # go to the exact position, stamp a square
    tt.goto(ORIGIN_POINT_X + px, ORIGIN_POINT_Y + py)
    tt.stamp()  # this will leave a square
 
    # calculate where turtle should go to
 
tt.penup()
 
# Exit on click
turtle.exitonclick()