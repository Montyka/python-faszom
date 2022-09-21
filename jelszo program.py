jelszo = 'Jancsi'
bemenet = input('Mi a jelszo? ')
proba = 0

while bemenet != jelszo: #!= - nem egyenlo
    proba += 1
    if proba == 3:
        print('Hozzaferes Megtagadva!')
        break
    print('Rossz jelszo! ')
    bemenet = input('Mi a jelszo? ')

if bemenet == jelszo:
    print('Hozzaferes megadva!')

