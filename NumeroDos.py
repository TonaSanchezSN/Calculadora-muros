from tkinter import *

ventana = Tk()
ventana.title("Ventana prueba")
ventana.resizable(1,1)
ventana.iconbitmap("icono.ico")

ventana.config(width =  "1920", height="1080")

#Textos
hori = 30
tabla1Pesta1 = Label (ventana, text = "Datos generales de la construcción",font= 'Calibri 11 bold').place(x = hori, y= 20)

ventana.mainloop()