# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:16:05 2018
test 
@author: bmusammartanov
"""

#import numpy as num
import tkinter as tk
from tkinter import  messagebox
import datetime
import math
import locale
locale.setlocale(locale.LC_TIME, "it_IT")

#Tkinter window
root = tk.Tk() #new window
root.geometry("650x250+100+100")
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
    oggi = datetime.datetime.today()
    oggi = oggi.strftime("%d/%m/%Y - %H:%M:%S - ")
    giorno = datetime.datetime.today().strftime("%A")
    giorno = giorno.capitalize()
    texttime = "Oggi è {} {}".format(oggi, giorno)
    ltime.configure(text= texttime)

    root.after(1000, click)
    
    return giorno

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
    
    if giorno == "Venerdi":
        messagebox.showinfo("message", "Happy Friday!!!")

   
# Funzione per calcolare l'orario di uscita
def calcola_uscita():
    try:
        # Ottieni l'orario di ingresso
        orario_ingresso = ingresso_var.get()
        ore_lavoro = 8  # Ore lavorative fisse

        # Converti l'orario in datetime
        ingresso_time = datetime.datetime.strptime(orario_ingresso, "%H:%M")

        # Ottieni le ore extra (gestendo il caso in cui non venga inserito un valore)
        try:
            ore_extra = float(extra_var.get())  # Converte l'input in numero
        except ValueError:
            ore_extra = 0  # Se l'input non è valido, assume 0 ore extra

        # Determina la durata della pausa pranzo
        pausa_minuti = 30 if pausa_var.get() == "30 min" else 60  # 30 o 60 minuti

        # Calcola l'orario di uscita
        uscita_time = ingresso_time + datetime.timedelta(hours=ore_lavoro, minutes=pausa_minuti) + datetime.timedelta(hours=ore_extra)

        # Mostra il risultato
        uscita_label.config(text=f"Orario di uscita: {uscita_time.strftime('%H:%M')}", fg="blue")

    except ValueError:
        messagebox.showerror("Errore", "Inserisci un orario valido nel formato HH:MM")

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

########## TARGET
# Sezione per l'orario di uscita
ora_in = tk.Label(root, text="Orario di ingresso (HH:MM):", font=f_BO10).place(x=365, y=30)
ingresso_var = tk.StringVar()
ingresso_entry = tk.Entry(root, textvariable=ingresso_var, width=10, justify="center",font=f_BO10)
ingresso_entry.place(x=550, y= 30)
ingresso_entry.insert(0, "08:30")  # Default

# Selezione della durata della pausa pranzo
tk.Label(root, text="Durata pausa pranzo:", font=f_BO10).place(x=365, y=70)
pausa_var = tk.StringVar(value="1 ora")
pausa_menu = tk.OptionMenu(root, pausa_var, "30 min", "1 ora")
pausa_menu.place(x=550, y=65)

#Seleziona ore di straordinario
extra_time = tk.Label(root, text="Ore straordinario :", font=f_BO10).place(x=400, y=110)
extra_var = tk.StringVar()
extra_entry = tk.Entry(root, textvariable=extra_var, width=10, justify="center", font=f_BO10)
extra_entry.place(x= 550, y= 110)
extra_entry.insert(0, "1")  # Default

# Pulsante per calcolare l'orario di uscita
calcola_btn = tk.Button(root, text="Calcola Uscita", command=calcola_uscita, font=f_BO10)
calcola_btn.place(x=460, y=160)

# Label per mostrare il risultato
uscita_label = tk.Label(root, text="", font=f_BO10, fg="blue")
uscita_label.place(x=400, y=200)

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
