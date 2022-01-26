import os

def borrar_pantalla():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def detectar_errores():
    while True:
        try:
            var = int(input("Introduzca el número que desea comprobar si es de Fibonacci: "))

            if var < 0:
                raise ValueError

        except ValueError:
            print("Por favor introduzca un número natural mayor o igual a cero.")
        else:
            break

    return var

def comprobar_fibonacci(n, fibonacci_n, fibonacci_n_1):
    if n == 0 or n == fibonacci_n_1:
        resultado = "El número " + str(n) + " es de Fibonacci."
    elif n > fibonacci_n_1:
        suma = fibonacci_n + fibonacci_n_1
        fibonacci_n = fibonacci_n_1
        fibonacci_n_1 = suma

        resultado = comprobar_fibonacci(n, fibonacci_n, fibonacci_n_1)
    else:
        resultado = "El número " + str(n) + " no es de Fibonacci."

    return resultado

def main():
    fibonacci_n = 0
    fibonacci_n_1 = 1

    borrar_pantalla()
    n = detectar_errores()

    print(comprobar_fibonacci(n, fibonacci_n, fibonacci_n_1))

main()
