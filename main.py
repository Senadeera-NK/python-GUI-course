#importing python tkinter
from tkinter import *
from tkinter.ttk import Combobox

#creating window
window = Tk()

#adding widgets
window.title("Hello python")
window.geometry("600x1000+10+20")

btn = Button(window, text="This is button widget", fg = 'blue')
btn.place(x=80, y=100)

label = Label(window, text="this is label widget", fg='red',font=("Helvetica", 16))
label.place(x=60, y=50)

txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

#dropdown list
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=200)

lb = Listbox(window, height=5, selectmode="multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=60, y=250)

#RADIO button
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=60, y=350)
r2.place(x=60, y=370)

#checkbutton
v1 = IntVar()
v2 = IntVar()
c1 = Checkbutton(window, text="cricket", variable=v1)
c2 = Checkbutton(window, text="tennis", variable=v2)
c1.place(x=200, y=350)
c2.place(x=200, y=370)

#event handling
#bind() method -->> associates an event to a callback function so that, when the event ocurs, the function is called.
#Ex: Widget.bind(event, callback)
#function = MyButtonClicked()
#Ex: btn.bind('<Button-1>', MyButtonClicked)

#command parameter = more convenient than the bind() method
#Ex: btn = Button(widow, text="btn",command=MyEventHandlerFunction)


#adding, minimizing calculator

#function definitions
def addNumbers():
    resultentry.delete(0,'end')
    addnum1= int(num1.get())
    addnum2= int(num2.get())
    addresult = addnum1 + addnum2
    resultentry.insert(END, str(addresult))

def minimizeNumbers():
    resultentry.delete(0, "end")
    mininum1 = int(num1.get())
    mininum2 = int(num2.get())
    miniresult = mininum1 - mininum2
    resultentry.insert(END, str(miniresult))


# add function widgets
lb1 = Label(window, text="number 1")
lb1.place(x=60, y=500)
num1 = Entry(window, text="please enter a number1", bd=5)
num1.place(x=120, y=500)

lb2 = Label(window, text="number 2")
lb2.place(x=60, y=550)
num2 = Entry(window, text="please enter a number2", bd=5)
num2.place(x=120, y=550)

addBtn = Button(window, text="add", fg="blue", command=addNumbers)
addBtn.place(x=300, y=525)

#result widgets
resultentry = Entry(window, bd=5)
resultentry.place(x=330, y=525)

#minimizing function widgets
minimizeBtn = Button(window, text="minimize", fg="blue", command=minimizeNumbers)
minimizeBtn.place(x=300, y=560)

window.mainloop()