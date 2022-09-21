
# if statements, conditionals - elagazasok, kondicionalasok - boolean keplet

eletkor = 16

if eletkor < 18: # if csak 1, else is csak 1, elif vegtelen
    if eletkor >= 16:
        print('Egy kis sort megihatsz')
    else:
        print('Se pia,se drogok')
elif eletkor >= 19 and eletkor < 30:
    print('Jo bulizast')
elif eletkor > 30 and eletkor < 65:
    print('Munka es csalad')
else:
    print('Nyugdijas elet, meg unokak')


