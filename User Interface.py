#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from calc import ellipticcurvehash as ec

class gui:
def __init__(self,master):
self.master = master
self.framei = Frame(master)
self.framei.pack()
self.inputmsg = Label(self.framei, text="Please Enter The Message",
font=("Helvetica", 14))
self.namevar = StringVar()
self.entry = Text(self.framei,font=("Helvetica", 14), width=90, height=10)
self.button = Button(self.framei, text="Submit", command=self.findhash1,
font=("Helvetica", 14))
self.inputmsg.grid(row=0, pady=15)
self.entry.grid(row=1, pady=15)
self.button.grid(row=1,column=2)
self.entry.bind("<Return>", self.findhash1)
self.outhash = Label(self.framei, text="The Message Fingerprint", font=("Helvetica",
14))
self.hashvar = StringVar()
self.op = Entry(self.framei, textvariable=self.hashvar, width=70,font=("Helvetica",
14),state='readonly')
self.hashvar.set("")
self.outhash.grid(row=2, pady=15)
self.op.grid(row=3, pady=15)

def findhash1(self, *args):
self.msg = self.entry.get("1.0",'end-1c')
self.object = ec.hashfind()
self.hashvar.set(self.object.findhash(self.msg))

if __name__=="__main__":
root=Tk()
ob=gui(root)
root.title("Elliptic Curve Hash Generator")
root.mainloop()

