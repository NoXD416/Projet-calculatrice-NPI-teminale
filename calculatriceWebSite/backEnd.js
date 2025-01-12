//variable
let calcList = [];
let numToEnter = 0;
let isDecimal = false;
let decimalFactor = 0.1;
let prevCalc = '';
let prevAns = 0;

//cree les nombre num par num
function inputNum(num) {
    if (!isDecimal) {
        numToEnter = numToEnter * 10 + num;
    } else {
        if (decimalFactor >= 0.001) {
            numToEnter += num * decimalFactor;
            decimalFactor /= 10;
        }
    }
    updateDisplay();
}

//transforme le nombre en decimal avec 3 nombre apre la virgule come maximum
function makeDecimal() {
    if (!isDecimal) {
        isDecimal = true;
    }
    updateDisplay();
}

//insert le nombre cree dans clacLsit pour ensuite calculer
function enterNum() {
    calcList.push(numToEnter);
    numToEnter = 0;
    decimalFactor = 0.1;
    isDecimal = false;
    updateDisplay();
}

//ajoute l'opperation donner dans calcList
function enterOperation(op) {
    calcList.push(op);
    updateDisplay();
}

//delete l'objet dernierement inseret dans calcList ou numToEnter si il est present
function deleteLast() {
    if (numToEnter !== 0) {
        numToEnter = 0;
        decimalFactor = 0.1;
        isDecimal = false;
    } else if (calcList.length > 0) {
        calcList.pop();
    }
    updateDisplay();
}

//ajoute la reponce precedente a calcList
function addAns() {
    calcList.push(prevAns);
    updateDisplay();
}

//controle la calculation de calcList
function calculate() {
    prevCalc = calcList.join(' ');
    const stack = [];

    calcList.forEach(elem => {
        if (typeof elem === 'number') {
            stack.push(elem);
        } else {
            const n1 = stack.pop();
            const n2 = stack.pop();
            let result;
            switch (elem) {
                case '+':
                    result = n2 + n1;
                    break;
                case '-':
                    result = n2 - n1;
                    break;
                case 'x':
                    result = n2 * n1;
                    break;
                case '/':
                    if (n1 === 0) {
                        result = 'Erreur division par 0';
                    } else {
                        result = n2 / n1;
                    }
                    break;
                case '^':
                    result = Math.pow(n2, n1);
                    break;
                default:
                    result = 0;
            }
            stack.push(result);
        }
    });

    const result = stack.pop();
    calcList = [result];
    prevAns = result;
    updateDisplay(true);
}

//update l'ecrant de la calculatrice
function updateDisplay(showPrev = false) {
    const prevDisplay = document.getElementById('prevCalc');
    const currentDisplay = document.getElementById('currentCalc');

    if (showPrev) {
        prevDisplay.textContent = `${prevCalc} = ${prevAns}`;
    }

    currentDisplay.textContent = calcList.join(' ') + ' ' + (numToEnter !== 0 ? numToEnter : '');
}