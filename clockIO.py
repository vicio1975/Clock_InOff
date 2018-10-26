# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:16:05 2018

@author: bmusammartanov
"""

#import numpy as num
import tkinter as tk
#from tkinter import  messagebox
#from PIL import ImageTk, Image

#Tkinter window
root = tk.Tk() #new window
root.geometry("700x470+100+50")
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
rc = 40
for i in range(10):
    root.rowconfigure(i, minsize=rc)
    
#input part
#Clock in/out selection    
l0 = tk.Label(root,text="Clock In ", padx = 10,font=f_BO10)
l0.grid(row=0,column=0,sticky="w")
l0_1 = tk.Label(root,text="[hh:mm]",padx = 10,font=f_BO10)
l0_1.grid(row=0,column=2)
T_ = tk.StringVar()
t1 = tk.Entry(root,textvariable= T_ , width=6,justify="center",font=f_10)
t1.grid(row=0,column=1)
t1.insert("end", 20)  
    
    
    
    
    
    
    
    
root.mainloop() #looping the frame