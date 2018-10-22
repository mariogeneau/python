# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from ImageClass import ImageClass
from datetime import date
import tkinter as tk
import tkinter.scrolledtext as tkst
import os
from JsonClass import JsonClass
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.jsonClassObj = JsonClass()
        self.imageObj = ImageClass()
        self.scroll_dates = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#eeeeee", height=10, width=30, padx=10, pady=10)
        self.scroll_new_note = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#eeeeee", height=16, width=30, padx=10, pady=10)
        self.new_note = Button(self.master, text="SAVE NOTE", command=lambda: self.saveNote(), height=2)
        self.load_note = Button(self.master, text="LOAD NOTE", command=lambda: self.loadNote(), height=2)
        self.delete_note = Button(self.master, text="DELETE NOTE", command=lambda: self.deleteNote(), height=2)
        self.load_note_field = Entry(self.master)
        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("MadNotes")
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # logo = self.imageObj.loadImage(os.getcwd() + "/MadNotes/" + "logo.png", 500)
        logo = self.imageObj.loadImage(os.getcwd() + "/" + "logo.png")
        logo.grid(row=0, column=0, pady=10, columnspan=2)
        # ¬¬¬¬
        self.today = str(date.today())
        the_date = Label(self.master, text=f"Today's date : {self.today}")
        the_date.grid(row=1, column=0, columnspan=2)
        # ¬¬¬¬
        title_1 = Label(self.master, text="LIST OF NOTES")
        title_1.grid(row=2, column=0, sticky=E+W, pady=(15, 0))
        # ¬¬¬¬
        title_2 = Label(self.master, text="NOTES")
        title_2.grid(row=2, column=1, sticky=E+W, pady=(15, 0))
        # ¬¬¬¬
        self.scroll_dates.grid(row=3, column=0, padx=(20, 10), sticky=N)
        self.loadJsonAndDisplayDates()
        # ¬¬¬¬
        self.scroll_new_note.grid(row=3, column=1, padx=(10, 20), rowspan=3, sticky=N)
        # ¬¬¬¬
        self.new_note.grid(row=6, column=1, sticky=E+W+N, padx=50, pady=(10, 0))
        # ¬¬¬¬
        title_3 = Label(self.master, text="INSERT DATE TO LOAD OR DELETE")
        title_3.grid(row=4, column=0, sticky=E+W)
        # ¬¬¬¬
        self.load_note_field.grid(row=5, column=0, sticky=E+W+N, padx=50)
        # ¬¬¬¬
        self.load_note.grid(row=6, column=0, sticky=E+W, padx=50, pady=(10, 10))
        # ¬¬¬¬
        self.delete_note.grid(row=7, column=0, sticky=E+W, padx=50, pady=(0, 50))
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadJsonAndDisplayDates(self):
        # self.dict = self.jsonClassObj.loadjsonFile(os.getcwd() + "/" + "notes.json")
        self.dict = self.jsonClassObj.loadJsonFromOnline("http://www.mariogeneau.com/projects/mad_notes/notes.json")
        the_dates = self.getDates(self.dict.keys())
        self.scroll_dates.config(state=NORMAL)
        self.scroll_dates.insert(tk.INSERT, the_dates)
        self.scroll_dates.config(state=DISABLED)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def getDates(self, the_dates):
        str_to_return = ""
        for date in the_dates:
            str_to_return += f"{date}\n"
        return str_to_return
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def saveNote(self):
        self.dict[self.today] = self.scroll_new_note.get('1.0', 'end-1c')
        self.jsonClassObj.saveJsonOnline("http://www.mariogeneau.com/projects/mad_notes/add_to_json.php", self.dict)
        # self.jsonClassObj.saveJsonFile(os.getcwd() + "/MadNotes/" + "notes.json", self.dict)
        # self.jsonClassObj.saveJsonFile(os.getcwd() + "/" + "notes.json", self.dict)
        self.scroll_dates.config(state=NORMAL)
        self.scroll_dates.delete(1.0, END)
        self.scroll_dates.config(state=DISABLED)
        self.scroll_new_note.delete(1.0, END)
        self.loadJsonAndDisplayDates()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadNote(self):
        self.scroll_new_note.delete(1.0, END)
        date_from_field = self.load_note_field.get()
        the_dates = list(self.dict.keys())
        the_notes = list(self.dict.values())
        note_to_display = ""
        for index, date in enumerate(the_dates):
            if the_dates[index] == date_from_field:
                note_to_display += the_notes[index]
                break
        self.scroll_new_note.insert(tk.INSERT, note_to_display)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def deleteNote(self):
        date_from_field = self.load_note_field.get()
        the_dates = list(self.dict.keys())
        for date in the_dates:
            if date_from_field == date:
                del self.dict[date]
                break
        self.scroll_dates.config(state=NORMAL)
        self.scroll_dates.delete(1.0, END)
        self.scroll_dates.config(state=DISABLED)
        self.scroll_new_note.delete(1.0, END)
        self.jsonClassObj.saveJsonOnline("http://www.mariogeneau.com/projects/mad_notes/add_to_json.php", self.dict)
        # self.jsonClassObj.saveJsonFile(os.getcwd() + "/MadNotes/" + "notes.json", self.dict)
        # self.jsonClassObj.saveJsonFile(os.getcwd() + "/" + "notes.json", self.dict)
        self.loadJsonAndDisplayDates()
            
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()









