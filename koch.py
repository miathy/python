def koch(n):
    if n == 0:
        return 'F'
    tmp = koch(n-1)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp

from turtle import Screen, Turtle
def drawKoch(n):
    s=Screen()
    t=Turtle()
    directions= koch(n)
    for move in directions:
        if move =='F':
            t.forward(300/3**n) 
        if move == 'L':
            t.lt(60)
        if move == 'R':
            t.rt(120)

    s.exitonclick()

drawKoch(3)