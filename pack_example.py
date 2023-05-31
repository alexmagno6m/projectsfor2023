from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Login')
root.geometry("350x220")



Label(text='Username:').pack(anchor=W, padx=10, pady=5, fill=X)
Entry().pack(anchor=W, padx=10, pady=5, fill=X)

Label(text='Password:').pack(anchor=W, padx=10, pady=5, fill=X)
Entry(show="*").pack(anchor=W, padx=10, pady=5, fill=X)

Button(text='Login').pack(anchor=W, padx=10, pady=5, side=LEFT)
Button(text="Cancel").pack(anchor=W, padx=10, pady=5, side=LEFT)

root.mainloop()