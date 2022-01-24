import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def completar_diccionario(diccionario, correspondencias):
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    for i in range(26):
        diccionario[correspondencias[i]] = abecedario[i]

    return diccionario

def descodificar_cadena(cadena, correspondencias):
    cadena_descodificada = ""
    diccionario = {}

    diccionario = completar_diccionario(diccionario, correspondencias)

    for letra in cadena:
        if letra == " ":
            cadena_descodificada += " "
        elif letra in diccionario:
            cadena_descodificada += diccionario[letra]
        else:
            cadena_descodificada += letra

    return cadena_descodificada

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto que desea descodificar: ")
    correspondencias = input("Introduzca la cadena de correspondencias con la que desea descodificar la cadena anterior:\n")

    cadena_descodificada = descodificar_cadena(cadena, correspondencias)
    print("Cadena de texto descodificada:\n" + cadena_descodificada)

main()
