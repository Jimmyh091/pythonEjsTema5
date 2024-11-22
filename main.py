
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
        if len(res) < len(it):
            res = it

    return res

def ej6(texto):

    masLarga = ej5(texto)

    palabras = texto.split()

    masCorta = palabras[0]
    for it in palabras:
        if len(masCorta) > len(it):
            masCorta = it

    return [masLarga, masCorta]

## hemos hecho varias veces este ejercicio con manu y tengo la formula grabada a fuego
def ej7(texto, subcadena):
    palabras = texto.split(subcadena)
    return len(palabras)

def ej8(texto, subcadena):

    palabras = texto.split(subcadena)

    lista = []

    for it in range(1, len(palabras)):
        total = 0

        for it2 in palabras[:it]:
            total += len(it2)

        total += len(subcadena) * it - 1

        inicio = total
        final = total + len(subcadena) - 1

        lista.append([inicio, final])

    return [len(palabras), lista]

def ej9(texto, subcadena):
    palabras = texto.split(subcadena)

    return [x for x in palabras if palabras != palabras[0] and palabras != palabras[-1]]

def ej10(num):
    res = ""
    for it in range(1, 10 + 1):
        res += f"{num} * {it} = {num * it}\n"

    return res

print(ej1("hola buenos dias", 'a'))
print(ej2("reconocer"))
print(ej3("asekljxnfskldfa"))
print(ej4("reconoce"))
print(ej5("El pan, del latín panis, es un alimento básico de la dieta humana que se suele preparar mediante el horneado de una masa, elaborada fundamentalmente con harina de cereal, agua y sal. La mezcla, en la mayoría de las ocasiones, suele contener levaduras para que se fermente la masa y sea más esponjosa y tierna."))
print(ej6("El pan, del latín panis, es un alimento básico de la dieta humana que se suele preparar mediante el horneado de una masa, elaborada fundamentalmente con harina de cereal, agua y sal. La mezcla, en la mayoría de las ocasiones, suele contener levaduras para que se fermente la masa y sea más esponjosa y tierna."))
print("\nEjercicio 7: ", ej7("assssasssasasass", "a"))
print("Ejercicio 8: ", ej8("assssasssasasass", "a"))
print("Ejercicio 9: ", ej9("ssassassassass", "a"))
print(ej10(11))