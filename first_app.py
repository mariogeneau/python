# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.field_file_name = Entry(self, bg="yellow", width=40)
        self.field_file_content = Entry(self, bg="yellow", width=40)
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("CREATE TEXT FILE")
        self.pack(fill=BOTH, expand=1)
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        label_1 = Label(self, text="File Name Without Extension :")
        label_1.place(x=10, y=20)
        # ---
        self.field_file_name.place(x=10, y=50)
        # ---
        label_2 = Label(self, text="File Content :")
        label_2.place(x=10, y=100)
        # ---
        self.field_file_content.place(x=10, y=130)
        # ---
        button_create_file = Button(self, text="Create File", highlightbackground ="#8EF0F7", pady=10, padx=10, relief=FLAT)
        button_create_file.place(x=10, y=180)
        button_create_file.bind('<Button-1>', self.createFile)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def createFile(self, event):
        text_file = open(self.field_file_name.get() + ".txt", "w")
        text_file.write(self.field_file_content.get())
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