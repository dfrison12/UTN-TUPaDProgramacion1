# TP 1 - Secuenciales - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

import math

# Ejercicio 1: Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
def ejercicio_1():
    print("EJERCICIO 1")
    print("Hola Mundo!")

# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
def ejercicio_2():
    print("EJERCICIO 2")
    
    nombre = input("Por favor, ingresa tu nombre: ")

    print(f"Hola {nombre}!")

# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
def ejercicio_3():
    print("EJERCICIO 3")

    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    lugar = input("Ingresa tu lugar de residencia: ")
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# Ejercicio 4: Crear un programa que pida al usuario el radio de un círculo e imprima su área y su perímetro.
def ejercicio_4():
    print("EJERCICIO 4")
    radio = float(input("Ingresa el radio del círculo: "))
    
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    
    print(f"El área del círculo es: {area}")
    print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima a cuántas horas equivale.
def ejercicio_5():
    print("EJERCICIO 5")

    segundos = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos / 3600
    
    print(f"{segundos} segundos equivalen a {horas} horas")

# Ejercicio 6: Crear un programa que pida al usuario un número e imprima la tabla de multiplicar de dicho número.
def ejercicio_6():
    print("EJERCICIO 6")

    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    
    print(f"Tabla de multiplicar del {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
def ejercicio_7():
    print("EJERCICIO 7")

    num1 = int(input("Ingresa el primer número (distinto de 0): "))
    num2 = int(input("Ingresa el segundo número (distinto de 0): "))
    
    # Verificar que ambos números sean distintos de 0
    if num1 == 0 or num2 == 0:
        print("Error: Los números deben ser distintos de 0")
        return
    
    # Operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division}")

# Ejercicio 8: Crear un programa que pida al usuario su altura y su peso e imprima su índice de masa corporal.
def ejercicio_8():
    print("EJERCICIO 8")

    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura ** 2)

    print(f"Tu índice de masa corporal (IMC) es: {imc}")

# Ejercicio 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima su equivalente en grados Fahrenheit.
def ejercicio_9():
    print("EJERCICIO 9")
    
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (9/5) * celsius + 32

    print(f"{celsius}°C equivalen a {fahrenheit}°F")

# Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima el promedio de los mismos.
def ejercicio_10():
    print("EJERCICIO 10")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    promedio = (num1 + num2 + num3) / 3
    
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")

# Ejecutar cada ejercicio
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
