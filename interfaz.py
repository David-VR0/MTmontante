import tkinter as tk
from tkinter import *
import os, sys
import montante

def borrar():
    etiquetar1 = tk.Label(text="                            ", font=("Arial", 14), fg='#FF0000' )
    etiquetar1.place(x=80, y=210)
    etiquetar2 = tk.Label(text="                            ", font=("Arial", 14), fg='#FF0000')
    etiquetar2.place(x=80, y=240)
    etiquetar3 = tk.Label(text="                            ", font=("Arial", 14), fg='#FF0000')
    etiquetar3.place(x=80, y=270)
def antr():
    borrar()
    matriz=[]
    matriz=[[ax.get(),ay.get(),az.get(),1,0,0],[bx.get(), by.get(), bz.get(),0,1,0],[cx.get(), cy.get(), cz.get(),0,0,1]]
    a = ag.get()
    b = bg.get()
    c = cg.get()
    x1,x2,x3 = montante.resolver(matriz,a,b,c)
    etiquetar1 = tk.Label(text="{0:.6f}".format(x1), font=("Arial", 14), fg='#FF0000' )
    etiquetar1.place(x=80, y=210)
    etiquetar2 = tk.Label(text="{0:.6f}".format(x2), font=("Arial", 14), fg='#FF0000')
    etiquetar2.place(x=80, y=240)
    etiquetar3 = tk.Label(text="{0:.6f}".format(x3), font=("Arial", 14), fg='#FF0000')
    etiquetar3.place(x=80, y=270)



#Creamos la ventana

root = tk.Tk() #creamos la ventana
root.title("Analisis Numerico")
root.resizable(0,0)
root.geometry("400x300+500+100")

#variable de entrada
ax = tk.DoubleVar()
ay = tk.DoubleVar()
az = tk.DoubleVar()
ag = tk.DoubleVar()
bx = tk.DoubleVar()
by = tk.DoubleVar()
bz = tk.DoubleVar()
bg = tk.DoubleVar()
cx = tk.DoubleVar()
cy = tk.DoubleVar()
cz = tk.DoubleVar()
cg = tk.DoubleVar()

m = Canvas(root, width=200, height=300)
m.pack(fill="x")


etiqueta1 = tk.Label(text="Método de Montante", font=("Arial", 20))
etiqueta1.place(x=80,y=10)


etiqueta2 = tk.Label(text="x\u2081 +", font=("Arial", 15))
etiqueta2.place(x=60,y=100)

entrada = tk.Entry(width=4,textvariable=ax)
entrada.place(x=30,y=100)

etiqueta3 = tk.Label(text="x\u2082 +", font=("Arial", 15))
etiqueta3.place(x=120,y=100)

entrada1 = tk.Entry(width=4,textvariable=ay)
entrada1.place(x=90,y=100)

etiqueta4 = tk.Label(text="x\u2083 =", font=("Arial", 15))
etiqueta4.place(x=180,y=100)

entrada2 = tk.Entry(width=4,textvariable=az)
entrada2.place(x=150,y=100)

entradai = tk.Entry(width=4,textvariable=ag)
entradai.place(x=215,y=100)

etiqueta5 = tk.Label(text="x\u2081 +", font=("Arial", 15))
etiqueta5.place(x=60,y=130)

entrada3 = tk.Entry(width=4,textvariable=bx)
entrada3.place(x=30,y=130)

etiqueta6 = tk.Label(text="x\u2082 +", font=("Arial", 15))
etiqueta6.place(x=120,y=130)

entrada4 = tk.Entry(width=4,textvariable=by)
entrada4.place(x=90,y=130)

etiqueta7 = tk.Label(text="x\u2083 =", font=("Arial", 15))
etiqueta7.place(x=180,y=130)

entrada5 = tk.Entry(width=4,textvariable=bz)
entrada5.place(x=150,y=130)

entradai1 = tk.Entry(width=4,textvariable=bg)
entradai1.place(x=215,y=130)

etiqueta8 = tk.Label(text="x\u2081 +", font=("Arial", 15))
etiqueta8.place(x=60,y=160)

entrada6 = tk.Entry(width=4,textvariable=cx)
entrada6.place(x=30,y=160)

etiqueta9 = tk.Label(text="x\u2082 +", font=("Arial", 15))
etiqueta9.place(x=120,y=160)

entrada7 = tk.Entry(width=4,textvariable=cy)
entrada7.place(x=90,y=160)

etiqueta10 = tk.Label(text="x\u2083 =", font=("Arial", 15))
etiqueta10.place(x=180,y=160)

entrada8 = tk.Entry(width=4,textvariable=cz)
entrada8.place(x=150,y=160)

entradai2 = tk.Entry(width=4,textvariable=cg)
entradai2.place(x=215,y=160)



boton1 = tk.Button(text="Iniciar", command=antr)
boton1.place(x=280,y=130)

etiqueta11 = tk.Label(text="x1 =", font=("Arial", 14))
etiqueta11.place(x=30,y=210)
etiqueta12 = tk.Label(text="x2 =", font=("Arial", 14))
etiqueta12.place(x=30,y=240)
etiqueta13 = tk.Label(text="x3 =", font=("Arial", 14))
etiqueta13.place(x=30,y=270)
root.mainloop()