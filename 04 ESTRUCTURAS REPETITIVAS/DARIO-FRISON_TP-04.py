# TP 4 - Estructuras Repetitivas - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

import random

# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
def ejercicio_1():
    print("Ejercicio 1")
    
    for numero in range(0, 101):
        print(numero)

# Ejecrcicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
def ejercicio_2():
    print("Ejercicio 2")

    numero = int(input("Por favor, ingresa un numero entero: "))
    cantidad_de_digitos = len(str(numero))
    print(f"El numero {numero} tiene {cantidad_de_digitos} digitos")

# Ejecrcicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
def ejercicio_3():
    print("Ejercicio 3")

    valor1 = int(input("Por favor, ingresa el primer valor: "))
    valor2 = int(input("Por favor, ingresa el segundo valor: "))
    suma = 0

    if valor1 > valor2:
        print("El primer valor debe ser menor que el segundo")
        return

    for numero in range(valor1 + 1, valor2):
        suma += numero
    print(f"La suma de los numeros {valor1} y {valor2} es: {suma}")
    
# Ejecrcicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
def ejercicio_4():
    print("Ejercicio 4")

    CORTE = 0
    suma = 0
    numero = int(input("Por favor, ingresa un numero entero o " + str(CORTE) + " para cortar: "))

    if numero == CORTE:
        print("No se ingresaron numeros")
        return

    while numero != CORTE:
        suma += numero
        numero = int(input("Por favor, ingresa un numero entero o " + str(CORTE) + " para cortar: "))

    print(f"La suma de los numeros es: {suma}")

# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
def ejercicio_5():
    print("Ejercicio 5")
    
    numero_aleatorio = random.randint(0, 9)
    intentos = 1
    MENSAJE = "Por favor, ingresa un numero entre 0 y 9: "

    numero = int(input(MENSAJE))
    if numero < 0 or numero > 9:
        print("El numero debe estar entre 0 y 9")
        return

    while numero != numero_aleatorio:
        numero = int(input("Por favor, ingresa un numero entre 0 y 9: "))
        intentos += 1
        if numero < 0 or numero > 9:
            print("El numero debe estar entre 0 y 9")
            continue

    print(f"Adivinaste el numero en {intentos} intentos")

# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
def ejercicio_6():
    print("Ejercicio 6")

    for numero in range(100, 0, -2):
        print(numero)
# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
def ejercicio_7():
    print("Ejercicio 7")

    numero = int(input("Por favor, ingresa un numero entero positivo: "))
    suma = 0

    if numero < 0:
        print("El numero debe ser positivo")
        return

    for numero in range(numero + 1):
        suma += numero

    print(f"La suma de los numeros es: {suma}")

# Ejercicio 8: 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
#  (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
def ejercicio_8():
    print("Ejercicio 8")

    cantidad = 100
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0

    for numero in range(cantidad):
        numero = int(input("Por favor, ingresa un numero entero: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if numero < 0:
            negativos += 1
        else:
            positivos += 1

    print(f"Los numeros pares son: {pares}")
    print(f"Los numeros impares son: {impares}")
    print(f"Los numeros negativos son: {negativos}")
    print(f"Los numeros positivos son: {positivos}")

# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
def ejercicio_9():
    print("Ejercicio 9")
    
    cantidad = 4
    suma = 0

    for numero in range(cantidad):
        numero = int(input("Por favor, ingresa un numero entero: "))
        suma += numero
    
    media = suma / cantidad
    print(f"La media de los numeros es: {media}")

# Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def ejercicio_10():
    print("Ejercicio 10")

    numero = int(input("Por favor, ingresa un numero: "))
    numero_invertido = 0

    while numero > 0:
        # Extraer el ultimo digito del numero ingresado
        ultimo_digito = numero % 10 
        # Agregar el ultimo digito al numero invertido
        numero_invertido = numero_invertido * 10 + ultimo_digito
        # Eliminar el ultimo digito del numero ingresado
        numero = numero // 10

    print(f"El numero invertido es: {numero_invertido}")



#Ejecutar el ejercicios
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_8()
ejercicio_9()
ejercicio_10()
