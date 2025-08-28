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



# Ejecutar el ejercicios
ejercicio_1()