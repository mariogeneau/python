# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from ImageClass import ImageClass
import os
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.imageObj = ImageClass()
        self.books = {"Java": 12.99, "Python": 14.99}
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("Tables")
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        l = Listbox(self.master, width=20, height=5, selectmode=BROWSE)
        for each_book in self.books:
            l.insert(1, f'  {each_book} - ${self.books[each_book]}')
        l.config(font=("Gill Sans Light", 16), fg="#000000", selectbackground="#EEEEEE")
        l.grid(row=0, column=0, sticky=W, padx=20, pady=20)
        l.bind("<<ListboxSelect>>", self.displaySelection)
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/MichiganTaxTip/logo.png', 150, 148)
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/logo.png', 150, 148)
        # logo.grid(row=0, column=0, pady=20)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def displaySelection(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        print(value.strip())
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# Needs the ImageClass

# To compile as an app : python3 MichiganTaxTip/setup.py py2app

# For Mac : Include the images in the package

# setup.py looks like this :
# from setuptools import setup
#
# APP = ['TeamJenMario/TeamJenMario.py']
# DATA_FILES = []
# OPTIONS = {
#     'argv_emulation': False,
#     'packages': ['PIL']
#     }
# 
# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬