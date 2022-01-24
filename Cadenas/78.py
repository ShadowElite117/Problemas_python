import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def corrimiento_circular_der(cadena):
    lon_cad = len(cadena)
    cadena_final = cadena[lon_cad - 1] + cadena[0:lon_cad - 1]

    return cadena_final

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto a la que desea realizarle corrimiento circular a derecha: ")

    print("Cadena después de realizarle corrimiento circular:\n" + corrimiento_circular_der(cadena))

main()
