import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def cadena_a_lista(cadena):
    return list(cadena)

def comparar_cadenas(cadena_1, cadena_2):
    incluida = 'La cadena "' + cadena_2 + '" está incluida la cadena "' + cadena_1 + '".'
    no_incluida = 'La cadena "' + cadena_2 + '" no está incluida la cadena "' + cadena_1 + '".'
    cadena_3 = ""

    lista_cadena_1 = cadena_a_lista(cadena_1)

    for i in cadena_2:
        j = 0

        while j < len(lista_cadena_1):
            if i == lista_cadena_1[j]:
                lista_cadena_1.remove(i)
                cadena_3 += i

                break
            j += 1

    if cadena_2 == cadena_3:
        return incluida

    return no_incluida

def main():
    borrar_pantalla()

    cadena_1 = input("Introduzca la cadena de texto: ")
    cadena_2 = input("Introduzca la cadena que desea comprobar si está incluida en la primera cadena: ")

    print(comparar_cadenas(cadena_1, cadena_2))

main()
