import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def comparar_subcadena_con_cadena(cadena, subcadena, longitud_cadena, longitud_subcadena):
    contenida = 'La cadena "' + subcadena + '" es subcadena de la cadena "' + cadena + '".'
    no_contenida = 'La cadena "' + subcadena + '" no es subcadena de la cadena "' + cadena + '".'

    for i in range(longitud_subcadena, longitud_cadena + 1):
        if subcadena == cadena[i - longitud_subcadena:i]:
            return contenida

    return no_contenida

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto: ")
    subcadena = input("Introduzca la subcadena que desea comprobar si pertenece a la cadena: ")

    longitud_cadena = len(cadena)
    longitud_subcadena = len(subcadena)

    print(comparar_subcadena_con_cadena(cadena, subcadena, longitud_cadena, longitud_subcadena))

main()
