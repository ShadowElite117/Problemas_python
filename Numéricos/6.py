import os

# Se importa la librería math debido a que la función módulo de Python tiene un comportamiento diferente
# con los números negativos y decimales, la función módulo de la librería math es mejor para este caso.
import math

class Error(Exception):
    pass

class DivisionPorCero(Error):
    pass

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def detectar_errores(n):
    while True:
        try:
            if n == 1:
                var = input("Introduzca el número: ")
            elif n == 2:
                var = input("Introduzca el número que desea probar como divisor del primero: ")

            var = int(var)

            if n == 2 and var == 0:
                raise DivisionPorCero

        except ValueError:
            try:
                var = float(var)

                if n == 2 and var == 0:
                    raise DivisionPorCero
                else:
                    break
            except ValueError:
                print("Por favor introduzca un número racional.")
            except DivisionPorCero:
                print("El divisor no puede ser el número 0, por favor introduzca otro número.")
        except DivisionPorCero:
            print("El divisor no puede ser el número 0, por favor introduzca otro número.")
        else:
            break

    return var

def modulo(numero, divisor):

    resto = math.fmod(numero, divisor)

    if resto == 0:
        resultado = "El número " + str(divisor) + " es divisor del número " + str(numero)
    else:
        resultado = "El número " + str(divisor) + " no es divisor del número " + str(numero)

    return resultado

def main():
    borrar_pantalla()

    numero = detectar_errores(1)
    divisor = detectar_errores(2)

    print(modulo(numero, divisor))

main()
