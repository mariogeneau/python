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
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("Michigan Tax & Tip")
        self.setUpInterface()
        
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/MichiganTaxTip/logo.png', 150, 148)
        logo = self.imageObj.loadImage(f'{os.getcwd()}/logo.png', 150, 148)
        logo.grid(row=0, column=0, pady=20)
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