# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:16:05 2018

@author: bmusammartanov
"""

#import numpy as num
import tkinter as tk
from tkinter import  messagebox
import datetime
import math

#Tkinter window
root = tk.Tk() #new window
root.geometry("345x250+100+100")
root.title("Clock In/Out")
root.resizable(width=False, height=False)

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
    #Lunch
    lunchIn = float(L1_.get()) + float(M2_.get())/60
    lunchOut = float(L2_.get()) + float(M3_.get())/60
    lunch = lunchOut - lunchIn
    #Out Time
    hOUT = float(T2_.get()) + float(M4_.get())/60
    
    if lunch < 0.5:
        lunch = 0.5

    if hOUT < hIN:
        messagebox.showwarning("Error",
                               "Orario di uscita inferiore dell'orario in ingresso!\n\n Ricorda di usare il formato 24h")
        lunch = 0
    elif hIN == 0:
        messagebox.showwarning("Error",
                               "Aggiungi i dati corretti!\n\n ... usa il formato 24h")
        lunch = 0
    elif hIN < 7.5:
        messagebox.showwarning("Error",
                               "Aggiungi i dati corretti!\n\n ... L'orario in ingresso deve essere superiore alle 07:30")
        lunch = 0
    
    todayH = (hOUT - hIN) - lunch
    
    todayText = "Ore totali lavorate..."+"{:02.2f}".format((todayH))
    l3h = tk.Label(root,text=todayText,font=f_BO10,fg = "red")   
    l3h.place(x= 55, y= 167)


    extraH = todayH - 8

    if extraH < 0:
        extraH = 0
        oreord = todayH
    elif extraH >=0:
        oreord = todayH - extraH
        
    todayOrd = "Ore ordinarie...{:02.2f}".format(oreord)
    todayExt = "Ore extra...{:02.2f}".format(0.5 * math.floor(extraH * 2 + 0.5))

    l4h = tk.Label(root,text=todayOrd,font=f_BO10,fg = "red")   
    l4h.place(x= 55, y= 193)

    l5h = tk.Label(root,text=todayExt,font=f_BO10,fg = "red")   
    l5h.place(x= 55, y= 217)
    
    if dd == "Friday":
        messagebox.showinfo("message", "Happy Friday!!!")


####time
ltime = tk.Label(root, padx = 20, font = f_BO10)
ltime.place(x = 50, y = 10)

# input part
# Clock in/out selection
lab1 = tk.Label(root, text = "Ingresso ", padx = 10, font=f_BO10)
lab1.grid(row=1, column=0, sticky="e")
lab1_1 = tk.Label(root, text="   [hh:mm]", font=f_BO10)
lab1_1.grid(row=1, column=3)

lab2 = tk.Label(root,text="Inizio Pranzo ", padx = 10,font=f_BO10)
lab2.grid(row=2,column=0,sticky="e")
lab2_1 = tk.Label(root,text="   [hh:mm]", font=f_BO10)
lab2_1.grid(row=2,column=3)

lab3 = tk.Label(root,text="Fine Pranzo ", padx = 10,font=f_BO10)
lab3.grid(row=3,column=0,sticky="e")
lab3_1 = tk.Label(root,text="   [hh:mm]", font=f_BO10)
lab3_1.grid(row=3,column=3)

lab4 = tk.Label(root, text="Uscita ", padx = 10,font=f_BO10)
lab4.grid(row=4,column=0, sticky="e")
lab4_1 = tk.Label(root,text="   [hh:mm]", font=f_BO10)
lab4_1.grid(row=4,column=3)

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

#Lunch in
#hours
L1_ = tk.StringVar()
l1 = tk.Entry(root,textvariable= L1_ , width=10,justify="center",font=f_10)
l1.grid(row=2,column=1)
l1.insert("end", "00")  
#minutes
M2_ = tk.StringVar()
m2 = tk.Entry(root,textvariable= M2_ , width=10,justify="center",font=f_10)
m2.grid(row=2,column=2)
m2.insert("end", "00")

#Lunch out
#hours
L2_ = tk.StringVar()
l2 = tk.Entry(root,textvariable= L2_ , width=10,justify="center",font=f_10)
l2.grid(row=3,column=1)
l2.insert("end", "00")  
#minutes
M3_ = tk.StringVar()
m3 = tk.Entry(root,textvariable= M3_ , width=10,justify="center",font=f_10)
m3.grid(row=3,column=2)
m3.insert("end", "00")

#Clock Out
#hours
T2_ = tk.StringVar()
t2 = tk.Entry(root,textvariable= T2_ , width=10,justify="center",font=f_10)
t2.grid(row=4,column=1)
t2.insert("end", "00")  
#minutes
M4_ = tk.StringVar()
m4 = tk.Entry(root,textvariable= M4_ , width=10,justify="center",font=f_10)
m4.grid(row=4,column=2)
m4.insert("end", "00")


########### hours of work

#output
frame00 = tk.Frame(width=210,height=80, colormap="new",relief="sunken",bd=2)
frame00.place(x=40,y=164)

c0 = tk.Button(root,text= "Go!",command=calc,font=f_BO10)
c0.config( height = 2, width = 6)
c0.place(x = 270, y = 180)

###########

#Main
dd = click()
root.mainloop() #looping the frame
