from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Major Subjects')
window.geometry("300x120+10+30")
data = "reading", "writing", "arithmetic", "coding"
lstbx = Listbox(window, height=5,selectmode="multiple")
for num in data:
    lstbx.insert(END, num)
lstbx.place(x=60,y=10)
window.mainloop()
