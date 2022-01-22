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

def detectar_errores(n):
    while True:
        try:
            if n == 1:
                var = int(input("Introduzca número de vacas: "))
            elif n == 2:
                var = float(input("Introduzca medida N del corral: "))
            elif n == 3:
                var = float(input("Introduzca medida M del corral: "))
            elif n == 4:
                var = float(input("Introduzca litros X de leche producidos por M metros cuadrados de pasto: "))

            if var <= 0:
                raise NumeroNegativo
        except ValueError:
            borrar_pantalla()
            if n == 1:
                print("Introduzca un número entero positivo.")
            elif n == 2 or n == 3 or n == 4:
                print("Introduzca un número racional positivo.")
        except NumeroNegativo:
            borrar_pantalla()
            print("Por favor no introduzca números negativos.")
        else:
            break

    return var

# Función necesaria para calcular la razón de proporcionalidad que influye directamente en la cantidad
# de leche producida por vaca, con respecto al área de pasto que puede consumir cada vaca, teniendo en
# cuenta que cada vaca necesita M metros cuadrados para producir X litros de leche.
def razon_de_proporcionalidad(M, area_por_vaca):
    proporcion = M/area_por_vaca

    return proporcion

def leche_producida(V, X, proporcion):
    leche = V * (X/proporcion)

    return leche

def main():
    borrar_pantalla()

    V = detectar_errores(1)
    N = detectar_errores(2)
    M = detectar_errores(3)
    X = detectar_errores(4)

    area:float = N * M

    area_por_vaca:float = area/V

    proporcion:float = razon_de_proporcionalidad(M, area_por_vaca)

    leche_total = leche_producida(V, X, proporcion)

    print("El total de leche producida en la granja es %.2f litros." %leche_total)

main()
