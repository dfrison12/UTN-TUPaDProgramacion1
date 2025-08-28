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


# Ejecutar el ejercicios
ejercicio_1()
ejercicio_2()