from tkinter import *
from tkinter import colorchooser

# Función para abrir el selector de color
def elegir_color():
    color = colorchooser.askcolor(title="Elige un color")
    if color[1]:  # color[1] es el valor hexadecimal
        color_label.config(text=f"Color elegido: {color[1]}", bg=color[1])

# Crear la ventana principal
ventana = Tk()
ventana.title("Color Picker App")
ventana.geometry("300x150")

# Botón para elegir el color
boton = Button(ventana, text="Seleccionar color", command=elegir_color)
boton.pack(pady=20)

# Etiqueta para mostrar el color elegido
color_label = Label(ventana, text="Color elegido: Ninguno")
color_label.pack(pady=10)

ventana.mainloop()