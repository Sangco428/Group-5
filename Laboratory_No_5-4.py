from tkinter import *

def ChangeColor(): bttn1.configure(bg="yellow")

window = Tk()
window.title('Button')
window.geometry("350x150+10+30")
bttn1 = Button(window, text="color", bg="blue", fg="red", command=ChangeColor)
bttn1.place(x=30, y=90)
bttn2 = Button(window, text="<--- click to change the color of the button")
bttn2.place(x=90, y=90)
window.mainloop()
