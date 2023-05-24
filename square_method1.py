import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.minsize(200, 200)

base = tk.StringVar()
height = tk.StringVar()
areaTotal = tk.Label(root)


def areasize():
    global areaTotal
    c = int(e1.get()) * int(e2.get())
    areaTotal = tk.Label(text='the area is {}'.format(c))
    areaTotal.pack()




l1 = tk.Label(root, text='base')
l1.pack(anchor=tk.W, padx=10, pady=10, fill=tk.X)

e1 = tk.Entry(root, textvariable=base)
e1.pack(anchor=tk.W, padx=10, pady=10, fill=tk.X)

l2 = tk.Label(root, text='height')
l2.pack(anchor=tk.W, padx=10, pady=10, fill=tk.X)

e2 = tk.Entry(root, textvariable=height)
e2.pack(anchor=tk.W, padx=10, pady=10, fill=tk.X)

b1 = tk.Button(root, text='Calculate', command=areasize)
b1.pack(anchor=tk.W, padx=10, pady=5)

l3 = tk.Label(root, textvariable=areaTotal)
l3.pack(anchor=tk.W, padx=10, pady=10)



root.mainloop()
