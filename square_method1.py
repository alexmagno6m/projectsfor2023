from tkinter import *
from tkinter.ttk import *


root = Tk()
root.minsize(200, 200)

base = StringVar()
height = StringVar()
areaTotal = Label(root)


def areasize():
    global areaTotal
    c = int(e1.get()) * int(e2.get())
    areaTotal = Label(text='the area is {}'.format(c))
    areaTotal.pack()




l1 = Label(root, text='base')
l1.pack(anchor=W, padx=10, pady=5, fill=X)

e1 = Entry(root, textvariable=base)
e1.pack(anchor=W, padx=10, pady=5, fill=X)

l2 = Label(root, text='height')
l2.pack(anchor=W, padx=10, pady=5, fill=X)

e2 = Entry(root, textvariable=height)
e2.pack(anchor=W, padx=10, pady=5, fill=X)

b1 = Button(root, text='Calculate', command=areasize)
b1.pack(anchor=W, padx=10, pady=5)

l3 = Label(root, textvariable=areaTotal)
l3.pack(anchor=W, padx=10, pady=10)



root.mainloop()
