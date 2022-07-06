from turtle import Screen, Turtle
def koch(n):
    if n == 0:
        return 'F'
    tmp = koch(n-1)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp
def drawSnowFlake(n):
    s=Screen()
    t=Turtle()
    directions = koch(n)
    for i in range(3):
        for move in directions:
            if move =='F':
                t.fd(300/3**n)
            if move =='L':
                t.lt(60)
            if move =='R':
                t.rt(120)
        t.rt(120)
    t.speed()
    s.exitonclick()

drawSnowFlake(3)
