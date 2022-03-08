#LOGIN Spiderman (Jhois COllado)

from asyncio.format_helpers import _format_callback_source
from cgitb import text
import tkinter as tk
from tkinter import font
from turtle import title


#1ra Ventana
vent0=tk.Tk()
vent0.resizable(width=False, height=False)
vent0.title("Login-🕷️")
vent0.config(bg="white")
vent0.geometry("638x900+550+250")


#Fondo de ventana e icono

vent0.iconbitmap("morales.ico") #icono

fond=tk.PhotoImage(file="Spider-Man.png")
fond1=tk.Label(vent0,image=fond).place(x=0,y=0)

fond2=tk.PhotoImage(file="logo2.png")
fond3=tk.Label(vent0,image=fond2).place(x=265,y=290)

#Etiquetas

etiqueta1=tk.Label(vent0,text="Usuario")
etiqueta1.place(x=253,y=520)
etiqueta1.config(bg="#0b97e9",font=("Eras Demi ITC",12))

etiqueta2=tk.Label(vent0,text="Contraseña")
etiqueta2.place(x=225,y=550)
etiqueta2.config(bg="#0b97e9",font=("Eras Demi ITC",12))


#Entradas

Usuario=tk.StringVar()
Contraseña=tk.StringVar()

entrada_u=tk.Entry(vent0,textvariable=Usuario).place(x=320,y=550)
entrada_c=tk.Entry(vent0,textvariable=Contraseña).place(x=320,y=520)

def entrada():
    nombre=Usuario.get()
    Con=Contraseña.get()
    
    if nombre== "10" and Con=="10":
        verdadero()
    else:
        pass

def verdadero():         #2da ventana
    vent0.withdraw()
    vent1=tk.Toplevel()
    vent1.resizable(width=False, height=False)
    vent1.title("Bienvenido-🕷️")
    vent1.geometry("500x400+550+250")
    vent1.config(bg="black")


    vent1.iconbitmap("morales.ico") #icono

    fond4=tk.PhotoImage(file="venom 4k.png")
    font5=tk.Label(vent1,image=fond4).place(x=0,y=0)

    vent1.mainloop()

#Botones

boton=tk.Button(vent0,text="Iniciar Sesión")
boton.place(x=320,y=600)
boton.config(bg="#0b97e9",command=entrada,font=("Eras Demi ITC",13))





vent0.mainloop()