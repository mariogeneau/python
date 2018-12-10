# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import messagebox
import tkinter as tk
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class MessageBoxClass:
    # ¬¬¬¬¬¬¬¬¬
    def __init__(self):
        super().__init__()
    # ¬¬¬¬¬¬¬¬¬
    def alert(self, title, message):
        tk.messagebox.showinfo(title, message)
    # ¬¬¬¬¬¬¬¬¬
    def dialog(self, title, message):
        self.show_dialog(messagebox.askokcancel, title, message)
    # ¬¬¬¬¬¬¬¬¬
    def show_dialog(self, func, *args, **kwargs):
        root = tk.Tk()
        root.withdraw()
        result = []
        def show_dialog():
            result.append(func(*args, **kwargs))
            root.destroy()
        root.after_idle(show_dialog)
        root.mainloop()
        root.quit()
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def question(self, title, question):
        tk.messagebox.askquestion(title, question, icon='warning')

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# Version 1

# from MessageBoxClass import MessageBoxClass
# self.messageBoxObj = MessageBoxClass()
# self.messageBoxObj.alert(title, message)
# self.messageBoxObj.dialog(title, message)
# self.messageBoxObj.question(title, question)

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬