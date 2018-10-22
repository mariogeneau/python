# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from ImageClass import ImageClass
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
        self.imageClassObj = ImageClass()
        logo = self.imageClassObj.loadImage(os.getcwd() + "/" + "logo.png")
        logo.grid(row=0, column=0, pady=(15, 10))
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadImage(self, path_to_image, the_width):
        image = Image.open(path_to_image)
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo, width=the_width)
        label.image = photo
        return label
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def messages(self, the_message):
        messagebox.showinfo("Message...", the_message)
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()