import string
import random

betuk = list(string.ascii_letters)
szamok = list(string.digits)
specko = list('!@#$%^&*()')
karakterek = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def jelszo_generator():
    hosszusag = int(input('Kerlek ird be a jelszod hosszusagat: '))

    betuk_mennyisege = int(input('Kerlek add meg a betuk szamat: '))
    szamok_mennyisege = int(input('Kerlek add meg a szamok mennyiseget: '))
    specko_mennyisege = int(input('Kerlek add meg a specialis karakterek mennyiseget: '))
    karakterek_mennyisege = betuk_mennyisege + szamok_mennyisege + specko_mennyisege

    if karakterek_mennyisege > hosszusag:
        print('Karakterek szama tobb mint a jelszo hosszusaga ')
        return

    jelszo =[]

    for i in range(betuk_mennyisege):
        jelszo.append(random.choice(betuk))
    for i in range(szamok_mennyisege):
        jelszo.append(random.choice(szamok))
    for i in range(specko_mennyisege):
        jelszo.append(random.choice(specko))

    print(''.join(jelszo))


jelszo_generator()


