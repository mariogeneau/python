# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
import os
from DateClass import DateClass
import time, threading
from JsonClass import JsonClass
import collections
from tkinter import messagebox
import tkinter as tk
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        # ===
        Frame.__init__(self, master)
        self.master = master
        self.master.config(bg='#4c968c')
        # ===
        self.dateObj = DateClass()
        self.jsonObj = JsonClass()
        # ===
        self.init_window()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        # ===
        self.master.title("MadCalories")
        # ===
        # self.dict = self.jsonObj.loadjsonFile(f'{os.getcwd()}/MadCalories/calories.json')
        self.dict = self.jsonObj.loadjsonFile(f'{os.getcwd()}/calories.json')
        # ===
        self.parseDict()
        # ===
        self.setUpInterface()
        # ===
        self.timer = threading.Timer(1, self.showTime)
        self.timer.start()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # ===
        logo = Label(self.master, text="  ... Mad Calories ...  ")
        logo.config(font=("LeckerliOne-Regular", 32), bg='#4c968c', foreground='white')
        logo.grid(row=0, column=0, padx=50, pady=(20, 5), sticky=W+E+N+S)
        # ===
        self.the_date = self.dateObj.getDate("%Y-%m-%d %H:%M:%S")
        self.date_label = Label(self.master, text=f'Date : {self.the_date} - Goal : 1677', bg='#4c968c', foreground='#7ff4e5')
        self.date_label.grid(row=1, column=0, sticky=W+E+N+S)
        # ===
        Frame1 = Frame(self.master, borderwidth=1, relief="ridge", background="#63bfb3")
        Frame1.grid(row=2, column=0, sticky=W+E+N+S, padx=20, pady=20) 
        # ===
        food = Label(Frame1, text="FOOD : ")
        food.config(bg='#63bfb3')
        food.grid(row=0, column=0, sticky=E, pady=(10, 0), padx=(10, 0))
        # ===
        self.food_entry = Entry(Frame1)
        self.food_entry.config(font=("Optima", 14), justify='left')
        self.food_entry.grid(row=0, column=1, pady=(10, 0), padx=(5, 0))
        # ===
        calories = Label(Frame1, text="CALORIES : ")
        calories.config(bg='#63bfb3')
        calories.grid(row=1, column=0, sticky=E, pady=(10, 0), padx=(10, 0))
        # ===
        self.calories_entry = Entry(Frame1)
        self.calories_entry.config(font=("Optima", 14), justify='left')
        self.calories_entry.grid(row=1, column=1, pady=10, padx=(5, 0))
        # ===
        self.add_button = Button(Frame1, text='ADD', command=lambda: self.addItem(), height=2, width=10)
        self.add_button.grid(row=0, column=2, rowspan=2, sticky=E, padx=(20, 0))
        # ===
        Frame2 = Frame(self.master, borderwidth=1, relief="ridge", background="#63bfb3")
        Frame2.grid(row=3, column=0, sticky=W+E+N+S, padx=20, pady=20)
        # ===
        self.listbox = Listbox(Frame2, width=40, height=5, selectmode=BROWSE)
        for i in range(len(self.no_duplicates_dates)):
            self.listbox.insert(1, f'  {self.no_duplicates_dates[i]} : {self.sum_calories[i]} Calories')
        self.listbox.config(font=("Optima", 16), fg="#000000", selectbackground="#EEEEEE")
        self.listbox.grid(row=0, column=0, sticky=W+E+N+S, padx=20, pady=20)
        self.listbox.bind("<<ListboxSelect>>", self.displaySelection)
        # ===
        self.erase_button = Button(self.master, text='ERASE ALL', command=lambda: self.doEraseAll(), height=2, width=10)
        self.erase_button.grid(row=4, column=0, sticky=W, padx=20, pady=(0, 20))
        # ===
        self.quit_button = Button(self.master, text='QUIT', command=lambda: self.quitApp(), height=2, width=10)
        self.quit_button.grid(row=4, column=0, sticky=E, padx=20, pady=(0, 20))
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def showTime(self):
        # ===
        self.date_label["text"]="Date : " + self.dateObj.getDate("%Y-%m-%d %H:%M:%S") + " - Goal : 1677"
        # ===
        self.timer = threading.Timer(1, self.showTime)
        self.timer.start()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def quitApp(self):
        # ===
        self.timer.cancel()
        # ===
        self.master.quit()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def displaySelection(self, event):
        # ===
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        # ===
        self.displayCaloriesForDayDetails(value.strip())
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def displayCaloriesForDayDetails(self, selection_value):
        # ===
        date = selection_value[:10]
        str_to_display = ""
        # ===
        the_dates = list(self.dict.keys())
        the_values = list(self.dict.values())
        # ===
        the_food = []
        the_calories = []
        short_dates = []
        # ===
        for each_item in the_values:
            the_calories.append(each_item["CALORIES"])
            the_food.append(each_item["FOOD"])
        # ===
        for each_date in the_dates:
            short_dates.append(each_date[:10])
        short_dates = sorted(short_dates)
        # ===
        for a in range(len(short_dates)):
            if date == short_dates[a]:
                str_to_display += f'{the_food[a]} : {the_calories[a]} \n'
        tk.messagebox.showinfo(f'DETAILS : {short_dates[a]}', str_to_display)
        str_to_display = ""
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def parseDict(self):
        # ===
        self.dict = collections.OrderedDict(sorted(self.dict.items()))
        # ===
        self.the_dates = list(self.dict.keys())
        the_values = list(self.dict.values())
        # ===
        self.the_food = []
        self.the_calories = []
        self.short_dates = []
        self.sum_calories = []
        # ===
        for each_item in the_values:
            self.the_calories.append(each_item["CALORIES"])
            self.the_food.append(each_item["FOOD"])
        # ===
        for each_date in self.the_dates:
            self.short_dates.append(each_date[:10])
        self.no_duplicates_dates = list(set(self.short_dates))
        self.no_duplicates_dates = sorted(self.no_duplicates_dates)
        # ===
        for a in range(len(self.no_duplicates_dates)):
            sum_cal = 0
            for b in range(len(self.short_dates)):
                if self.no_duplicates_dates[a] == self.short_dates[b]:
                    sum_cal += int(self.the_calories[b])
            self.sum_calories.append(sum_cal)
            sum_cal = 0
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def addItem(self):
        # ===
        if self.checkEmptyEntry():
            return
        # ===
        date = self.dateObj.getDate("%Y-%m-%d %H:%M:%S")
        food_item = self.food_entry.get()
        calories = self.calories_entry.get()
        # ===
        self.dict[date] = {"FOOD": food_item, "CALORIES": calories}
        # ===
        # self.jsonObj.saveJsonFile(f'{os.getcwd()}/MadCalories/calories.json', self.dict)
        self.jsonObj.saveJsonFile(f'{os.getcwd()}/calories.json', self.dict)
        # ===
        self.parseDict()
        # ===
        self.listbox.delete(0,'end')
        # ===
        for i in range(len(self.no_duplicates_dates)):
            self.listbox.insert(1, f'  {self.no_duplicates_dates[i]} : {self.sum_calories[i]} Calories')
        # ===
        self.eraseEntries()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def checkEmptyEntry(self):
        if self.food_entry.get() == "" or self.calories_entry.get() == "":
            tk.messagebox.showinfo("Message...", "Entries Should Not be Empty...")
            return True
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def eraseEntries(self):
        # ===
        self.food_entry.delete(0,'end')
        self.calories_entry.delete(0,'end')
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def eraseAll(self):
        # ===
        # self.jsonObj.saveJsonFile(f'{os.getcwd()}/MadCalories/calories.json', {})
        self.jsonObj.saveJsonFile(f'{os.getcwd()}/calories.json', {})
        # ===
        self.listbox.delete(0,'end')
        # ===
        self.dict = {}
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
    def doEraseAll(self):
        # ===
        MsgBox = tk.messagebox.askquestion('Erase All','Are you sure you want to erase all?', icon = 'warning')
        # ===
        if MsgBox == 'yes':
            self.eraseAll()
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.resizable(False, False)
app = Window(root)
root.mainloop()
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬









