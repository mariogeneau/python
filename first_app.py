# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.scrolledtext as tkst
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.field_file_name = Entry(self, bg="yellow", width=40)
        self.field_file_content = Entry(self, bg="yellow", width=40)
        self.scroll = tkst.ScrolledText(master=self, wrap=tk.WORD, width=40, height=5, bg="yellow")
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("CREATE TEXT FILE")
        self.pack(fill=BOTH, expand=1)
        self.setUpInterface()
        self.readFile()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def readFile(self):
        with open("mario.txt", "r") as f:
            self.scroll.insert(tk.INSERT, f.read())
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        label_1 = Label(self, text="File Name Without Extension :")
        label_1.pack(side=TOP, pady=10)
        # ---
        self.field_file_name.pack(side=TOP)
        # ---
        label_2 = Label(self, text="File Content :")
        label_2.pack(side=TOP, pady=10)
        # ---
        self.field_file_content.pack(side=TOP)
        # ---
        button_create_file = Button(self, text="Create File", highlightbackground ="#8EF0F7", pady=10, padx=10, relief=FLAT)
        button_create_file.pack(side=TOP, pady=10)
        button_create_file.bind('<Button-1>', self.createFile)
        # ---
        self.scroll.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def createFile(self, event):
        text_file = open(self.field_file_name.get() + ".txt", "w")
        self.scroll.insert(tk.INSERT, self.field_file_content.get())
        text_file.write(self.scroll.get('1.0', 'end-1c'))
        text_file.close()
        self.messages("File Creation Successful")
        self.eraseFields()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def messages(self, the_message):
        messagebox.showinfo("Message...", the_message)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def eraseFields(self):
        self.field_file_name.delete(0, END)
        self.field_file_content.delete(0, END)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()