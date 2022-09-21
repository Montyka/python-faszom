import string
import random

karakterek = list('!@#$%^&*()' + string.digits + string.ascii_letters)

def jelszo_generator():
    hosszusag = int(input('Kerlek ird be a jelszod hosszusagat: '))
    jelszo = []

    for i in range(hosszusag):
        jelszo.append(random.choice(karakterek))
    random.shuffle(karakterek)

    print(''.join(jelszo))

jelszo_generator()

