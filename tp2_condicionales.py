# TP 2 - Condicionales - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

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

# Ejecutar el ejercicios
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()