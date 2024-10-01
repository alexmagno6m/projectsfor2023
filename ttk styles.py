from tkinter import *
from tkinter.ttk import *

# Crear la ventana principal
root = Tk()
root.geometry("300x200")

# Crear un estilo personalizado
style = Style()
style.configure("Marco1.TLabelframe", background="lightblue", relief="ridge", padding=10)
style.configure("Marco1.TLabelframe.Label", background="lightblue", foreground="blue", font=("Arial", 12, "bold"))

# Crear un LabelFrame con el estilo personalizado
frame = LabelFrame(root, text="Mi LabelFrame", style="Marco1.TLabelframe")
frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Crear un Label dentro del LabelFrame
label = Label(frame, text="Hola", background="lightblue")
label.pack()

# Iniciar el loop principal de la aplicación
root.mainloop()