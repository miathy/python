from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#text = Label(root, 
#font = ('Helvetica', 14, 'bold italic'),
#foreground = 'white',
#background = 'black',
#padx=35,
#pady=35,
#text='PEACE & LOVE')
#text.pack(side=LEFT)

photo = Image.open('gg.jpg')
resized = photo.resize((200,200),Image.ANTIALIAS)
#peace = Label(master=root,image = photo,width=1300,height=1800)
photo = ImageTk.PhotoImage(resized)
peace = Label(root,image = photo)
peace.pack()
root.mainloop()