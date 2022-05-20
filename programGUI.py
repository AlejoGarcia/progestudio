
from tkinter import *

window = Tk()

label1 = Label(window, text = "Select an action:", font=("Helvetica", 16))
label1.place(x = 70, y = 50)
bttn_open = Button(window, text = "Open", fg = 'blue')
bttn_open.place(x = 80, y = 80)
bttn_create = Button(window, text = "Create", fg = 'blue')
bttn_create.place(x = 160, y = 80)
window.title("Hello tkinter")
window.geometry("300x200+10+10")


window.mainloop()

