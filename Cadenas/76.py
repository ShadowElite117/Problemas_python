import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def cadena_a_lista(cadena):
    return list(cadena)

def lista_a_cadena(lista):
    if lista:
        cadena = "".join(lista)
    else:
        cadena = ""

    return cadena

def remover_espacios(lista):
    for i in lista:
        if i == " ":
            lista.remove(i)

    return lista

def invertir_cadena(cadena):
    cadena_invertida = ""
    lon_cadena = len(cadena)

    for i in range(lon_cadena):
        cadena_invertida += cadena[-i - 1]

    return cadena_invertida

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto que desea comprobar si es frase palíndrome: ")

    lista_cadena = cadena_a_lista(cadena)
    lista_frase = remover_espacios(lista_cadena)
    frase = lista_a_cadena(lista_frase)
    frase_invertida = invertir_cadena(frase)

    if frase == frase_invertida:
        print('La cadena "' + cadena + '" es frase palíndrome.')
    else:
        print('La cadena "' + cadena + '" no es frase palíndrome.')

main()
