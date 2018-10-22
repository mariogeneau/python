# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from PIL import Image, ImageTk
import os
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("MAD CALORIES")
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        image = Image.open(os.getcwd() + "/MadCalories/" + "logo.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=0, pady=(15, 10))
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadImage(self, path_to_image, the_width):
        image = Image.open(path_to_image)
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo, width=the_width)
        label.image = photo
        return label
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()