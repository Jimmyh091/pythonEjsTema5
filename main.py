
def ej1(linea, char):
    return len([x for x in linea if x == char])

def ej2(linea):
    return linea == linea[::-1]

def ej3(linea):

    return [
        linea[:5],
        linea[-5:],
        linea[1::2],
        linea[::2],
        linea[::-1]
    ]

def ej4(linea):
    return linea[::-1]

def ej5(texto):
    palabras = texto.split()

    res = palabras[0]
    for it in palabras:
        if len(res) < len(palabras[it]):
            res = palabras[it]

    return res

def ej6(texto):

    masLarga = ej5(texto)

    palabras = texto.split()

    masCorta = palabras[0]
    for it in palabras:
        if len(masCorta) > len(palabras[it]):
            masCorta = palabras[it]

    return [masLarga, masCorta]

## hemos hecho varias veces este ejercicio con manu y tengo la formula grabada a fuego
def ej7(texto, subcadena):
    palabras = texto.split(subcadena)
    return len(palabras)

def ej8(texto, subcadena):

    palabras = texto.split(subcadena)

    lista = []

    for it in range(0, len(palabras) + 1):
        total = 0

        for it2 in palabras[:it + 1]:
            total += len(it2)

        inicio = total
        final = total + len(palabras[it])

        lista.add([inicio, final])

    return [len(palabras), lista]

def ej9(texto, subcadena):
    palabras = texto.split()

    return [x for x in palabras if texto[0:len(subcadena)] == subcadena and texto[-len(subcadena):-1]]

def ej10(num):
    res = ""
    for it in range(1, 10 + 1):
        res += f"{num} + {it} = {num * it}\n"

    return res

ej1()