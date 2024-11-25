
import random
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

"""
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
"""

def ejPipo():
    while(True):

        print("Bienvenido al pipo este\n")

        res = int(input("Que quieres hacer?:"
              "\n\t1. Aprender las tablas."
              "\n\t2. Practicar las tablas."
              "\n\t3. Escapar.\n > "))

        if res == 1:
            aprenderTablas()
        elif res == 2:
            practicarTablas()
        elif res == 3:
            print("Espero que te lo hayas pasado bien!!!!!!!!!!")
            break
        else:
            print("Opcion no disponible.")

def aprenderTablas():
    res = int(input("Que tablas quieres aprender?\n > "))

    for it in range(1,10):
        print(f"{res} x {it} = {(res * it)}")

    print("\n")

def practicarTablas():

    res = input("Que tablas quiieres practicar? (separa los numeros con \'-\')\n > ")

    tablas = res.split("-")

    numIntentos = int(input("Cuantos intentos quieres tener?\n > "))

    aciertos = 0
    fallos = 0

    for it in range(0, numIntentos):
        tabla = int(random.choice(tablas))
        multiplicador = random.randint(0,10)

        intento = int(input(f"Cuanto es {tabla} x {multiplicador}?"))

        solucion = int(tabla * multiplicador)

        if intento == solucion:
            print("Correcto!\n")
            aciertos += 1
        else:
            print(f"Mal. {tabla} x {multiplicador} es {solucion}, no {intento}\n")
            fallos += 1

    print(f"Has tenido {aciertos} aciertos y {fallos} fallos. Eso te da una tasa de acierto del {numIntentos * 100 / aciertos}%\n")

def ahorcado():

    print("Bienvenido al ahorcado")

    dificultad = int(input("Introduce la dificultad:"
                    "\n\t1. Bebe."
                    "\n\t2. Menos bebe."
                    "\n\t3. Muy poco bebe.\n > "))

    vidas = 3

    solucion : str

    if dificultad == 1:
        solucion = "mesa"
    elif dificultad == 2:
        solucion = "computacion"
    elif dificultad == 3:
        solucion = "esternocleidomastoideo"

    letrasAcertadas = []

    for it in solucion:
        letrasAcertadas.append(False)

    victoria = True

    while vidas > 0:

        victoria = True

        for it in range(0, len(solucion)):
            if letrasAcertadas[it]:
                print(" " + solucion[it])
            else:
                print(" _")

        print("\n")

        res = input("Elige una letra\n > ")

        letraIncluida = False
        for it in solucion:
            if res.lower() == it:
                letraIncluida = True

        if letraIncluida:
            print("Correcto!")

            for it in range(0, len(solucion)):
                if solucion[it] == res:
                    letrasAcertadas[it] = True

        else:
            vidas -= 1
            print(f"Incorrecto. Te quedan {vidas} vidas.")

        for it in letrasAcertadas:
            if not it:
                victoria = False
                break

        if victoria:
            break


    print(f"\n\n{"Has ganado!!!" if victoria else "Perdiste"}")

ahorcado()