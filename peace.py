
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
photo = Image.open('DSC_0273.jpeg')
resized = photo.resize((225,170),Image.ANTIALIAS)
#peace = Label(master=root,image = photo,width=1300,height=1800)
photo = ImageTk.PhotoImage(resized)
peace = Label(root,image = photo)
peace.pack(pady=20)
root.mainloop()
