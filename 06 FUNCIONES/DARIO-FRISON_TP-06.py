# TP 6 - Funciones - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

import math

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

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def es_flotante_valido(s):
    """Devuelve True si la cadena puede convertirse a float y es >= 0."""
    if s.strip() == "":
        return False
    # Permitir formatos como '3', '3.5' o '.5' y también con signo +/-.'
    partes = s.replace('+', '').replace('-', '')
    # Aceptar si contiene solo dígitos o un punto con dígitos
    if partes.count('.') > 1:
        return False
    if partes.replace('.', '').isdigit():
        try:
            return float(s) >= 0
        except Exception:
            return False
    return False


def solicitar_radio_usuario():
    while True:
        entrada = input("Ingrese el radio del círculo: ")
        if not es_flotante_valido(entrada):
            print("Por favor, ingrese un número válido y no negativo para el radio.")
            continue
        radio = float(entrada)
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
        break

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

def solicitar_segundos_usuario():
    while True:
        entrada = input("Ingrese la cantidad de segundos: ")
        if not (entrada.isdigit() and int(entrada) >= 0):
            print("Por favor, ingrese un número entero no negativo para los segundos.")
            continue
        segundos = int(entrada)
        horas = segundos_a_horas(segundos)
        print(f"{segundos} segundos son equivalentes a {horas:.2f} horas.")
        break

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def solicitar_numero_usuario():
    while True:
        entrada = input("Ingrese un número para ver su tabla de multiplicar: ")
        if not (entrada.lstrip('-').isdigit()):
            print("Por favor, ingrese un número entero válido.")
            continue
        numero = int(entrada)
        tabla_multiplicar(numero)
        break

# Programa principal
def main():
    # Ejercicio 1
    imprimir_hola_mundo()
    # Ejercicio 2
    saludo = saludar_usuario("Dario")
    print(saludo)
    # Ejercicio 3
    solicitar_datos_usuario()
    #Ejercicio 4
    solicitar_radio_usuario()
    #Ejercicio 5
    solicitar_segundos_usuario()
    #Ejercicio 6
    solicitar_numero_usuario()



main()