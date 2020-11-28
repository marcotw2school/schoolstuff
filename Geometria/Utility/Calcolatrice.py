# Creato da Marco Sisto - 28/11/2020


# finput = FiguraInput
# minput = MainInput

import math

def rettangolo_parallelogrammo():
    finput = input('Cosa vuoi calcolare?: ')
    if finput == 'Area':
        base = int(input('Inserisci la Base: '))
        altezza = int(input('Inserisci l''Altezza: '))
        area = base * altezza
        print('Area = ' + str(area))
    elif finput == 'Perimetro':
        base = int(input('Inserisci la Base: '))
        altezza = int(input('Inserisci l''Altezza: '))
        perimetro = 2*base + 2*altezza
        print('Base*2 = ' + str(base*2), 'Altezza*2 = ' + str(altezza*2), 'Perimetro = ' + str(perimetro))
    elif finput == 'Diagonale':
        base = int(input('Inserisci la Base: '))
        altezza = int(input('Inserisci l''Altezza: '))
        diagonale = math.sqrt(base**2 + altezza**2)
        print('Base^2 = ' + str(base**2) ,'Altezza^2 = ' + str(altezza**2),'Diagonale = ' + str(diagonale))
    elif finput == 'Formule Inverse':
        finput = input('Che formula inversa vuoi calcolare?: ')
        if finput == 'Base':
            area = int(input('Inserisci l''Area: '))
            altezza = int(input('Inserisci l''Altezza: '))
            base = area//altezza
            print(base)
        elif finput == 'Altezza':
            area = int(input('Inserisci l''Area: '))
            base = int(input('Inserisci la Base: '))
            altezza = area//base
            print(altezza)

def quadrato():
    finput = input('Cosa vuoi calcolare?: ')
    if finput == 'Area':
        lato = int(input('Inserisci il lato: '))
        area = lato**2
        print('Area/Lato^2 = ' + str(area))
    elif finput == 'Perimetro':
        lato = int(input('Inserisci il lato: '))
        perimetro = lato*4
        print('Perimetro/Lato*4 = ' + str(perimetro))
    elif finput == 'Diagonale':
        lato = int(input('Inserisci il lato: '))
        diagonale = lato * math.sqrt(2)
        print('Diagonale = ' + str(diagonale))
    elif finput == 'Formule Inverse':
        print('Che formula inversa vuoi calcolare?:')
        finput = input('LatoConArea = 1, LatoConDiagonale = 2')
        if finput == '1':
            area = int(input('Inserisci l''Area: '))
            lato = math.sqrt(area)
            print('Lato = ' + str(lato))
        elif finput == '2':
            diagonale = int(input('Inserisci la Diagonale: '))
            lato = diagonale//math.sqrt(2)
            print('Lato = ' + str(lato))

def triangolo():
    finput = input('Cosa vuoi calcolare?: ')
    if finput == 'Area':
        base = int(input('Inserisci la Base: '))
        altezza = int(input('Inserisci l''Altezza: '))
        area = (base * altezza)//2
        print('Area = ' + str(area))
    elif finput == 'Formule Inverse':
        print('Che formula inversa vuoi calcolare?:')
        finput = input('Base = 1, Altezza = 2, Formula di Erone (Area) = 3: ')
        if finput == '1':
            area = int(input('Inserisci l''Area: '))
            altezza = int(input('Inserisci l''Altezza: '))
            base = (2*area)//altezza
            print('Base = ' + int(base))
        elif finput == '2':
            area = int(input('Inserisci l''Area: '))
            base = int(input('Inserisci la Base: '))
            altezza = (2*area)//base
            print('Altezza = ' + str(altezza))
        elif finput == '3':
            semiperimetro = int(input('Inserisci il semiperimetro: '))
            a = int(input('Inserisci a: '))
            b = int(input('Inserisci b: '))
            c = int(input('Inserisci a: '))
            area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))
            print('Area = ' + str(area))

def triangolo_rettangolo():
    finput = input('Cosa vuoi calcolare?: ')
    if finput == 'Area':
        print('Che formula vuoi usare?: ')
        finput = input('AreaConBase = 1, AreaConIpotenusa = 2: ')
        if finput == '1':
            base = int(input('Inserisci il Cateto: '))
            altezza = int(input('Inserisci l''Altezza: '))
            area = (base * altezza)//2
            print('Area = ' + str(area))
        elif finput == '2':
            ipotenusa = int(input('Inserisci l''Ipotenusa: '))
            latobliquo = int(input('Inserisci il Lato Obliquo: '))
            area = (ipotenusa * latobliquo)//2
            print('Area = ' + str(area))
    elif finput == 'Perimetro':
        ipotenusa = int(input('Inserisci l''Ipotenusa: '))
        c1 = int(input('Inserisci il Cateto 1: '))
        c2 = int(input('Inserisci il Cateto 2: '))
        perimetro = ipotenusa + c1 + c2
        print('Perimetro = ' + str(perimetro))

def main():
    minput = input('Che figura vuoi calcolare?: ')
    if minput == 'Rettangolo':
        rettangolo()
    elif minput == 'Quadrato':
        quadrato()
    elif minput == 'Triangolo':
        triangolo()
    elif minput == 'Triangolo Rettangolo':
        triangolo_rettangolo()

main()

    
