#!/usr/bin/env python

import sys
from Tkinter import *
import tkMessageBox
import tkFileDialog
import wave


def mhello():
    pass
    return
def mQuit():
    mExit = tkMessageBox.askyesno(title="Quit",message="Are you Sure?")
    if mExit > 0:
        mGui.destroy()
        return

def nOpen():
    myOpen = tkFileDialog.askopenfile()
    txt = wave.open(myOpen,'r')
    sample_rate = txt.getframerate()
    print sample_rate
    return

def print_value(val):
    print val

mGui = Tk()
mGui.geometry('800x800+300+20')
mGui.title('Assignment')
mlabel = Label(mGui,text="My Label",fg="red",bg="white").grid(row = 1,column = 1)
mbutton = Button(text="OK").place(x=200,y=200)
menubar = Menu(mGui)
filemenu = Menu(menubar)
filemenu.add_command(label="New")
filemenu.add_command(label="Open",command=nOpen)
filemenu.add_command(label="Save As..")
filemenu.add_command(label="Close",command=mQuit)

menubar.add_cascade(label="File",menu=filemenu)
Slider_1 = Scale(mGui,orient=HORIZONTAL,length=300,width=20,sliderlength=30,from_=0,to=50,tickinterval=5,command=print_value).place(x=50,y=50)
mGui.config(menu=menubar)


mGui.mainloop()
