from tkinter import *

window = Tk()
window.title("αριθμομηχανη")
window.geometry("300x300")

box1 = Entry(window)
box1.place(x=10, y=10)

box2 = Entry(window)
box2.place(x=10, y=40)

lbl1 = Label(window, text="αριθμος 1")
lbl1.place(x=140, y=10)

lbl2 = Label(window, text="αριθμος 2")
lbl2.place(x=140, y=40)

lbl3 = Label(window, text="αποτελεσμα")
lbl3.place(x=10, y=150)

def prosthesi():
    n1 = float(box1.get())
    n2 = float(box2.get())
    apotelesma = n1 + n2
    lbl3.configure(text=str(apotelesma))

def afairesi():
    n1 = float(box1.get())
    n2 = float(box2.get())
    apotelesma = n1 - n2
    lbl3.configure(text=str(apotelesma))

def pollaplasiasmos():
    n1 = float(box1.get())
    n2 = float(box2.get())
    apotelesma = n1 * n2
    lbl3.configure(text=str(apotelesma))

def diairesi():
    n1 = float(box1.get())
    n2 = float(box2.get())
    apotelesma = n1 / n2
    lbl3.configure(text=str(apotelesma))

btn1 = Button(window, text="+", command=prosthesi)
btn1.place(x=10, y=80)

btn2 = Button(window, text="-", command=afairesi)
btn2.place(x=40, y=80)

btn3 = Button(window, text="*", command=pollaplasiasmos)
btn3.place(x=70, y=80)

btn4 = Button(window, text="/", command=diairesi)
btn4.place(x=100, y=80)

window.mainloop()