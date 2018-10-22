from tkinter import *

top = Tk()

b1 = Button(top, text="one", padx=10)
b2 = Button(top, text="two", padx=10)
b3 = Button(top, text="three", padx=10)
b4 = Button(top, text="four", padx=10)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)

top.mainloop()