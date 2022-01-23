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
                var = float(input("Introduzca medida N del corral: "))
            elif n == 2:
                var = float(input("Introduzca medida M del corral: "))
            elif n == 3:
                var = float(input("Introduzca precio por metro del alambre de púas: "))
            elif n == 4:
                var = float(input("Introduzca precio por metro de las tablas de madera: "))
            elif n == 5:
                var = float(input("Introduzca precio por metro de las varillas: "))

            if var <= 0:
                raise NumeroNegativo
        except ValueError:
            borrar_pantalla()
            print("Introduzca un número racional positivo.")
        except NumeroNegativo:
            borrar_pantalla()
            print("Por favor no introduzca números negativos.")
        else:
            break

    return var

def calcular_perimetro(M, N):
    perimetro = 2 * M + 2 * N

    return perimetro

def calcular_precios(perimetro, P, Q, S):
    precio_alambre = 5 * perimetro * P
    precio_tablas = 4 * perimetro * Q
    precio_varillas = 8 * perimetro * S

    print("Cercar el corral con 5 hileras de alambre de púas tiene un coste de: %.2f" %round(precio_alambre, 2))
    print("Cercar el corral con 4 hileras de tablas de madera tiene un coste de: %.2f" %round(precio_tablas, 2))
    print("Cercar el corral con 8 hileras de varillas tiene un coste de: %.2f" %round(precio_varillas, 2))

    return precio_alambre, precio_tablas, precio_varillas

def menor_precio(precio_alambre, precio_tablas, precio_varillas):
    precio_barato = precio_alambre

    if precio_barato > precio_tablas:
        precio_barato = precio_tablas
    elif precio_barato > precio_varillas:
        precio_barato - precio_varillas

    return precio_barato

def comparar_precios(precio_barato, precio_alambre, precio_tablas, precio_varillas):
    if precio_barato == precio_alambre and precio_barato == precio_tablas and precio_barato == precio_varillas:
        cerca_barata = "Todos los cerramientos son igual de económicos."
    elif precio_barato == precio_alambre and precio_barato == precio_tablas:
        cerca_barata = "Los cerramientos de alambre y tablas son los más económicos."
    elif precio_barato == precio_alambre and precio_barato == precio_varillas:
        cerca_barata = "Los cerramientos de alambre y varillas son los más económicos."
    elif precio_barato == precio_tablas and precio_barato == precio_varillas:
        cerca_barata = "Los cerramientos de tablas y varillas son los más económicos."
    elif precio_barato == precio_alambre:
        cerca_barata = "El cerramiento más económico es el de alambre de púas."
    elif precio_barato == precio_tablas:
        cerca_barata = "El cerramiento más económico es el de tablas de madera."
    elif precio_barato == precio_varillas:
        cerca_barata = "El cerramiento más económico es el de varillas."

    return cerca_barata

def main():
    borrar_pantalla()

    N = detectar_errores(1)
    M = detectar_errores(2)
    P = detectar_errores(3)
    Q = detectar_errores(4)
    S = detectar_errores(5)

    perimetro:float = calcular_perimetro(M, N)
    precio_alambre, precio_tablas, precio_varillas = calcular_precios(perimetro, P, Q, S)
    precio_barato:float = menor_precio(precio_alambre, precio_tablas, precio_varillas)
    cerca_barata:str = comparar_precios(precio_barato, precio_alambre, precio_tablas, precio_varillas)

    print(cerca_barata)

main()
