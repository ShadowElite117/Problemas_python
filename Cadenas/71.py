import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def contar_caracter(caracter, cadena):
    contador = 0

    for i in cadena:
        if i == caracter:
            contador += 1

    return contador

def main():
    borrar_pantalla()

    caracter = input("Introduzca el carácter que desea contar en una cadena: ")
    cadena = input("Introduzca la cadena de texto: ")

    print("El carácter " + caracter + " aparece " + str(contar_caracter(caracter, cadena)) + " veces en la cadena introducida.")

main()
