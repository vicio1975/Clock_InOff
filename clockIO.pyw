# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:16:05 2018

@author: bmusammartanov
"""

#import numpy as num
import tkinter as tk
from tkinter import  messagebox
import datetime
from PIL import Image  

#Tkinter window
root = tk.Tk() #new window
root.geometry("345x187+100+100")
root.title("Clock In/Out")
root.resizable(width=False, height=False)
#root.iconbitmap(r'clock.ico')

#Fonts
f_8 = ("arial", 8)
f_9 = ("arial", 9)
f_10 = ("arial", 10)
f_12 = ("arial", 12)

f_IT8 = ("arial", 8, "italic")
f_IT8 = ("arial", 8, "italic")
f_IT9 = ("arial", 9, "italic")
f_IT11 = ("arial", 11, "italic")
f_BO7 = ("arial", 7, "bold")
f_BO9 = ("arial", 9, "bold")
f_BO10 = ("arial", 10, "bold")
f_BO12 = ("arial", 12, "bold")

##columnconfig
rc = 30
for i in range(10):
    root.rowconfigure(i, minsize=rc)
    root.columnconfigure(i, minsize=60)

###function
def click():
    now = datetime.datetime.today().strftime("%d/%m/%Y - %H:%M")
    wd = datetime.datetime.today().strftime("%A")
    texttime = "Today is {} - {}".format(now,wd)
    ltime.configure(text= texttime)
    root.after(1000, click)
    return wd

def calc():
    #In Time
    hIN = float(T1_.get()) + float(M1_.get())/60
    #Out Time
    hOUT = float(T2_.get()) + float(M2_.get())/60
    #Left time
    hLEFTover = float(T3_.get()) + float(M3_.get())/60    

    if hOUT < hIN:
        messagebox.showwarning("Error",
                               "Off time is lower than In time!\n\n Remember to use a 24h format")
        luncH = 0
    elif hIN == 0:
        messagebox.showwarning("Error",
                               "Please add some input!\n\n ... remember to use a 24h format")
        luncH = 0
        
    elif hIN < 6.5:
        messagebox.showwarning("Error",
                               "Please add a valid input!\n\n ... InTime has to be bigger than 06:30")       
        luncH = 0
    elif hOUT <= 13.5:
        luncH = 0

    elif hOUT > 13.5:
        luncH = 1

    todayH = hOUT - hIN - luncH
    
    hoursL = (todayH + hLEFTover) - 7.5
 
    hL = int(abs( hoursL ))
    mL = round((abs(hoursL)-hL) * 60)
    
    if mL == 60:
        mL = 0
        hL = 1

    todayText = "Today's hours\t"+"{:02.2f}".format(todayH)+"\thours"
    l3h = tk.Label(root,text=todayText,font=f_BO10,fg = "red")   
    l3h.place(x= 35, y= 128)

    if (hoursL < 0) :
        ttt = "-"+"{:02.0f}:{:02.0f}".format(hL,mL)
    elif (hoursL >= 0) :
        ttt = "{:02.0f}:{:02.0f}".format(hL,mL)
    
    ttt_ = "Daily balance\t"+ttt+"\thh:mm"    
    l4 = tk.Label(root,text=ttt_,font=f_BO10,fg = "red")   
    l4.place(x= 35,y=155)

    if dd == "Friday":
        messagebox.showinfo("message", "Happy Friday!!!")


####time
ltime = tk.Label(root, padx = 20, font = f_BO10)
ltime.place(x = 50, y = 10)

# input part
# Clock in/out selection
l1 = tk.Label(root, text = "Clock In ", padx = 10, font=f_BO10)
l1.grid(row=1, column=0, sticky="e")
l1_1 = tk.Label(root, text="[hh:mm]", font=f_BO10)
l1_1.grid(row=1, column=3)

l2 = tk.Label(root, text="Clock Out ", padx = 10,font=f_BO10)
l2.grid(row=2,column=0, sticky="e")
l2_1 = tk.Label(root,text="[hh:mm]", font=f_BO10)
l2_1.grid(row=2,column=3)

l3 = tk.Label(root,text="Hours leftover ", padx = 10,font=f_BO10)
l3.grid(row=3,column=0,sticky="e")
l3_2 = tk.Label(root,text="[hh:mm]", font=f_BO10)
l3_2.grid(row=3,column=3)

#Clock In 
#hours
T1_ = tk.StringVar()
t1 = tk.Entry(root,textvariable= T1_ , width=10,justify="center",font=f_10)
t1.grid(row=1,column=1)
t1.insert("end", "00")  
#minutes
M1_ = tk.StringVar()
m1 = tk.Entry(root,textvariable= M1_ , width=10,justify="center",font=f_10)
m1.grid(row=1,column=2)
m1.insert("end", "00")  

#Clock Out
#hours
T2_ = tk.StringVar()
t2 = tk.Entry(root,textvariable= T2_ , width=10,justify="center",font=f_10)
t2.grid(row=2,column=1)
t2.insert("end", "00")  
#minutes
M2_ = tk.StringVar()
m2 = tk.Entry(root,textvariable= M2_ , width=10,justify="center",font=f_10)
m2.grid(row=2,column=2)
m2.insert("end", "00")  

#Hours Left
T3_ = tk.StringVar()
t3 = tk.Entry(root,textvariable= T3_ , width=10,justify="center",font=f_10)
t3.grid(row=3,column=1)
t3.insert("end", "00")  
#minutes left
M3_ = tk.StringVar()
m3 = tk.Entry(root,textvariable= M3_ , width=10,justify="center",font=f_10)
m3.grid(row=3,column=2)
m3.insert("end", "00")  
########### hours of work

#Buttons
frame00 = tk.Frame(width=264,height=58, colormap="new",relief="sunken",bd=2)
frame00.place(x=8,y=122)

c0 = tk.Button(root,text= "Go!",command=calc,font=f_BO10)
c0.config( height = 2, width = 4)
c0.place(x = 280, y = 130)

###########

#Main
dd = click()
root.mainloop() #looping the frame
