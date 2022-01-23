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
            var = int(input("Introduzca número de aves: "))

            if var <= 0:
                raise NumeroNegativo
        except ValueError:
            borrar_pantalla()
            print("Introduzca un número entero positivo.")
        except NumeroNegativo:
            borrar_pantalla()
            print("Por favor no introduzca números negativos.")
        else:
            break

    return var

def numero_gallinas(A):
    gallinas = round(A/3)

    return gallinas

def huevos_producidos(G):
    # Gallinas tipo 1, las que ponen 1 huevo cada 3 días.
    huevos = G/2 * 30/3

    # Gallinas tipo 2, las que ponen 1 huevo cada 5 días.
    huevos += G/2 * 30/5

    return huevos

def main():
    borrar_pantalla()

    A = detectar_errores()
    G = numero_gallinas(A)

    huevos:float = huevos_producidos(G)
    print("El total de huevos producidos en un mes es %d." %huevos)

main()
