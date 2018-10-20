from tkinter import *

root = Tk()
l = Label(text="Hello world", font=("Helvetica", 20))
l.pack()
b = Button(text="Kill Me", command=sys.exit)
b.pack()
root.mainloop()
