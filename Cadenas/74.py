import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def invertir_cadena(cadena):
    cadena_invertida = ""
    lon_cadena = len(cadena)

    for i in range(lon_cadena):
        cadena_invertida += cadena[-i - 1]

    return cadena_invertida

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto que desea invertir: ")

    print(invertir_cadena(cadena))

main()
