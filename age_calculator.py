from tkinter import *
from datetime import date

root = Tk()
root.geometry('280x300')
# vertical and horizontal
root.resizable(False, False)
root.title('Age calculator')
statement = Label(root)


def ageCal():
    global statement
    statement.destroy()
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()),
                     int(dayEntry.get()))
    age = today.year - birthDate.year
    if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
        age -= 1
    statement = Label(text="{}'s age is {}".format(nameValue.get(), age))
    ls = Label(text='Result')
    ls.grid(row=6, column=0, padx=10, pady=10)
    statement.grid(row=6, column=1, pady=15)


l1 = Label(text="name:")
l1.grid(row=1, column=0)
nameValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
nameEntry.grid(row=1, column=1, padx=10, pady=10)
l2 = Label(text="Year: ")
l2.grid(row=2, column=0)
yearValue = StringVar()
yearEntry = Entry(root, textvariable=yearValue)
yearEntry.grid(row=2, column=1, pady=10, padx=10)

l3 = Label(text='Month: ')
l3.grid(row=3, column=0)
monthValue = StringVar()

monthEntry = Entry(root, textvariable=monthValue)
monthEntry.grid(row=3, column=1, padx=10, pady=10)

l4 = Label(text='Day:')
l4.grid(row=4, column=0)
dayValue = StringVar()

dayEntry = Entry(root, textvariable=dayValue)
dayEntry.grid(row=4, column=1, pady=10, padx=10)

button = Button(text='Calculate Age', command=ageCal)
button.grid(column=1, row=5)

root.mainloop()
