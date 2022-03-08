

import tkinter as tk
from tkinter import font

#Ventanas
vent0=tk.Tk()
vent0.title("Login")
vent0.config(bg="white")
vent0.geometry("900x507")





fond1=tk.PhotoImage(file="spiderman negro.png")
fond0=tk.Label(vent0,image=fond1).place(x=0,y=0)



boton1=tk.Button(vent0,text="Iniciar",bg="blue")
boton1.place(x=50,y=50)

boton1=tk.Button(vent0,text="Salir",bg="blue")
boton1.place(x=100,y=50)







vent0.mainloop()