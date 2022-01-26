import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def detectar_errores(n):
    while True:
        try:
            if n == 1:
                var = input("Introduzca el coeficiente A del término x^2: ")
            elif n == 2:
                var = input("Introduzca el coeficiente B del término x: ")
            elif n == 3:
                var = input("Introduzca el coeficiente C del término independiente: ")
            elif n == 4:
                var = input("Introduzca el número que desea evaluar en el polinomio: ")

            var = int(var)

        except ValueError:
            try:
                var = float(var)
                break
            except ValueError:
                borrar_pantalla()
                print("Por favor introduzca un número racional.")
        else:
            break

    return var

def evaluar_polinomio(A, B, C, x):
    resultado = A * x ** 2 + B * x + C

    return resultado

def main():
    borrar_pantalla()

    # Polinomio de grado 2, de la forma Ax^2 + Bx + C
    A = detectar_errores(1)
    B = detectar_errores(2)
    C = detectar_errores(3)
    x = detectar_errores(4)

    resultado = evaluar_polinomio(A, B, C, x)
    print("El resultado de f(" + str(x) + ") = (" + str(A) + ")x^2 + (" + str(B) + ")x + (" + str(C) + ") = " + str(resultado))

main()
