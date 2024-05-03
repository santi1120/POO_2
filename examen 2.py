from tkinter import *
from tkinter import ttk
window = Tk() #comando para abrir la ventana de opciones 
window.title("cuestionario de intro")#nombre de la ventana 
window.geometry('450x700')# tamaño de la ventana 
window.configure(background = "green");#comando para color del fondo 
a = Label(window ,text = "apodo").grid(row = 0,column = 0) #espacio en blanco para contestar tus preguntas (aplica para todos los label)
b = Label(window ,text = "apellido").grid(row = 1,column = 0)
c = Label(window ,text = "direccion de correo electronico").grid(row = 2,column = 0)
d = Label(window ,text = "telefono cel").grid(row = 3,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)# espacio entre preguntas (aplica para todos los entry)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 2,column = 1)
d1 = Entry(window).grid(row = 3,column = 1)
def clicked(): #Va a ser una definicion para que el boton se pueda presionar
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
window.mainloop()