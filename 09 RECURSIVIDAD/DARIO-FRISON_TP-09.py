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

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este 
# procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio_4():
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
            break
        else:
            print("** Error: Debe ingresar un número entero positivo **")

    print(f"Representación en binario de {numero}: {decimal_a_binario(numero)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

def ejercicio_5():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 
# Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

def ejercicio_6():
    while True:
        entrada = input("Ingrese un número entero positivo: ")
        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
            break
        else:
            print("** Error: Debe ingresar un número entero positivo **")

    print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def ejercicio_7():
    while True:
        entrada = input("Ingrese el número de bloques en el nivel más bajo (entero positivo): ")
        if entrada.isdigit() and int(entrada) > 0:
            numero = int(entrada)
            break
        else:
            print("** Error: Debe ingresar un número entero positivo **")

    print(f"Total de bloques necesarios para construir la pirámide: {contar_bloques(numero)}")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        if ultimo_digito == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

def ejercicio_8():
    while True:
        entrada_numero = input("Ingrese un número entero positivo: ")
        entrada_digito = input("Ingrese un dígito (0-9): ")
        if (entrada_numero.isdigit() and int(entrada_numero) > 0 and 
            entrada_digito.isdigit() and 0 <= int(entrada_digito) <= 9):
            numero = int(entrada_numero)
            digito = int(entrada_digito)
            break
        else:
            print("** Error: Debe ingresar un número entero positivo y un dígito válido **")

    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces")

def main():
    ejercicio_1()
    ejercicio_2()
    ejercicio_3()
    ejercicio_4()
    ejercicio_5()
    ejercicio_6()
    ejercicio_7()
    ejercicio_8()

main()