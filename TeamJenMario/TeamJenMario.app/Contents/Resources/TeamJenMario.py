# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from ImageClass import ImageClass
import os
import tkinter as tk
import tkinter.scrolledtext as tkst
from JsonClass import JsonClass
import time
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        # ===
        Frame.__init__(self, master)
        self.master = master
        # ===
        self.imageObj = ImageClass()
        # ===
        self.init_window()
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("TeamJenMario")
        self.jsonObj = JsonClass()
        self.setUpInterface()
        self.loadJsonData()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # ===
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/TeamJenMario/logo.png', 582, 109)
        logo = self.imageObj.loadImage(f'{os.getcwd()}/logo.png', 582, 109)
        logo.grid(row=0, column=0, pady=(10, 0), columnspan=4)
        # ===
        message_to_send_label = Label(self.master, text='MESSAGE TO SEND')
        message_to_send_label.config(font=("Courier-Bold", 21))
        message_to_send_label.grid(row=1, column=0, columnspan=4, sticky=W, padx=100, pady=(30, 0))
        # ===
        self.scroll_message_to_send = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#c61f5d", height=5, width=80, padx=10, pady=10)
        self.scroll_message_to_send.config(font=("Courier", 21), fg="White")
        self.scroll_message_to_send.grid(row=2, column=0, columnspan=4, padx=100, pady=(5, 0))
        # ===
        self.send_button = Button(self.master, text="SEND", command=lambda: self.sendButton(), height=2, width=8)
        self.send_button.config(font=("Courier-Bold", 21))
        self.send_button.grid(row=3, column=0, columnspan=4, sticky=E, padx=100, pady=(10, 0))
        # ===
        timeline_label = Label(self.master, text='TIMELINE')
        timeline_label.config(font=("Courier-Bold", 21))
        timeline_label.grid(row=4, column=0, columnspan=4, sticky=W, padx=100, pady=(30, 0))
        # ===
        self.scroll_timeline = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#c61f5d", height=15, width=80, padx=10, pady=10)
        self.scroll_timeline.config(font=("Courier", 21), fg="White")
        self.scroll_timeline.grid(row=5, column=0, columnspan=4, padx=100, pady=(5, 0))
        # ===
        self.update_button = Button(self.master, text='UPDATE', command=lambda: self.updateButton(), height=2, width=8)
        self.update_button.config(font=("Courier-Bold", 21))
        self.update_button.grid(row=6, column=0, columnspan=4, sticky=E, padx=100, pady=(10, 50))
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def sendButton(self):
        self.scroll_timeline.delete(1.0, END)
        localtime = time.asctime( time.localtime(time.time()))
        self.dict['JEN - ' + localtime] = self.scroll_message_to_send.get('1.0', 'end-1c')
        self.jsonObj.saveJsonOnline("http://www.mariogeneau.com/projects/teamjenmario/add_to_json.php", self.dict)
        self.loadJsonData()
        self.scroll_message_to_send.delete(1.0, END)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def updateButton(self):
        self.loadJsonData()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadJsonData(self):
        self.scroll_timeline.delete(1.0, END)
        self.dict = self.jsonObj.loadJsonFromOnline("http://www.mariogeneau.com/projects/teamjenmario/timeline.json")
        timeline_data = self.createTimeline(self.dict)
        self.scroll_timeline.insert(tk.INSERT, timeline_data)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def createTimeline(self, the_dict):
        the_dates = list(the_dict.keys())
        the_dates.reverse()
        the_messages = list(the_dict.values())
        the_messages.reverse()
        timeline_str_to_return = ""
        for i, date in enumerate(the_dates):
            timeline_str_to_return += f'{date} : \n\n'
            timeline_str_to_return += f'{the_messages[i]}\n\n------------------------------------------------------------\n'
        return timeline_str_to_return
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def getDates(self, the_dates):
        str_to_return = ""
        for date in the_dates:
            str_to_return += f"{date}\n"
        return str_to_return
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def getMessages(self, the_messages):
        str_to_return = ""
        for message in the_messages:
            str_to_return += f"{message}\n"
        return str_to_return
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()










