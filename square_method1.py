from tkinter import *
from tkinter.ttk import *

root = Tk()
root.minsize(width=300, height=200)
root.title("Square area")

base = StringVar()
height = StringVar()
areaTotal = Label(root)

def areasize(event=None):
    global areaTotal
    c = float(e1.get()) * float(e2.get())
    areaTotal = Label(text='the area is {}'.format(c))
    areaTotal.pack()

def set_focus(event):
    e1.focus()

l1 = Label(root, text='base')
l1.pack(anchor=W, padx=10, pady=5, fill=X)

e1 = Entry(root, textvariable=base)
e1.pack(anchor=W, padx=10, pady=5, fill=X)
e1.focus_set()  # Establecer el foco en el campo de entrada e1

l2 = Label(root, text='height')
l2.pack(anchor=W, padx=10, pady=5, fill=X)

e2 = Entry(root, textvariable=height)
e2.pack(anchor=W, padx=10, pady=5, fill=X)
e2.bind("<Return>", areasize)

b1 = Button(root, text='Calculate', command=areasize)
b1.pack(anchor=W, padx=10, pady=5)

l3 = Label(root, textvariable=areaTotal)
l3.pack(anchor=W, padx=10, pady=10)

root.mainloop()

