nevek1 = ['Xena', 'Bozsi', 'Eniko', 'Ildi', 'Zsuzsi', 'Evi', 10, True]
nevek2 = ['Jancsi', 'Joci', 'Bence', 'Petike', 'Ferko']

#for nev in nevek1:
#    print(nev)

#for nev in nevek2:
#    print(nev)

def nev_printer(nev_lista): # fugveny #Minden ami ez alatt van az a fugveny testet kepezi aka indentation
    for nev in nev_lista:
        if isinstance(nev, str): #megkerdezi hogy a listaban talahato adat az string-e
            print(nev.upper())  # .upper az mindent nagy betuvel fogja kiirni, csak stringeken
        else:
            print('nem string type, hanem: ' + str(type(nev))) #string osszefuzes, kurvara nem tudom mit csinal

nev_printer(nevek1) # fugveny meghivas
nev_printer(nevek2)