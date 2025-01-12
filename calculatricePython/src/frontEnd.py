from tkinter import *
import tkinter as tk
import backEnd

#operation pour Tkinter
Calculatrice = Tk()
Calculatrice.title("Calculatrice")
Calculatrice.minsize(538, 515)
Calculatrice.maxsize(538, 515)
Calculatrice.geometry("200x300")
Calculatrice.configure(bg="black")

#opperation pour l'ecran de la calculatrice
ansScreen = tk.Label(Calculatrice, text='', fg='Gray', font=("Comic Sans", 13), bg="black", height=2, anchor='e')
CalcScreen = tk.Label(Calculatrice, text='', fg='White', font=("Comic Sans", 15), bg="black", height=1, anchor='e')
ansScreen.pack(side=tk.TOP, fill=tk.X)
CalcScreen.pack(side=tk.TOP, fill=tk.X)

#fonction pour renouveler l'ecran
def display(upAns):
    if upAns == True:
        toDesplay = backEnd.prevCalc + '=  ' + str(backEnd.prevAns)
        ansScreen.config(text = toDesplay)
    current_display = backEnd.updateDisplay()
    CalcScreen.config(text = current_display)
    
#fonction relier ou fonction du script backEnd
def frontInputNum(num):
    backEnd.inputNum(num)
    display(False)

def frontMakeDecimal():
    backEnd.makeDecimal()
    display(False)

def frontEnterNum():
    backEnd.enterNum()
    display(False)

def frontDelete():
    backEnd.delete()
    display(False)
    
def frontEnterOperation(op):
    backEnd.enterOperation(op)
    display(False)

def frontAddAns():
    backEnd.addAns()
    display(False)

def equalOp():
    backEnd.calculate()
    display(True)

#opperation button
plusButton = tk.Button(Calculatrice, command=lambda: frontEnterOperation('+'), text='+', bg='lightgray', width=14, height=6, background="orange")
minusButton = tk.Button(Calculatrice, command=lambda: frontEnterOperation('-'), text='-', bg='lightgray', width=14, height=6, background="orange")
timesButton = tk.Button(Calculatrice, command=lambda: frontEnterOperation('x'), text='x', bg='lightgray', width=14, height=6, background="orange")
divButton = tk.Button(Calculatrice, command=lambda: frontEnterOperation('/'), text='/', bg='lightgray', width=14, height=6, background="orange")
expButton = tk.Button(Calculatrice, command=lambda: frontEnterOperation('^'), text='^', bg='lightgray', width=14, height=6, background="orange")

#numero 1, 2, 3
oneButton = tk.Button(Calculatrice, command=lambda: frontInputNum(1), text='1', bg='lightgray', width=14, height=6, background="gray")
twoButton = tk.Button(Calculatrice, command=lambda: frontInputNum(2), text='2', bg='lightgray', width=14, height=6, background="gray")
threeButton = tk.Button(Calculatrice, command=lambda: frontInputNum(3), text='3', bg='lightgray', width=14, height=6, background="gray")

#numero 4, 5, 6
fourButton = tk.Button(Calculatrice, command=lambda: frontInputNum(4), text='4', bg='lightgray', width=14, height=6, background="gray")
fiveButton = tk.Button(Calculatrice, command=lambda: frontInputNum(5), text='5', bg='lightgray', width=14, height=6, background="gray")
sixButton = tk.Button(Calculatrice, command=lambda: frontInputNum(6), text='6', bg='lightgray', width=14, height=6, background="gray")

#numero 7, 8, 9
sevenButton = tk.Button(Calculatrice, command=lambda: frontInputNum(7), text='7', bg='lightgray', width=14, height=6, background="gray")
eightButton = tk.Button(Calculatrice, command=lambda: frontInputNum(8), text='8', bg='lightgray', width=14, height=6, background="gray")
nineButton = tk.Button(Calculatrice, command=lambda: frontInputNum(9), text='9', bg='lightgray', width=14, height=6, background="gray")

#right side button
delButton = tk.Button(Calculatrice, command=lambda: frontDelete(), text='DELETE', bg='lightgray', width=14, height=6, background="orange")
equalButton = tk.Button(Calculatrice, command=lambda: equalOp(), text='=', bg='lightgray', width=14, height=6, background="orange")
enterButton = tk.Button(Calculatrice, command=lambda: frontEnterNum(), text='ENTER', bg='lightgray', width=14, height=6, background="orange")

#left side button
dotButton = tk.Button(Calculatrice, command=lambda: frontMakeDecimal(), text=',', bg='lightgray', width=14, height=6, background="gray")
zeroButton = tk.Button(Calculatrice, command=lambda: frontInputNum(0), text='0', bg='lightgray', width=14, height=6, background="gray")
ansButton = tk.Button(Calculatrice, command=lambda: frontAddAns(), text='ANS', bg='lightgray', width=14, height=6, background="light blue")

#place operation buttons
plusButton.place(x=0, y=111)
plusButton.lift()
minusButton.place(x=107, y=111)
timesButton.place(x=215, y=111)
divButton.place(x=323, y=111)
expButton.place(x=431, y=111)

#place number buttons
zeroButton.place(x=0, y=414)
oneButton.place(x=107, y=212)
twoButton.place(x=215, y=212)
threeButton.place(x=323, y=212)
fourButton.place(x=107, y=313)
fiveButton.place(x=215, y=313)
sixButton.place(x=323, y=313)
sevenButton.place(x=107, y=414)
eightButton.place(x=215, y=414)
nineButton.place(x=323, y=414)

#plae function buttons
equalButton.place(x=431, y=414)
enterButton.place(x=431, y=313)
dotButton.place(x=0, y=313)
delButton.place(x=431, y=212)
ansButton.place(x=0, y=212)