from tkinter import *
from tkinter.ttk import *
root = Tk()
root.minsize(width=300, height=200)

base = DoubleVar(value="")
height = DoubleVar(value="")
areaTotal = DoubleVar()


def areasize(event=None):
    areaTotal.set(base.get() * height.get())

def set_focus(event):
    e1.focus_set()

l1 = Label(root, text='base')
l1.pack(anchor=W, padx=10, pady=5)

e1 = Entry(root, textvariable=base)
e1.pack(padx=10, pady=5, fill=X)
e1.focus_set()

l2 = Label(root, text='height')
l2.pack( padx=10, pady=5, fill=X)

e2 = Entry(root, textvariable=height)
e2.pack( padx=10, pady=5, fill=X)
e2.bind("<Return>", areasize)

b1 = Button(root, text='Calculate', command=areasize)
b1.pack(anchor=W, padx=10, pady=5, fill=X)

l3 = Label(root, textvariable=areaTotal)
l3.pack(anchor=W, padx=10, pady=5, fill=X)



root.mainloop()
