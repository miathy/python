def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def emoticon(t,x,y):
    t.pensize(3)
    t.setheading(0)
    jump(t,x,y)
    t.circle(100)
    jump(t,x+35,y+120)
    t.dot(25)
    jump(t,x-35,y+120)
    t.dot(25)
    jump(t,x-60.62, y+65)
    t.setheading(-60)
    t.circle(70,120)