import os

# Se importa la librería math debido a que la función módulo de Python tiene un comportamiento diferente
# con los números negativos y decimales, la función módulo de la librería math es mejor para este caso.
import math

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def detectar_errores(n):
    while True:
        try:
            if n == 1:
                var = input("Introduzca el primer sumando: ")
            elif n == 2:
                var = input("Introduzca el segundo sumando: ")
            elif n == 3:
                var = input("Introduzca el número que desea saber si es múltiplo de la suma de los dos primeros: ")

            var = int(var)

        except ValueError:
            try:
                var = float(var)
                break
            except ValueError:
                borrar_pantalla()
                print("Por favor introduzca un número racional.")
        else:
            break

    return var

def comprobar_multiplo(sumando_1, sumando_2, multiplo):
    suma = sumando_1 + sumando_2

    if math.fmod(multiplo, suma) == 0:
        resultado = "El número " + str(multiplo) + " es múltiplo de la suma entre los números " + str(sumando_1) + " y " + str(sumando_2) + "."
    else:
        resultado = "El número " + str(multiplo) + " no es múltiplo de la suma entre los números " + str(sumando_1) + " y " + str(sumando_2) + "."

    return resultado

def main():
    borrar_pantalla()

    sumando_1 = detectar_errores(1)
    sumando_2 = detectar_errores(2)
    multiplo = detectar_errores(3)

    print(comprobar_multiplo(sumando_1, sumando_2, multiplo))

main()
