def cif(cislo):
    cifra = 0                           # inicializovali sme cifru číslom 0
    while cislo > 0:                    # // = celocislene delenie
        lastdig = cislo % 10            # % = zvysok po delení
        cifra += lastdig
        cislo = cislo // 10
    return cifra
#print(cif(1234))


def cif(cislo):
    cifra = 0
    while cislo > 0:
        lastdig = cislo % 10
        if lastdig % 2 == 0:
            cifra += lastdig
        cislo = cislo // 10
    return cifra
#print(cif(1234))


def cif(cislo):
    cifra = 0
    while cislo > 0:
        lastdig = cislo % 10
        cifra = cifra * 10 + lastdig
        cislo = cislo // 10
    return cifra
#(cif(1234))






def convertToBin(namb):
    powTen = 1
    result = 0
    while namb != 0:
        modulo = namb % 2                               # zvyšok po delení 2, môže byť iba 1 alebo
        result = modulo * powTen + result               #
        namb = namb // 2                                # vydelíme 2
        powTen *= 10                                    # mocnina desiatky
    return result
#print(convertToBin(37))


def convertToDex(namb):
    powTwo = 1
    result = 0
    while namb != 0:
        lastdig = namb % 10
        result = lastdig * powTwo + result
        namb = namb // 10
        powTwo *= 2
    return result
print(convertToDex(1011))


def convertToBin(namb):
    powTen = 1
    result = 0
    while namb != 0:
        modulo = namb % 10
        result = modulo * powTen + result
        namb = namb // 10
        powTen *= 2
    return result
#print(convertToBin(1011))