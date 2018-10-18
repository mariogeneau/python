# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as tkst
import os
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.field_file_name = Entry(self, bg="yellow", width=40)
        self.scroll = tkst.ScrolledText(master=self, wrap=tk.WORD, width=40, height=5, bg="yellow")
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("CREATE TEXT FILE")
        self.pack(fill=BOTH, expand=1)
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def readFile(self, event):
        self.scroll.delete(1.0, END)
        with open(os.getcwd() + "/" + self.field_file_name.get() + ".txt", "r") as f:
            self.scroll.insert(tk.INSERT, f.read())
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        label_1 = Label(self, text="File Name Without Extension :")
        label_1.pack(side=TOP, pady=10)
        # ---
        self.field_file_name.pack(side=TOP)
        # ---
        button_create_file = Button(self, text="Create or Save File", highlightbackground ="#8EF0F7", pady=10, padx=10, relief=FLAT)
        button_create_file.pack(side=TOP, pady=10)
        button_create_file.bind('<Button-1>', self.createFile)
        # ---
        button_load_file = Button(self, text="Load File", highlightbackground ="#8EF0F7", pady=10, padx=10, relief=FLAT)
        button_load_file.pack(side=TOP)
        button_load_file.bind('<Button-1>', self.readFile)
        # ---
        self.scroll.pack(side=BOTTOM, fill=BOTH, expand=True, padx=20, pady=10)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def createFile(self, event):
        text_file = open(self.field_file_name.get() + ".txt", "w")
        text_file.write(self.scroll.get('1.0', 'end-1c'))
        text_file.close()
        self.messages("Created or Saved Succesfully...")
        # self.eraseFields()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def messages(self, the_message):
        messagebox.showinfo("Message...", the_message)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def eraseFields(self):
        # self.field_file_name.delete(0, END)
        # self.scroll.insert(tk.INSERT, "")
        pass
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()