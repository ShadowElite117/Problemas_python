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
                var = int(input("Introduzca el primer número: "))
            elif n == 2:
                var = int(input("Introduzca el segundo número: "))

            if var < 1:
                raise ValueError
        except ValueError:
            borrar_pantalla()
            print("Por favor introduzca un número natural mayor o igual a 1.")
        else:
            break

    return var

def descomponer_numero(numero):
    descomposicion = []

    while numero != 1:
        if numero % 2 == 0:
            divisor = 2
            numero = numero/divisor
        else:
            divisor = 3

            while numero % divisor != 0:
                divisor += 2

            numero = numero/divisor

        descomposicion.append(divisor)

    descomposicion.append(1)
    descomposicion.sort(reverse=True)

    return descomposicion

def primos_relativos(descomposicion_num_1, descomposicion_num_2):
    divisores_comunes = []

    for i in descomposicion_num_1:
        if i in descomposicion_num_2:
            divisores_comunes.append(i)

    if divisores_comunes == [1]:
        relativos = True
    else:
        relativos = False

    return relativos

def main():
    borrar_pantalla()

    numero_1 = detectar_errores(1)
    numero_2 = detectar_errores(2)

    descomposicion_num_1 = descomponer_numero(numero_1)
    descomposicion_num_2 = descomponer_numero(numero_2)

    relativos = primos_relativos(descomposicion_num_1, descomposicion_num_2)

    if relativos == True:
        print("Los números " + str(numero_1) + " y " + str(numero_2) + " son primos relativos.")
    else:
        print("Los números " + str(numero_1) + " y " + str(numero_2) + " no son primos relativos.")

main()
