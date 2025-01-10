from tkinter import *
from PIL import Image, ImageTk

#Function for Pressing Key
def press(key):
    if key == '=':
        try:
            result = eval(screenval.get())
            screenval.set(result)
        except Exception:
            screenval.set("Error")
    elif key == "C":
        screenval.set("")
    else:
        screenval.set(screenval.get() + key)

root = Tk()
root.title("Calculator By Sagar")
root.geometry("300x433")
root.minsize(300,433)
root.maxsize(300,433)

#Icon
img = PhotoImage(file='calculator.png')
root.iconphoto(False, img)

#Entry Field
fr1 = Frame(root, bg="light grey")
fr1.pack()
screenval = StringVar()
screenval.set("")
screen = Entry(fr1, textvariable=screenval, width=30, font="lucida 30 bold", relief=RIDGE, borderwidth=10)
screen.pack(padx=5, pady=5)

#Buttons 
fr2 = Frame(root, bg="light grey")
fr2.pack()
buttons =[
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', 'C',
]
row, col = 0, 0
for btn in buttons:
    Button(fr2, text=btn, font=("Arial", 15), width=5, height=2,bg="white", command=lambda key=btn: press(key))\
          .grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

#For "=" Button
fr3 = Frame(root, bg="light grey")
fr3.pack()
special = Button(fr3, text="=", font=("Arial", 18), width=30, height=2,bg="DodgerBlue3", command=lambda: press('=')).pack(padx=5, pady=5)

root.mainloop()


