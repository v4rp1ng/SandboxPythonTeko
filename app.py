while True:
    try:
        zahl1 = int(input('Bitte erste Zahl eingeben: '))
        operator = input('Bitte Operator eingeben: ')
        zahl2 = int(input('Bitte zweite Zahl eingeben: '))
        break
    except:
        print('Es dürfen nur Zahlen eingegeben werden.')
        continue

if operator == '+':
    ergebnis = zahl1 + zahl2
elif operator == '-':
    ergebnis = zahl1 - zahl2
elif operator == '*':
    ergebnis = zahl1 * zahl2
elif operator == '/':
    if zahl2 == 0:
        ergebnis = 'Error: Division durch Null nicht möglich.'
    else:
        ergebnis = zahl1 / zahl2

print('Das Ergebnis ist:', ergebnis)



