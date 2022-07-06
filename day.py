from tkinter import Tk, Button, Entry, Label, END
from time import strptime,strftime
from tkinter.messagebox import showinfo

def compute():
    global dateEnt
    date = dateEnt.get()
    weekday = strftime('%a', strptime(date, '%b %d'))
    showinfo(message='{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)

root = Tk()
label = Label(root, text = 'Enter day')
label.grid(row=0, column=0)

dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()