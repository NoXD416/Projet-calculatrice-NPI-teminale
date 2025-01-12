from pile import *

#variable global
calcList = []
numToEnter = 0
isDecimal = False
decimalFactor = 0.1
prevCalc = ''
prevAns = 0

#cree les nombre num par num
def inputNum(num):
    global numToEnter
    global decimalFactor
    if not isDecimal:
        numToEnter = numToEnter * 10 + num
    else:
        if decimalFactor >= .001:
            numToEnter += num * decimalFactor
            decimalFactor /= 10
    return numToEnter

#transforme le nombre en decimal avec 3 nombre apre la virgule come maximum
def makeDecimal():
    global isDecimal
    global numToEnter
    if not isDecimal:
        isDecimal = True
        numToEnter += 0.0

#insert le nombre cree dans clacLsit pour ensuite calculer
def enterNum():
    global numToEnter
    global decimalFactor
    global isDecimal

    calcList.append(numToEnter)
    numToEnter = 0
    decimalFactor = 0.1
    isDecimal = False

#ajoute l'opperation donner dans calcList
def enterOperation(op):
    calcList.append(op)

#delete l'objet dernierement inseret dans calcList ou numToEnter si il est present
def delete():
    global numToEnter
    global decimalFactor
    global isDecimal
    if numToEnter != 0:
        numToEnter = 0
        decimalFactor = 0.1
        isDecimal = False
    elif len(calcList) != 0:
        calcList.pop(-1)

#update l'ecrant de la calculatrice
def updateDisplay():
    finale = ''
    for element in calcList:
        finale += str(element) + '  '
    if numToEnter != 0:
        finale += str(numToEnter)
    return finale

#ajoute la reponce precedente a calcList
def addAns():
    calcList.append(prevAns)

#controle la calculation de calcList
def calculate():
    global numToEnter
    global decimalFactor
    global isDecimal
    global calcList
    global prevCalc
    global prevAns

    prevCalc = ''
    for element in calcList:
        prevCalc += str(element) + '  ' #pour afficher le calcule fait presedement

    P = pile()
    n1 = 0
    n2 = 0
    for elem in calcList: 
        if type(elem) == str:
            n1 = Depiler(P)
            n2 = Depiler(P)
            if elem == '+':
                Empiler(P, n2+n1)
            elif elem == '-':
                Empiler(P, n2-n1)
            elif elem == 'x':
                Empiler(P, n2*n1)
            elif elem == '/':
                if n1 == 0:
                    prevCalc = 'Erreur division par un nombre '
                    return
                else:
                    Empiler(P, n2/n1)
            else:
                Empiler(P, n2**n1)
        else:
            Empiler(P, elem)
    
    #reset les variable global
    calcList = []
    numToEnter = 0
    isDecimal = False
    decimalFactor = 0.1
    calcList.append(Depiler(P))
    prevAns = calcList[0]
    return