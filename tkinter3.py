from tkinter import *

window = Tk()

window.title("Amin Khan")


hello_labal = Label(window,text="Click")
hello_labal.pack()
hello_labal.config(fg="red")

window.geometry("300x400")
window.mainloop()