from tkinter import *

root = Tk()
root.minsize(200, 200)

base = DoubleVar()
height = DoubleVar()
areaTotal = DoubleVar()


def areasize():
    areaTotal.set(base.get() * height.get())

def set_focus(event):
    e1.focus_set()

l1 = Label(root, text='base')
l1.pack()

e1 = Entry(root, textvariable=base)
e1.bind('<FocusIn>', set_focus)
e1.pack()

l2 = Label(root, text='height')
l2.pack()

e2 = Entry(root, textvariable=height)
e2.pack()

b1 = Button(root, text='Calculate', command=areasize)
b1.pack()

l3 = Label(root, textvariable=areaTotal)
l3.pack()



root.mainloop()
