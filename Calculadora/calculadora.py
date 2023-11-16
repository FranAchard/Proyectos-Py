from tkinter import*

ventana =Tk()
ventana.title("Calculadora")
ventana.geometry("350x300")

#Entrada
e_texto=Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=0 , column=0, columnspan=4 , padx=5 , pady=5)

#Botones
boton1 = Button(ventana, text="1", width=5, height=2)
boton2 = Button(ventana, text="2", width=5, height=2)
boton3 = Button(ventana, text="3", width=5, height=2)
boton4 = Button(ventana, text="4", width=5, height=2)
boton5 = Button(ventana, text="5", width=5, height=2)
boton6 = Button(ventana, text="6", width=5, height=2)
boton7 = Button(ventana, text="7", width=5, height=2)
boton8 = Button(ventana, text="8", width=5, height=2)
boton9 = Button(ventana, text="9", width=5, height=2)
boton0 = Button(ventana, text="0", width=13, height=2)

boton_borrar = Button(ventana, text="AC", width=5, height=2)
boton_parentesis1 = Button(ventana, text="(", width=5, height=2)
boton_parentesis2 = Button(ventana, text=")", width=5, height=2)
boton_punto = Button(ventana, text=".", width=5, height=2)

boton_suma = Button(ventana, text="+", width=5, height=2)
boton_resta = Button(ventana, text="-", width=5, height=2)
boton_division = Button(ventana, text="/", width=5, height=2)
boton_multiplicacion = Button(ventana, text="x", width=5, height=2)
boton_igual = Button(ventana, text="=", width=5, height=2)

#Agregar los botones
boton_borrar.grid(row= 1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row= 1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row= 1, column=2, padx=5, pady=5)
boton_division.grid(row= 1, column=3, padx=5, pady=5)

ventana.mainloop()