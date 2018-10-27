# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:16:05 2018

@author: bmusammartanov
"""

#import numpy as num
import tkinter as tk
from tkinter import  messagebox
#from PIL import ImageTk, Image

#Tkinter window
root = tk.Tk() #new window
root.geometry("450x300+100+100")
root.title("Clock In/Out")
root.resizable(width=False, height=False)

#Fonts
f_8 = ("arial",8)
f_9 = ("arial",9)
f_10 = ("arial",10)
f_12 = ("arial",12)

f_IT8 = ("arial",8,"italic")
f_IT8 = ("arial",8,"italic")
f_IT9 = ("arial",9,"italic")
f_IT11 = ("arial",11,"italic")
f_BO7 = ("arial",7,"bold")
f_BO9 = ("arial",9,"bold")
f_BO10 = ("arial",10,"bold")
f_BO12 = ("arial",12,"bold")

##columnconfig
rc = 30
for i in range(10):
    root.rowconfigure(i, minsize=rc)

###function 
    
def calc():
    hin = float(T1_.get())
    minIn = float(M1_.get())/60
    hout = float(T2_.get())
    minOut = float(M2_.get())/60
    hIN  = hin + minIn
    hOUT = hout + minOut

    if hOUT < hIN:
        messagebox.showwarning("Error","Off time is lower than In time!\n\n Remember to use a 24h format")
    
    elif hOUT <= 12.5:
        luncH = 0

    elif hOUT >= 13.5:
        luncH = 1

    elif (hOUT > 12.5) and (hOUT < 13.5):
        luncH = 0

    todayH = hOUT - hIN - luncH
    hoursL = weekHours - todayH
        
    l3 = tk.Label(root,text="Today's hours", padx = 10,font=f_BO10,fg = "red")   
    l3.grid(row = 4, column = 0)
    l3_1 = tk.Label(root,text="{:1.2f}".format(todayH),padx = 10,font=f_BO10,
                    fg = "red")
    l3_1.grid(row = 4, column = 1)
    
    l4 = tk.Label(root,text="Hours left", padx = 10,font=f_BO10,fg = "red")   
    l4.grid(row = 5, column = 0)
    l4_1 = tk.Label(root,text="{:1.2f}".format(hoursL),padx = 10,font=f_BO10,
                    fg = "red")
    l4_1.grid(row = 5, column = 1)

    
#input part
#Clock in/out selection    
l1 = tk.Label(root,text="Clock In ", padx = 10,font=f_BO10)
l1.grid(row=1,column=0,sticky="e")
l1_1 = tk.Label(root,text="[hh:mm]", font=f_BO10)
l1_1.grid(row=1,column=3)

l2 = tk.Label(root,text="Clock Out ", padx = 10,font=f_BO10)
l2.grid(row=2,column=0,sticky="e")
l2_1 = tk.Label(root,text="[hh:mm]", font=f_BO10)
l2_1.grid(row=2,column=3)

l3 = tk.Label(root,text="Hours done ", padx = 10,font=f_BO10)
l3.grid(row=3,column=0,sticky="e")
l3_1 = tk.Label(root,text="[hh:mm]", font=f_BO10)
l3_1.grid(row=3,column=3)

#Clock In 
#hours
T1_ = tk.StringVar()
t1 = tk.Entry(root,textvariable= T1_ , width=6,justify="center",font=f_10)
t1.grid(row=1,column=1)
t1.insert("end", "00")  
#minutes
M1_ = tk.StringVar()
m1 = tk.Entry(root,textvariable= M1_ , width=6,justify="center",font=f_10)
m1.grid(row=1,column=2)
m1.insert("end", "00")  

#Clock Out
#hours
T2_ = tk.StringVar()
t2 = tk.Entry(root,textvariable= T2_ , width=6,justify="center",font=f_10)
t2.grid(row=2,column=1)
t2.insert("end", "00")  
#minutes
M2_ = tk.StringVar()
m2 = tk.Entry(root,textvariable= M2_ , width=6,justify="center",font=f_10)
m2.grid(row=2,column=2)
m2.insert("end", "00")  

#plus Hours
T3_ = tk.StringVar()
t3 = tk.Entry(root,textvariable= T3_ , width=6,justify="center",font=f_10)
t3.grid(row=3,column=1)
t3.insert("end", "00")  
#plus minutes
M3_ = tk.StringVar()
m3 = tk.Entry(root,textvariable= M3_ , width=6,justify="center",font=f_10)
m3.grid(row=3,column=2)
m3.insert("end", "00")  


########### hours of work
weekHours = 37.5

l0 = tk.Label(root,text="Total Week's hours", padx = 10,font=f_BO10)   
l0.grid(row=0,column=0)
l0_1 = tk.Label(root,text="{}".format(weekHours),padx = 10,font=f_BO10)
l0_1.grid(row=0,column=1)


#Buttons
c0 = tk.Button(root,text="Calculate",command=calc,font=f_BO9)
c0.config( height = 2, width = 8)
c0.grid(row=4,column=4)

ln = tk.Button(root,text="Exit",command=root.destroy,font=f_BO9)
ln.config( height = 2, width = 8)
ln.grid(row=5,column=4)

    
root.mainloop() #looping the frame