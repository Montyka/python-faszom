# https://docs.python.org/3/library/functions.html

print(abs(-78))

nevek = ['Jancsi', 'Joci', 'Bence', 'Petike', 'Ferko']

for index, nev in enumerate(nevek): #Elemek megszamozasa, index valtozo a szamot adja vissza
    print(index,nev)


print(float('141.876')) #at castolja floatra az egesz szamot, de azt is ha stringket adod meg

print(hex(125)) #vissza adja a hexadecimalis erteket

print(int(24.78)) #Ugyan az mint a float, csak egesz szamra

print(len(nevek)) #hosszusag

print(len('hello, hogy vagy')) #ugyan az mint felette levo

print(max(7, 5, 12, 45, 77, 192)) #kivalassza legnagyobb erteket, azt irja ki

print(min(7, 5, 12, 45, 77, 192)) # fenti ellenkezoje

print(pow(2, 10)) #hatvanyozast

print(list(range(50, 100, 2))) #list, listaba rakas, range adott szamtol-szamig, kettes az pedig stepsize, kettesevel fog emelkedni

print(list(reversed(nevek))) #vissza fele irja ki adott parametert

print(round(12.567313, 2)) #kerekites, 2-es azt jelenti mennyi tizedes jegyig kerekitse

