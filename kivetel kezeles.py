#
# # exception handling error handling - kivetelkezeles (hibakezeles)
#
# lista = [1,2,3]
#
#
#
# try:
#     print(bla)
#     #print(lista[5])
#     #print(1/0)
# except NameError as e:
#     print(e, ' - Nem letezo valtozo')
# except IndexError as e:
#     print(e, '- Tartomanyon kivuli index')
# except ZeroDivisionError as e:
#     print(e, '- Nullaval osztas')
#
# print('A program vege! ')
#


# lista = ['1', '2', '3', None, '4', '', True, 'Bozsi', '12.64']
#
# for i in lista:
#     try:
#         print(int(i)*2)
#     except:
#         continue
#
#
# print(True == 1)

try:
    #print(bla)
    print('bla')
except:
    print('Nem jo valtozo nev')
else:
    print('Az else')
finally: #
    print('Try vege')
