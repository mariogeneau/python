# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from ImageClass import ImageClass
import os
import tkinter as tk
import tkinter.scrolledtext as tkst
from JsonClass import JsonClass
import time
import collections
import datetime
import socket
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
        self.checkInternetAvailability()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def checkInternetAvailability(self):
        if self.is_connected():
            self.loadJsonData()
        else:
            self.show_dialog(messagebox.askokcancel, "Message...", "No Internet Connectivity...")
    # ¬¬¬¬¬¬¬¬¬¬¬¬
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
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def is_connected(self):
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # ===
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/TeamJenMario/logo.png', 450, 84)
        logo = self.imageObj.loadImage(f'{os.getcwd()}/logo.png', 450, 84)
        logo.grid(row=0, column=0, pady=20)
        # ===
        message_to_send_label = Label(self.master, text='MESSAGE TO SEND')
        message_to_send_label.config(font=("Courier-Bold", 16))
        message_to_send_label.grid(row=1, column=0, sticky=W, padx=(25, 0))
        # ===
        self.scroll_message_to_send = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#FF265D", height=12, width=50, padx=10, pady=10)
        self.scroll_message_to_send.config(font=("Courier", 16), fg="White")
        self.scroll_message_to_send.grid(row=2, column=0, padx=25)
        # ===
        self.send_button = Button(self.master, text="SEND", command=lambda: self.sendButton(), height=2, width=8)
        self.send_button.config(font=("Courier", 16))
        self.send_button.grid(row=3, column=0, sticky=E, padx=(0, 25), pady=10)
        # ===
        timeline_label = Label(self.master, text='TIMELINE')
        timeline_label.config(font=("Courier-Bold", 16))
        timeline_label.grid(row=4, column=0, sticky=W, padx=(25, 0))
        # ===
        self.scroll_timeline = tkst.ScrolledText(self.master, wrap=tk.WORD, bg="#FF265D", height=18, width=50, padx=10, pady=10)
        self.scroll_timeline.config(font=("Courier", 16), fg="White")
        self.scroll_timeline.grid(row=5, column=0)
        # ===
        self.reset_button = Button(self.master, text='RESET', command=lambda: self.resetAlert(), height=2, width=8)
        self.reset_button.config(font=("Courier", 16))
        self.reset_button.grid(row=6, column=0, sticky=W, padx=(25, 0), pady=(10, 30))
        # ===
        self.update_button = Button(self.master, text='UPDATE', command=lambda: self.updateButton(), height=2, width=8)
        self.update_button.config(font=("Courier", 16))
        self.update_button.grid(row=6, column=0, sticky=E, padx=(0, 25), pady=(10, 30))
        # ===
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def sendButton(self):
        if self.scroll_message_to_send.get("1.0", 'end-1c') == "":
            return
        self.loadJsonData()
        self.scroll_timeline.delete(1.0, END)
        localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dict[localtime] = f"MAD - {self.scroll_message_to_send.get('1.0', 'end-1c')}"
        self.jsonObj.saveJsonOnline("http://www.mariogeneau.com/projects/teamjenmario/add_to_json.php", self.dict)
        # self.jsonObj.saveJsonFile(f'{os.getcwd()}/TeamJenMario/timeline.json', self.dict);
        self.loadJsonData()
        self.scroll_message_to_send.delete(1.0, END)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def updateButton(self):
        self.loadJsonData()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def resetButton(self):
        self.scroll_timeline.delete(1.0, END)
        self.dict = {"©TeamJenMario": "©TeamJenMario"}
        self.jsonObj.saveJsonOnline("http://www.mariogeneau.com/projects/teamjenmario/add_to_json.php", self.dict)
        self.scroll_message_to_send.delete(1.0, END)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def loadJsonData(self):
        self.scroll_timeline.delete(1.0, END)
        self.dict = self.jsonObj.loadJsonFromOnline("http://www.mariogeneau.com/projects/teamjenmario/timeline.json")
        # self.dict = self.jsonObj.loadjsonFile(f'{os.getcwd()}/TeamJenMario/timeline.json')
        timeline_data = self.createTimeline()
        self.scroll_timeline.insert(tk.INSERT, timeline_data)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def createTimeline(self):
        self.dict = collections.OrderedDict(sorted(self.dict.items()))
        the_dates = list(self.dict.keys())
        the_messages = list(self.dict.values())
        for date in the_dates:
            if date == "©TeamJenMario":
                del self.dict["©TeamJenMario"]
                break
        the_dates = list(self.dict.keys())
        the_messages = list(self.dict.values())
        the_dates.reverse()
        the_messages.reverse()
        timeline_str_to_return = ""
        for i, date in enumerate(the_dates):
            timeline_str_to_return += f'{date} : \n\n'
            timeline_str_to_return += f'{the_messages[i]}\n\n--------------------------------------\n'
        return timeline_str_to_return
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def resetAlert(self):
        resetBox = tk.messagebox.askquestion('Message...','Really want to reset everything?',icon = 'warning')
        if resetBox == 'yes':
           self.resetButton()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
app = Window(root)
root.mainloop()
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬










