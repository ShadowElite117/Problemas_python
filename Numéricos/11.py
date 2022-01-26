import os

class Error(Exception):
    pass

class CoeficienteCero(Error):
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
                var = input("Introduzca el coeficiente A del término x^2: ")
            elif n == 2:
                var = input("Introduzca el coeficiente B del término x: ")
            elif n == 3:
                var = input("Introduzca el coeficiente C del término independiente: ")

            var = int(var)

            if n == 1 and var == 0:
                raise CoeficienteCero

        except ValueError:
            try:
                var = float(var)

                if n == 1 and var == 0:
                    raise CoeficienteCero
                else:
                    break
            except ValueError:
                borrar_pantalla()
                print("Por favor introduzca un número racional.")
            except CoeficienteCero:
                print("El coeficiente A del término x^2 no puede ser cero, ya que el polinomio debe ser de grado 2.")
        except CoeficienteCero:
            print("El coeficiente A del término x^2 no puede ser cero, ya que el polinomio debe ser de grado 2.")
        else:
            break

    return var

# La derivada de un polinomio grado 2 de la forma Ax^2 + Bx + C, es 2Ax + B
def derivar_polinomio_g2(A):
    A = A * 2

    return A

def main():
    borrar_pantalla()

    # Polinomio de grado 2, de la forma Ax^2 + Bx + C
    A = detectar_errores(1)
    B = detectar_errores(2)
    C = detectar_errores(3)

    A_1 = derivar_polinomio_g2(A)
    print("El coeficiente lineal de la derivada del polinomio (" + str(A) + ")x^2 + (" + str(B) + ")x + (" + str(C) + ") es " + str(A_1))

main()
