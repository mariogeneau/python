# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from tkinter import *
from tkinter import messagebox
from ImageClass import ImageClass
import os
import tkinter as tk
from Brain import Brain
import pickle
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Window(Frame):
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.imageObj = ImageClass()
        result_field = Entry(self.master)
        self.brain = Brain()
        self.amount = ""
        self.tax = ""
        self.tip = ""

        # tax = open('MichiganTaxTip/tax.pckl', 'rb')
        # self.tax_ratio = float(pickle.load(tax))
        # tax.close()
        # 
        # tip = open('MichiganTaxTip/tip.pckl', 'rb')
        # self.tip_ratio = float(pickle.load(tip))
        # tip.close()

        tax = open(f'{os.getcwd()}/tax.pckl', 'rb')
        self.tax_ratio = float(pickle.load(tax))
        tax.close()

        tip = open(f'{os.getcwd()}/tip.pckl', 'rb')
        self.tip_ratio = float(pickle.load(tip))
        tip.close()

        self.init_window()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def init_window(self):
        self.master.title("Michigan Tax & Tip")
        self.setUpInterface()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def setUpInterface(self):
        # logo = self.imageObj.loadImage(f'{os.getcwd()}/MichiganTaxTip/logo.png', 150, 148)
        logo = self.imageObj.loadImage(f'{os.getcwd()}/logo.png', 150, 148)
        logo.place(relx=0.5, y=90, anchor=CENTER)
        # ---
        amount_label = Label(self.master, text='AMOUNT : ')
        amount_label.config(font=("Futura", 14))
        amount_label.place(relx=0.35, y=210, anchor=E)
        # ---
        self.amount_field = Entry(self.master)
        self.amount_field.config(font=("Optima", 14), justify='center')
        self.amount_field.place(relx=0.35, y=210, width=100, anchor=W)
        self.amount_field.bind("<Key>", self.amountFieldEvent)
        # ---
        taxes_label = Label(self.master, text='WITH TAX : ')
        taxes_label.config(font=("Futura", 14))
        taxes_label.place(relx=0.35, y=250, anchor=E)
        # ---
        self.taxes_field = Entry(self.master)
        self.taxes_field.config(font=("Optima", 14), justify='center')
        self.taxes_field.place(relx=0.35, y=250, width=100, anchor=W)
        self.taxes_field.insert(tk.INSERT, str(self.tax_ratio))
        self.taxes_field.bind("<Key>", self.changeTaxRatio)
        # ---
        self.taxes_result = Label(self.master, text='$0.00 - $0.00')
        self.taxes_result.config(font=("Optima", 14))
        self.taxes_result.place(relx=0.60, y=250, anchor=W)
        # ---
        tip_label = Label(self.master, text='WITH TIP : ')
        tip_label.config(font=("Futura", 14))
        tip_label.place(relx=0.35, y=290, anchor=E)
        # ---
        self.tip_field = Entry(self.master)
        self.tip_field.config(font=("Optima", 14), justify='center')
        self.tip_field.place(relx=0.35, y=290, width=100, anchor=W)
        self.tip_field.insert(tk.INSERT, str(self.tip_ratio))
        self.tip_field.bind("<Key>", self.changeTipRatio)
        # ---
        self.tip_result = Label(self.master, text='$0.00 - $0.00')
        self.tip_result.config(font=("Optima", 14))
        self.tip_result.place(relx=0.60, y=290, anchor=W)
        # ---
        result_label = Label(self.master, text='RESULT : ')
        result_label.config(font=("Futura", 14))
        result_label.place(relx=0.35, y=330, anchor=E)
        # ---
        self.result_field = Entry(self.master)
        self.result_field.config(background="#f7f6d2", font=("Optima", 14, "bold"), justify='center', fg='#ff0000')
        self.result_field.place(relx=0.35, y=330, width=100, anchor=W)
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def amountFieldEvent(self, evt):
        if evt.char == '\x7f':
            self.result_field.delete(0, END)
            self.amount_field.delete(0, END)
            self.taxes_result["text"] = "$0.00 - $0.00"
            self.tip_result["text"] = "$0.00 - $0.00"
            self.amount = ""
        else:
            self.amount += evt.char
            tax = "$" + '{:.2f}'.format(round(self.brain.getTaxes(self.amount, self.tax_ratio), 2))
            tax_plus_amount = "$" + '{:.2f}'.format(round(self.brain.getTaxesPlusAmount(self.amount, self.tax_ratio), 2))
            self.taxes_result["text"] = f'{tax} - {tax_plus_amount}'
            tip = "$" + '{:.2f}'.format(round(self.brain.getTip(self.amount, self.tip_ratio), 2))
            tip_plus_amount = "$" + '{:.2f}'.format(round(self.brain.getTipPlusAmount(self.amount, self.tip_ratio), 2))
            self.tip_result["text"] = f'{tip} - {tip_plus_amount}'
            result = self.brain.getResult(self.amount, self.tax_ratio, self.tip_ratio)
            self.result_field.delete(0, END)
            self.result_field.insert(tk.INSERT, "$" + '{:.2f}'.format(result))
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def changeTaxRatio(self, evt):
        if evt.char == '\x7f':
            self.taxes_field.delete(first=0,last=10)
            self.tax = ""
            self.amount_field.delete(0, END)
            self.result_field.delete(0, END)
            self.amount = ""
            self.taxes_result["text"] = "$0.00 - $0.00"
            self.tip_result["text"] = "$0.00 - $0.00"
        else:
            self.tax += evt.char
            self.tax_ratio = float(self.tax)
            # f = open('MichiganTaxTip/tax.pckl', 'wb')
            f = open(f'{os.getcwd()}/tax.pckl', 'wb')
            pickle.dump(self.tax_ratio, f)
            f.close()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
    def changeTipRatio(self, evt):
        if evt.char == '\x7f':
            self.tip_field.delete(first=0,last=10)
            self.tip = ""
            self.amount_field.delete(0, END)
            self.result_field.delete(0, END)
            self.amount = ""
            self.taxes_result["text"] = "$0.00 - $0.00"
            self.tip_result["text"] = "$0.00 - $0.00"
        else:
            self.tip += evt.char
            self.tip_ratio = float(self.tip)
            # f = open('MichiganTaxTip/tip.pckl', 'wb')
            f = open(f'{os.getcwd()}/tip.pckl', 'wb')
            pickle.dump(self.tip_ratio, f)
            f.close()
    # ¬¬¬¬¬¬¬¬¬¬¬¬
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()














