from tkinter import *

#creating window
window = Tk()

#window's title
window.title("simple calculator")
#window's width & height + x length + y height
window.geometry("500x600+400+20")

#display
displayLabel = Label(window, text="display", bg="white", anchor="w", width=12, borderwidth=1, relief="solid", font=("Arial",50))
displayLabel.place(x=10, y=8)

#canvas all the button exists on the calculator
canvas = Canvas(window, bg="grey", width=470, height= 480, borderwidth=1, relief="solid")
canvas.place(x=10, y=100)

#functions
#functions
def btnClicked(number):
     displayLabel['text'] = number

#all numbers buttons
btn1 = Button(canvas, width=5, height=2, text="1", font=("Arial", 15), borderwidth=1, relief="solid", command=btnClicked(1))
btn1.place(x=3, y=3)

btn1 = Button(canvas, width=5, height=2, text="2", font=("Arial", 15), borderwidth=1, relief="solid", command=btnClicked(1))
btn1.place(x=65, y=3)

btn1 = Button(canvas, width=5, height=2, text="3", font=("Arial", 15), borderwidth=1, relief="solid", command=btnClicked(1))
btn1.place(x=127, y=3)

btn1 = Button(canvas, width=5, height=2, text="4", font=("Arial", 15), borderwidth=1, relief="solid", command=btnClicked(1))
btn1.place(x=189, y=3)

window.mainloop()