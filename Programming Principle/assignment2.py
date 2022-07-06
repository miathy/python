
import turtle

# CONSTANTS
ORIGIN_POINT_X = -200
ORIGIN_POINT_Y = -200
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 500
WINDOW_BACKGROUND_COLOR = "orange"
LENGTH_AXIS = 400
TICKS_COLOR = "red"
TICKS_SIZE = 5
TICKS_LABEL_FONT = ("Verdana", 12, "bold")
 
TICKS_Y = 6  # number of ticks on Y axis
TICKS_Y_UNITS = 4  # 4 units between ticks on Y axis (0, 4, 8, ...)
TICKS_Y_LEFT_MARGIN = -40  # spacing between ticks and labels on Y axis
SPACING_Y = LENGTH_AXIS / (TICKS_Y - 1)


# INPUT NUMBER OF POINTS 

n = int(turtle.numinput('Input Needded', 'How many data points? ', minval=0, maxval=20))

print('Enter the valid input:')
spacing_x = (LENGTH_AXIS / n)

# DRAW X-Y AXIS with ticks and labels methods

def draw_x():
    turtle.penup()
    turtle.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)
    turtle.pendown()
    turtle.goto(ORIGIN_POINT_X + LENGTH_AXIS+50, ORIGIN_POINT_Y)
    turtle.stamp()
    turtle.penup()
    
def draw_y():
    turtle.penup()
    turtle.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)
    turtle.pendown() 
    turtle.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y+ LENGTH_AXIS+50)
    turtle.left(90)
    turtle.stamp()
    turtle.penup()
    turtle.goto(ORIGIN_POINT_X, ORIGIN_POINT_Y)

def y_marker():
    for i in range(TICKS_Y):
        turtle.penup()
        y = ORIGIN_POINT_Y + SPACING_Y*i
        turtle.goto(ORIGIN_POINT_X, y)
        turtle.pendown()
        turtle.dot(TICKS_SIZE, TICKS_COLOR)
        turtle.penup()
        turtle.goto(ORIGIN_POINT_X+TICKS_Y_LEFT_MARGIN, y)
        turtle.pendown()
        turtle.write(i*TICKS_Y_UNITS, font=TICKS_LABEL_FONT)

def x_marker():
    for i in range(n):
        turtle.penup()
        x = ORIGIN_POINT_X + spacing_x * (i+1)
        turtle.goto(x, ORIGIN_POINT_Y)
        turtle.pendown()
        turtle.dot(TICKS_SIZE, TICKS_COLOR)
        turtle.penup()
        turtle.goto(x,ORIGIN_POINT_Y+TICKS_Y_LEFT_MARGIN)
        turtle.write(i+1, font = TICKS_LABEL_FONT)


def draw_lines():
    for i in range(n):
        dy = int(turtle.numinput('Input Needed', 'Next points:?'))    
        # calculate spacing from origin
        py = dy * (SPACING_Y/4)
        px = (i+1) * spacing_x
         # go to the exact position, stamp a square
        turtle.goto(ORIGIN_POINT_X + px, ORIGIN_POINT_Y + py)
        turtle.pendown()
        turtle.shape('square')
        turtle.stamp() #this will leave a square
           

def main():
    turtle.hideturtle()
    turtle.speed(0)
    # turtle.shape('square')
    turtle.screensize(WINDOW_SIZE_X, WINDOW_SIZE_Y, WINDOW_BACKGROUND_COLOR)
    draw_x()
    draw_y()
    y_marker()
    x_marker()
    draw_lines()

if __name__ == '__main__':
    main()
    turtle.exitonclick()
