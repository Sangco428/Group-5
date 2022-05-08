from tkinter import *

class Mywindow:
    def __init__(self, win):
        self.lbl1 = Label(window, text="Semestral Grade Calculator", font=("Arial", 16))
        self.lbl1.place(x=25, y=20)

        self.lbl2 = Label(window, text="Prelim Grade")
        self.lbl2.place(x=25, y=70)
        self.Ent1 = Entry(window, bd=2, justify="center")
        self.Ent1.place(x=150, y=70)
        self.Ent1.insert(0, "75")

        self.lbl3 = Label(window, text="Midterm Grade")
        self.lbl3.place(x=25, y=110)
        self.Ent2 = Entry(window, bd=2, justify="center")
        self.Ent2.place(x=150, y=110)
        self.Ent2.insert(0, "75")

        self.lbl4 = Label(window, text="Finals Grade")
        self.lbl4.place(x=25, y=150)
        self.Ent3 = Entry(window, bd=2, justify="center")
        self.Ent3.place(x=150, y=150)
        self.Ent3.insert(0, "75")

        self.lbl5 = Label(window, text="Semestral Grade")
        self.lbl5.place(x=25, y=190)
        self.Ent4 = Entry(window, bd=2, justify="center")
        self.Ent4.place(x=150, y=190)
        self.Ent4.insert(0, "75")

        self.bttn = Button(window, text="Compute Semestral Grade", width="35", bg="#BBF0F0", command=self.compute)
        self.bttn.place(x=25, y=230)

    def compute(self):
        pre = float(self.Ent1.get())
        mid = float(self.Ent2.get())
        fin = float(self.Ent3.get())
        grade = pre*.3 + mid*.3 + fin*.4
        self.Ent4.delete(0, 'end')
        self.Ent4.insert(0, grade)

window = Tk()
mywin = Mywindow(window)
window.geometry("320x300+20+50")
window.title("Semestral Grade Calculator")


window.mainloop()