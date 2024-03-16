# 某一種python的UI套件
from tkinter import *

root = Tk()

def click():
    print("Button clicked!")

button = Button(root, text="Click me", command=click)
button.pack()

root.mainloop()


from tkinter import *

root = Tk()

label = Label(root, text="Hello, world!")
label.pack()

root.mainloop()


from tkinter import *

root = Tk()

def show_entry():
    print(entry.get())

entry = Entry(root)
entry.pack()

button = Button(root, text="Show entry", command=show_entry)
button.pack()

root.mainloop()
