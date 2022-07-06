from tkinter import Tk, Button
from time import strftime, localtime, gmtime
#from tkinter.messagebox import showinfo
root = Tk()
def clicked1():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    print('Local time\n'+ time) 


def clicked2():
    time= strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
    print('Greenwich time\n'+time) 
button1 = Button(root, text = 'Local time', command = clicked1)
button1.pack()
button2 = Button(root, text = 'Greenwich time', command = clicked2)
button2.pack()
root.mainloop()
