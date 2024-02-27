from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Login')
root.geometry("300x220")
style = Style()
style.configure('TLabel', font=('Arial', 11), foreground="red")
style.configure('Custom.TButton', font=('Arial', 12), background="red", foreground="blue")


Label(text='Username:').pack(anchor=W, padx=10, pady=5, fill=X)
Entry().pack(anchor=W, padx=10, pady=5, fill=X)

Label(text='Password:').pack(anchor=W, padx=10, pady=5, fill=X)
Entry(show="*").pack(anchor=W, padx=10, pady=5, fill=X)

Button(text='Login', style='Custom.TButton').pack(anchor=W, padx=10, pady=5, side=LEFT)
Button(text="Cancel", command=root.destroy).pack(anchor=W, padx=10, pady=5, side=LEFT)
'''
frame = Frame(root)
frame.pack(anchor=SE, padx=10, pady=5)
#evita que se ajuste la ventana al tamno del contenido
frame.pack_propagate(0)


Label(frame, text='Design by: Alexander Acevedo').pack(side=RIGHT)
'''
Label(text='Design by: Alexander Acevedo').place(anchor=SE, relx=1, rely=1, x=-10, y=-10)


root.mainloop()

