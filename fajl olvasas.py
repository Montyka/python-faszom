
file = open('New folder/mondasok.txt', 'r', encoding='utf-8') # encoding csak akkor kell ha valami teljesen nem angol szoveg

#for sor in file:  # for ciklusos megoldas
#    print(sor.strip())


#sor = file.readline() # readline az 1 sort fog bereadelni
#while sor:
 #   print(sor.strip())
   # sor = file.readline()



#file.close()

with open('New folder/mondasok.txt', 'r', encoding='utf-8') as file: #ez magatol lezarja a filet, ide nem kell file.close

    sor = file.read() #readlines az listakent fogja beolvasni, read sok sorral nem ajanlott
    print(sor)

    #while sor:
     #   print(sor.strip())
      #  sor = file.readline()



