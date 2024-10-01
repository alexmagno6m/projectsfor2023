from tkinter import *
from ttkbootstrap import *

root = Window(themename="morph")
root.geometry("380x80")


frame = LabelFrame(root, text="Seccion de botones")
frame.pack(side=LEFT)

boton2 = Button(frame, text="Salida")
boton2.pack(padx=10, pady=10, side=LEFT)

boton2a = Button(frame, text="Salida")
boton2a.pack(padx=10, pady=10, side=LEFT)

frame2 = LabelFrame(root, text="Seccion 2 de botones")
frame2.pack(side=RIGHT)

boton3 = Button(frame2, text="Cancel")
boton3.pack(padx=10, pady=10, side=LEFT)

boton3a = Button(frame2, text="Cancel")
boton3a.pack(padx=10, pady=10, side=LEFT)

root.mainloop()
