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

# 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def ejercicio_2():
    while True:
        entrada = input("Ingrese la posición de la serie de Fibonacci que desea calcular: ")
        if entrada.isdigit() and int(entrada) >= 0:
            posicion = int(entrada)
            break
        else:
            print("** Error: Debe ingresar un número entero no negativo **")

    print(f"Fibonacci en la posición {posicion}: {fibonacci(posicion)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def ejercicio_3():
    while True:
        entrada_base = input("Ingrese la base (número entero): ")
        entrada_exponente = input("Ingrese el exponente (número entero no negativo): ")
        if entrada_base.isdigit() and entrada_exponente.isdigit() and int(entrada_exponente) >= 0:
            base = int(entrada_base)
            exponente = int(entrada_exponente)
            break
        else:
            print("** Error: Debe ingresar números enteros válidos **")

    print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")























def main():
    # ejercicio_1()
    # ejercicio_2()
    ejercicio_3()

main()