# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from ImageClass import ImageClass
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.v = IntVar()
        self.imageClassObj = ImageClass()
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("Mad.Converter")
        self.pack(fill=BOTH, expand=1)
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        image = self.imageClassObj.loadImage()
        image.pack()
        image.place(x=40, y=10)
        r1 = Radiobutton(self, text="Celsius", value=1, command=self.temperature, variable=self.v)
        r1.pack()
        r1.place(x=40, y=150)
        r2 = Radiobutton(self, text="Fahrenheit", value=2, command=self.temperature, variable=self.v)
        r2.pack()
        r2.place(x=40, y=180)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def temperature(self):
        if self.v.get() == 1:
            print("Celsius")
        else:
            print("Fahrenheit")
    # ¬¬¬¬¬¬¬¬¬¬¬¬

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.geometry("500x700")
app = Window(root)
root.mainloop()
