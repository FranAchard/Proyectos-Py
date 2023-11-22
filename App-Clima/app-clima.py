from tkinter import*

ventana = Tk()
ventana.title("App Clima")
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font= ("Courier", 20, "normal"), justify="center")
texto_ciudad.pack(padx=30, pady=30)

obtener_clima= Button(ventana,text="Obtener Clima")
obtener_clima.pack()

ventana.mainloop