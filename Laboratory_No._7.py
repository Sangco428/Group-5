from tkinter import *

class Mywindow:
    def __init__(self, win):
        self.scr = Text(bd=20, width=47, height=3)
        self.scr.grid(row=0, column=0, columnspan=12)
        self.clr = Button(text="C", width=52, height=3)
        self.clr.grid(row=1, column=0, columnspan=12)
        #top row
        self.no7 = Button(text="7", width=12, height=3)
        self.no7.grid(row=2, column=0, columnspan=3)
        self.no8 = Button(text="8", width=12, height=3)
        self.no8.grid(row=2, column=3, columnspan=3)
        self.no9 = Button(text="9", width=12, height=3)
        self.no9.grid(row=2, column=6, columnspan=3)
        self.div = Button(text="/", width=12, height=3)
        self.div.grid(row=2, column=9, columnspan=3)
        #middle row
        self.no4 = Button(text="4", width=12, height=3)
        self.no4.grid(row=3, column=0, columnspan=3)
        self.no5 = Button(text="5", width=12, height=3)
        self.no5.grid(row=3, column=3, columnspan=3)
        self.no6 = Button(text="6", width=12, height=3)
        self.no6.grid(row=3, column=6, columnspan=3)
        self.mul = Button(text="*", width=12, height=3)
        self.mul.grid(row=3, column=9, columnspan=3)
        #bottom row
        self.no4 = Button(text="1", width=12, height=3)
        self.no4.grid(row=4, column=0, columnspan=3)
        self.no5 = Button(text="2", width=12, height=3)
        self.no5.grid(row=4, column=3, columnspan=3)
        self.no6 = Button(text="3", width=12, height=3)
        self.no6.grid(row=4, column=6, columnspan=3)
        self.min = Button(text="-", width=12, height=3)
        self.min.grid(row=4, column=9, columnspan=3)
        #0, decimal point and plus
        self.no0 = Button(text="0", width=16, height=3)
        self.no0.grid(row=5, column=0, columnspan=4)
        self.dec = Button(text=".", width=16, height=3)
        self.dec.grid(row=5, column=4, columnspan=4)
        self.plu = Button(text="+", width=16, height=3)
        self.plu.grid(row=5, column=8, columnspan=4)
        #equal sign
        self.clr = Button(text="=", width=52, height=3)
        self.clr.grid(row=6, column=0, columnspan=12)

window = Tk()
mywin = Mywindow(window)
window.geometry("380x420+20+50")
window.title("Calculator")


window.mainloop()
