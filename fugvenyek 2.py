
a = 10
b = 20

def osszeadas1(): # Zarojelbe irsz bemenetet, parametert 0 vagy tobb, vagy string is
    print(a+b)

def osszeadas2(a, b, c=4): # bemenet/parameterre ugyan az a szabaly vonatkozik mint valtozokra
    return a+b+c # return, az vissza tero ertek, magaba nem ir ki semmit

def osszeadas3(*args):  #args=arguments/parameterek, *args 0 vagy tobb parametert is fogadhat,de igazabol barmit ithatsz args helyett
    return sum(args) #sum=osszeg


def udvozlesek(*args):
    koszones = 'Ennyi fele koszones letezik: '
    for k in args:
        koszones += k
        koszones += ', '
    print(koszones[0:len(koszones)-2])

udvozlesek('Szia','Hello', 'Szevasz', 'Szervusz', 'Hali')

# osszeadas1()
# osszeg = osszeadas2(45, 25) #return pelda, vagy print(osszeadas2(45, 25)), most valtozoval
# print(osszeg)
#
# print(osszeadas3(10, 20, 30, 40, 50, 60))