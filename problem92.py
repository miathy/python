from calendar import monthrange
from tkinter import Tk, Label
root = Tk()


def cal(year, month):
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i in range(7):
        label = Label(root, text=days[i])
        label.grid(row=0,column=i)

    weekday,numDays = monthrange(year, month)
    week = 1
    for i in range(1, numDays+1):
        label = Label(root, text = str(i))
        label.grid(row=week, column=weekday)
        weekday += 1
        if weekday>6:
            week +=1
            weekday = 0
    root.mainloop()

cal(2012,2)