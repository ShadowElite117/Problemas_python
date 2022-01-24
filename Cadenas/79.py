import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def completar_diccionario(diccionario, correspondencias):
    abecedario = "abcdefghijklmnopqrstuvwxyz"

    for i in range(26):
        diccionario[abecedario[i]] = correspondencias[i]

    return diccionario

def codificar_cadena(cadena, correspondencias):
    cadena_codificada = ""
    diccionario = {}

    diccionario = completar_diccionario(diccionario, correspondencias)

    for letra in cadena:
        if letra == " ":
            cadena_codificada += " "
        elif letra in diccionario:
            cadena_codificada += diccionario[letra]
        else:
            cadena_codificada += letra

    return cadena_codificada

def main():
    borrar_pantalla()

    cadena = input("Introduzca la cadena de texto que desea codificar: ")
    correspondencias = input("Introduzca la cadena de correspondencias con la que desea codificar la cadena anterior:\n")

    cadena_codificada = codificar_cadena(cadena, correspondencias)
    print("Cadena de texto codificada:\n" + cadena_codificada)

main()
