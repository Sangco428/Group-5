from tkinter import *

window = Tk()
window.title('Label')
window.geometry("400x110+10+30")
lbl1 = Label(window, text="Laboratory Activity 5")
lbl1.place(x=40, y=30)
lbl2 = Label(window, text="Submitted to: Mam Sayo")
lbl2.place(x=30, y=50)
window.mainloop()
