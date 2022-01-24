import os
from platform import python_branch

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def corrimiento_circular_izq(cadena):
    lon_cad = len(cadena)
    cadena_final = cadena[1:lon_cad] + cadena[0]

    return cadena_final

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto a la que desea realizarle corrimiento circular a izquierda: ")

    print("Cadena después de realizarle corrimiento circular:\n" + corrimiento_circular_izq(cadena))

main()
