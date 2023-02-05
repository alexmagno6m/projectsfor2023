from tkinter import *

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
l1.pack()

e1 = Entry(root, textvariable=base)
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
