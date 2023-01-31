import tkinter
from tkinter import *
import math

# import tkinter,Tkinter is the standard GUI library for Python.
# Python when combined with Tkinter provides a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.


def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'DEL':      # In this try block ,check all the buttton for its working procedure.
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'AC':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError: # exception handle work for if the try is not working.
        pass



def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l




root = Tk()
root.title('Scientific Calculator')
root.config(bg='#6E7B8B')
root.geometry('582x530+100+100')

logoImage = PhotoImage(file='logo.png') # logo for the calculator
logoLabel = Label(root, image=logoImage, bg='#6E7B8B')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 25, 'bold'), bg='#458B74', fg='white', bd=10, relief=SUNKEN, width=20) # calculator display settings
entryField.grid(row=0, column=0, columnspan=6,pady=7)


button_text_list = ["DEL", "AC", "√", chr(8731), "x\u02b8","x\u00B3","x\u00B2","sinθ","cosθ","tanθ",
                    "sinh", "cosh", "tanh","rad", "e", "+", "deg", "2π",
                    "7", "8","9","-","log₁₀", "π",
                    "4", "5", "6","*", "ln", "%", "1", "2",
                    "3", chr(247), "(", ")", ".","0" ,"="]   # All  buttons are named here.





rowvalue = 1
columnvalue = 0
for i in button_text_list:  # decorating all the buttons
    if(i=='DEL' or i=='AC'):
            button = Button(root, width=5, height=1, bd=5, relief=SUNKEN, text=i, bg='#FF7F00', fg='white',
                        font=('arial', 18, 'bold'), activebackground='#1A1A1A',activeforeground='#FF6103', command=lambda button=i: click(button))
            button.grid(row=rowvalue, column=columnvalue, pady=3,padx=3)
    elif (i == '='):
            button = Button(root, width=16, height=1, bd=5, relief=SUNKEN, text=i, bg='#FF7F00', fg='white',
                        font=('arial', 18, 'bold'), activebackground='#1A1A1A',activeforeground='#FF6103', command=lambda button=i: click(button)).place(x=305,y=455)
    elif (i == '0'):
            button = Button(root, width=11, height=1, bd=5, relief=SUNKEN, text=i, bg='#212121', fg='white',
                        font=('arial', 18, 'bold'), activebackground='#1A1A1A',activeforeground='#FF6103', command=lambda button=i: click(button)).place(x=103,y=455)

    else:
        button = Button(root, width=5, height=1, bd=5, relief=SUNKEN, text=i, bg='#212121', fg='white',
                        font=('arial', 18, 'bold'), activebackground='#1A1A1A',activeforeground='#FF6103', command=lambda button=i: click(button))
        button.grid(row=rowvalue, column=columnvalue, pady=3,padx=3)


    columnvalue += 1
    if columnvalue > 5:
        rowvalue += 1
        columnvalue = 0




root.mainloop()
