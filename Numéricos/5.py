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
                var = int(input("Introduzca el número base que desea potenciar: "))
            elif n == 2:
                var = int(input("Introduzca el exponente: "))
        except ValueError:
            borrar_pantalla()
            print("Por favor introduzca un número entero.")
        else:
            break

    return var

def potenciar(base, exponente):
    resultado = base ** exponente

    return resultado

def main():
    borrar_pantalla()

    base = detectar_errores(1)
    exponente = detectar_errores(2)

    resultado = potenciar(base, exponente)

    print("El resultado de", base, "elevado a", exponente, "es", resultado)

main()
