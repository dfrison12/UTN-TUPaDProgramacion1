# TP 9 - Recursividad - Tecnicatura Universitaria en Programacion
# Alumno: Dario Frison

# 1. Crea una función  recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def ejercicio_1():
    # Solicitar numero al usuario
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
            break
        else:
            print("** Error: Debe ingresar un número entero positivo **")

    print(f"Factoriales desde 1 hasta {numero}: {factorial(numero)}")

def main():
    ejercicio_1()

main()