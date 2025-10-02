# TP 6 - Funciones - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
#  Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función saludar_usuario(nombre) que reciba un nombre y devuelva
# un saludo personalizado: "Hola <nombre>!". Esta función debe estar disponible
# para ser reutilizada por otras partes del programa.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") 

def solicitar_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)



# Programa principal
def main():
    # Ejercicio 1
    imprimir_hola_mundo()
    # Ejercicio 2
    saludo = saludar_usuario("Dario")
    print(saludo)
    # Ejercicio 3
    solicitar_datos_usuario()

main()