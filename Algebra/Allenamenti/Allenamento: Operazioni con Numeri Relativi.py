# Creato da Marco Sisto - 28/11/2020

import random
import operator
import time

print(' ')
print('Benvenuto/a all\'allenamento con moltiplicazioni con numeri relativi.\n')
diff = input('Seleziona una Difficoltà: (Facile, Medio, Difficile) >>> ')
print('Pronti, Partenza, Via!')
time.sleep(0.5)
print(' ')

def operazione():
    segnimat = {'+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.truediv}
    if diff == 'Facile':
        num1 = random.randint(-10,10)
        num2 = random.randint(-10,10)
    elif diff == 'Medio':
        num1 = random.randint(-20,20)
        num2 = random.randint(-20,20)
    elif diff == 'Difficile':
        num1 = random.randint(-30,30)
        num2 = random.randint(-30,30)
    segno = random.choice(list(segnimat.keys()))
    risposta = segnimat.get(segno)(num1,num2)
    print('({}) {} ({})\n'.format(num1, segno, num2))
    return risposta

def domanda():
    risposta = operazione()
    risputente = float(input())
    return risputente == risposta

def main():
    punteggio = 0
    if diff == 'Facile':
        for i in range(10):
            rispgiusta = domanda()
            if rispgiusta:
                punteggio += 1
                print('Giusto!\n')
            else:
                print('Sbagliato!\n')
        print('Punteggio: {}/30'.format(punteggio))
    elif diff == 'Medio':
        for i in range(20):
            rispgiusta = domanda()
            if rispgiusta:
                punteggio += 1
                print('Giusto!\n')
            else:
                print('Sbagliato!\n')
        print('Punteggio: {}/30'.format(punteggio))
    elif diff == 'Difficile':
        for i in range(30):
            rispgiusta = domanda()
            if rispgiusta:
                punteggio += 1
                print('Giusto!\n')
            else:
                print('Sbagliato!\n')
        print('Punteggio: {}/30'.format(punteggio))
main()
