import os

class Error(Exception):
    pass

class NumeroNegativo(Error):
    pass

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def detectar_errores():
    while True:
        try:
            var = int(input("Introduzca el número que desea saber si es primo o no: "))

            if var < 2:
                raise ValueError
        except ValueError:
            borrar_pantalla()
            print("Por favor introduzca un número natural mayor a 1.")
        else:
            break

    return var

def numero_primo(numero):
    posicion = 1

    if numero == 2:
        resultado = "El número 2 es un número primo."
    elif numero % 2 == 0:
        resultado = "El número " + str(numero) + " no es un número primo, es decir, es compuesto."
    else:
        tercio = numero/3
        i = 3

        while i <= tercio:
            if i < 11:
                if numero % i == 0:
                    resultado = "El número " + str(numero) + " no es un número primo, es decir, es compuesto."

                    break
                else:
                    i += 2
            elif numero % i == 0:
                resultado = "El número " + str(numero) + " no es un número primo, es decir, es compuesto."

                break
            elif posicion == 2:
                posicion += 1
                i += 4
            elif posicion == 4:
                posicion = 1
                i += 2
            else:
                posicion += 1
                i += 2

        if i > tercio:
            resultado = "El número " + str(numero) + " es un número primo."

    return resultado

def main():
    numero = detectar_errores()

    print(numero_primo(numero))

main()
