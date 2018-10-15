# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
# import tkinter as tk
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.aLabel = Label(self, text="Hello World!")
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        aField = Entry(self, text="File Name")
        aField.place(x=10, y=100)
        aButton = Button(self, text="Click me!")
        aButton.place(x=10, y=10)
        aButton.bind('<Button-1>', self.display)
        self.aLabel.place(x=10, y=50)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def display(self, event):
        # self.configure(background='yellow')
        # w = tk.Label(self, text="Hello World!")
        # w.pack()
        # import sys; sys.exit()
        self.aLabel['text'] = 'This is cool!'
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()
