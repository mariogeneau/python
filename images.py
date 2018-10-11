from tkinter import *
import base64
import urllib
root = Tk()
URL = "butterfly.jpeg"
link = urllib.urlopen(URL)
raw_data = link.read()
link.close()
next = base64.encodestring(raw_data)
image = PhotoImage(data=next)
label = Label(image=image)
label.pack()
root.mainloop()
