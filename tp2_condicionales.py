# TP 2 - Condicionales - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

import random
from statistics import mode, median, mean

# Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga "Es mayor de edad"
def ejercicio_1():
    print("EJERCICIO 1")
    
    edad = int(input("Por favor, ingresa tu edad: "))
    
    if edad > 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

# Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga "Aprobado"; en caso contrario deberá mostrar el mensaje "Desaprobado".
def ejercicio_2():
    print("EJERCICIO 2")
    
    nota = float(input("Por favor, ingresa tu nota: "))
    
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# Ejercicio 3: Escribir un programa que permita ingresar solo números pares.
#  Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
def ejercicio_3():
    print("EJERCICIO 3")
    
    numero = int(input("Por favor, ingresa un número: "))
    
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
def ejercicio_4():
    print("EJERCICIO 4")
    
    edad = int(input("Por favor, ingresa tu edad: "))
    
    if edad < 12:
        print("Niño/a")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >= 18 and edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
def ejercicio_5():
    print("EJERCICIO 5")
    
    contraseña = input("Por favor, ingresa una contraseña: ")
    longitud = len(contraseña)
    
    if longitud >= 8 and longitud <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Usar la moda (mode), la mediana (median) y la media (mean) para predecir la forma de una distribución normal a partir del siguiente criterio:
# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
# Sin sesgo: cuando la media, la mediana y la moda son iguales.
def ejercicio_6():
    print("EJERCICIO 6")
    
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    
    moda_valor = mode(numeros_aleatorios)
    mediana_valor = median(numeros_aleatorios)
    media_valor = mean(numeros_aleatorios)
    
    print("Lista de números: ", numeros_aleatorios)
    print("Moda: ", moda_valor)
    print("Mediana: ", mediana_valor)
    print("Media: ", media_valor)
    
    if media_valor > mediana_valor and mediana_valor > moda_valor:
        print("Sesgo positivo o a la derecha")
    elif media_valor < mediana_valor and mediana_valor < moda_valor:
        print("Sesgo negativo o a la izquierda")
    else:
        print("Sin sesgo")

# Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. 
# Si termina con vocal, añadir un signo de exclamación al final e imprimir el string por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
def ejercicio_7():
    print("EJERCICIO 7")
    
    frase = input("Por favor, ingresa una frase o palabra: ")
    ultima_letra = frase[-1].lower()
    
    if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' or ultima_letra == 'u':
        print(frase,"!")
    else:
        print(frase)

# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
def ejercicio_8():
    print("EJERCICIO 8")
    
    nombre = input("Por favor, ingresa tu nombre: ")
    print("¿Cómo quieres que se muestre tu nombre?")
    print("1. En mayúsculas")
    print("2. En minúsculas")
    print("3. Con la primera letra mayúscula")
    
    opcion = int(input("Ingresa el número de la opción (1, 2 o 3): "))
    
    if opcion == 1:
        mayusculas = nombre.upper()
        print(mayusculas)
    elif opcion == 2:
        minusculas = nombre.lower()
        print(minusculas)
    elif opcion == 3:
        primera_letra_mayuscula = nombre.title()
        print(primera_letra_mayuscula)
    else:
        print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#  Menor que 3: "Muy leve" (imperceptible).
#  Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#  Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#  Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#  Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#  Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
def ejercicio_9():
    print("EJERCICIO 9")
    
    magnitud = float(input("Por favor, ingresa la magnitud del terremoto: "))
    
    if magnitud < 0:
        print("Error: La magnitud de un terremoto no puede ser negativa")
    elif magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10: Utilizando la información sobre las estaciones del año, escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
def ejercicio_10():
    print("EJERCICIO 10")
    
    hemisferio = input("Ingrese el hemisferio (N para Norte, S para Sur): ").upper()
    hemisferio_valido = hemisferio == "N" or hemisferio == "S"

    if not hemisferio_valido:
        print("Error: El hemisferio ingresado no es válido")
        return

    mes = int(input("Ingrese el mes (1-12): "))
    mes_valido = mes >= 1 and mes <= 12

    if not mes_valido:
        print("Error: El mes ingresado no es válido")
        return

    dia = int(input("Ingrese el día (1-31): "))
    dia_valido = dia >= 1 and dia <= 31

    if not dia_valido:
        print("Error: El día ingresado no es válido")
        return
    
    
    if hemisferio == "N":  
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        else:  # (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)
            estacion = "Otoño"
    elif hemisferio == "S":  
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:  # (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20)
            estacion = "Primavera"
    
    print("Estás en la estación de", estacion)

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