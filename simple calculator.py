from tkinter import *
from functools import partial

#creating window
window = Tk()

#window's title
window.title("simple calculator")
#window's width & height + x length + y height
window.geometry("280x400+400+20")

#display
displayEntry = Entry(window, text="display", bg="white", width=7, borderwidth=1, relief="solid", font=("Arial",50))
displayEntry.place(x=8, y=8)

#functions
#symbols that user adds to display
displaySymbolsList = []

def btnClicked(number):
     displayEntry.insert(END, number)
     displaySymbolsList.append(number)
     print(displaySymbolsList)

def btnFunctionDelete():
    displayEntry.delete(0, "end")
    displaySymbolsList.clear()

def btnFunctionResult():
    displayEntry.delete(0, "end")
    symbolList = ['+','-','x','/']
    firstNumber = ""
    secondNumber = ""
    symbolindex = ""
    symbolFromList = ""
    resultNumber = 0

    lenl1 = len(displaySymbolsList)

    #getting the first number to the variable
    x = 0
    while x < lenl1:
        if displaySymbolsList[x] not in symbolList:
            firstNumber = firstNumber + displaySymbolsList[x]
        else:
            symbolindex = x
            symbolFromList = displaySymbolsList[symbolindex]
            break
        x=x+1

    #getting the second number to the variable
    y = symbolindex + 1
    while y <lenl1:
        secondNumber = secondNumber + displaySymbolsList[y]
        y= y+1

    print(firstNumber)
    print(secondNumber)
    if symbolFromList == "+":
        resultNumber = int(firstNumber) + int(secondNumber)
    if symbolFromList == "-":
        resultNumber = int(firstNumber) - int(secondNumber)
    if symbolFromList == "x":
        resultNumber = int(firstNumber) * int(secondNumber)
    if symbolFromList == "/":
        resultNumber = int(firstNumber) / int(secondNumber)

    print(resultNumber)
    #displaying the result on the entryfield
    displayEntry.insert(END, str(resultNumber))


#canvas all the button exists on the calculator
canvas = Canvas(window, bg="grey", width=250, height= 242, borderwidth=1, relief="solid")
canvas.place(x=10, y=100)

#all numbers buttons
btn1 = Button(canvas, width=5, height=2, text="1", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "1"))
btn1.place(x=3, y=3)
#space between near x's -> 62
btn2 = Button(canvas, width=5, height=2, text="2", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "2"))
btn2.place(x=65, y=3)

btn3 = Button(canvas, width=5, height=2, text="3", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "3"))
btn3.place(x=127, y=3)

#space between near y's -> 60
btn4 = Button(canvas, width=5, height=2, text="4", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "4"))
btn4.place(x=3, y=63)

btn5 = Button(canvas, width=5, height=2, text="5", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "5"))
btn5.place(x=65, y=63)

btn6 = Button(canvas, width=5, height=2, text="6", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "6"))
btn6.place(x=127, y=63)

btn7 = Button(canvas, width=5, height=2, text="7", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "7"))
btn7.place(x=3, y=123)

btn8 = Button(canvas, width=5, height=2, text="8", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "8"))
btn8.place(x=65, y=123)

btn9 = Button(canvas, width=5, height=2, text="9", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "9"))
btn9.place(x=127, y=123)

btn0 = Button(canvas, width=5, height=2, text="0", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "0"))
btn0.place(x=65, y=183)

#mathematical functions
btnAdd = Button(canvas, width=5, height=2, text="+", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "+"))
btnAdd.place(x=189, y=3)

btnMini = Button(canvas, width=5, height=2, text="-", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "-"))
btnMini.place(x=189, y=63)

btnMultiple = Button(canvas, width=5, height=2, text="x", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "x"))
btnMultiple.place(x=189, y=123)

btnEqual = Button(canvas, width=5, height=2, text="=", font=("Arial", 15), borderwidth=1, relief="solid", command = (btnFunctionResult))
btnEqual.place(x=127, y=183)

btnDivide = Button(canvas, width=5, height=2, text="/", font=("Arial", 15), borderwidth=1, relief="solid", command = partial(btnClicked, "/"))
btnDivide.place(x=189, y=183)

#delete
btnDelete = Button(canvas, width=5, height=2, text="C", font=("Arial", 15), borderwidth=1, relief="solid", command = (btnFunctionDelete))
btnDelete.place(x=3, y=183)


window.mainloop()