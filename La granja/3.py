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
                var = int(input("Introduzca número de escorpiones pequeños: "))
            elif n == 2:
                var = int(input("Introduzca número de escorpiones medianos: "))
            elif n == 3:
                var = int(input("Introduzca número de escorpiones grandes: "))

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

def escorpiones_en_venta(P, M, G):
    escorpiones = P + M + G
    poblacion_de_reserva = round(escorpiones * 2/3)
    escorpiones_disponibles = escorpiones - poblacion_de_reserva

    # La idea es vender la mayor cantidad posible de kilos de escorpiones, por lo tanto, se deben
    # vender primero los grandes (G), luego los medianos (M) y por último los pequeños (P), hasta
    # que la población de escorpiones restantes sea de 2/3.
    # Se hace necesario en cada caso, calcular la diferencia entre la suma de los grupos de escor-
    # piones necesarios para cumplir la demanda y los escorpiones disponibles para la venta, de
    # tal modo que se puede calcular con precisión la máxima cantidad de kilos de escorpiones.
    if escorpiones_disponibles <= G:
        diferencia = G - escorpiones_disponibles
        G -= diferencia
        kilos = (G * 50)/1000
    elif escorpiones_disponibles <= G + M:
        diferencia = G + M - escorpiones_disponibles
        M -= diferencia
        kilos = (G * 50 + M * 30)/1000
    else:
        diferencia = escorpiones - escorpiones_disponibles
        P -= diferencia
        kilos = (G * 50 + M * 30 + P * 20)/1000

    return kilos

def main():
    borrar_pantalla()

    P = detectar_errores(1)
    M = detectar_errores(2)
    G = detectar_errores(3)

    kilos_en_venta:float = escorpiones_en_venta(P, M, G)

    print("Se pueden vender a China %.2f kilos de escorpiones." %kilos_en_venta)

main()
