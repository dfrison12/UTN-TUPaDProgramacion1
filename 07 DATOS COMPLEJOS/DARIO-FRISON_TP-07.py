# TP 7 - Estructura de datos - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

def ejercicio_1_2_y_3():
    # Diccionario inicial
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    print("Diccionario inicial de frutas:")
    print(precios_frutas)
    print()
    
    # Ejercicio: Añadir nuevas frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print("Diccionario después de añadir las nuevas frutas:")
    print(precios_frutas)
    print()

    # Ejercicio 2: Actualizar los precios de las frutas especificadas
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print("Diccionario después de actualizar los precios:")
    print(precios_frutas)
    print()
    
    # Ejercicio 3: Crear lista con solo los nombres de las frutas (claves del diccionario)
    lista_frutas = list(precios_frutas.keys())

    print(lista_frutas)
    print()


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

def ejercicio_4():
    contactos = {}
    
    print("Carga de contactos telefónicos")
    
    # Cargar 5 contactos
    for i in range(1, 6):
        print(f"\nContacto {i}:")
        nombre = input("  Ingrese el nombre: ")
        telefono = input("  Ingrese el número de teléfono: ")
        contactos[nombre] = telefono
    
    print("\nContactos cargados exitosamente!")
    print(f"Total de contactos: {len(contactos)}")
    print()
    
    # Mostrar todos los contactos
    print("Lista de contactos:")
    for nombre, telefono in contactos.items():
        print(f"  {nombre}: {telefono}")
    print()
    
    # Consultar un contacto
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    
    if nombre_buscar in contactos:
        print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")
    print()

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

def ejercicio_5():
    print("Análisis de palabras en una frase")
    
    # Ingresar frase
    frase = input("Ingrese una frase: ")
    palabras = frase.lower().split()
    palabras_unicas = set(palabras)
    
    # Recuento de cada palabra
    recuento = {}
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1
    
    print("\nResultados:")
    print(f"Palabras únicas: {palabras_unicas}")
    print(f"Recuento: {recuento}")
    print()

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

def ejercicio_6():
    alumnos = {}
    
    print("Registro de alumnos y notas")
    
    # Cargar 3 alumnos con sus 3 notas
    for i in range(1, 4):
        print(f"\nAlumno {i}:")
        nombre = input("  Ingrese el nombre del alumno: ")
        
        # Solicitar y validar la primera nota
        while True:
            entrada_nota1 = input("  Ingrese la primera nota: ")
            if entrada_nota1.replace('.', '', 1).isdigit() or (entrada_nota1.startswith('-') and entrada_nota1[1:].replace('.', '', 1).isdigit()):
                nota1 = float(entrada_nota1)
                if 0 <= nota1 <= 10:
                    break
                else:
                    print("  ** Error: La nota debe estar entre 0 y 10 **")
            else:
                print("  ** Error: Ingrese un valor numérico válido **")
        
        # Solicitar y validar la segunda nota
        while True:
            entrada_nota2 = input("  Ingrese la segunda nota: ")
            if entrada_nota2.replace('.', '', 1).isdigit() or (entrada_nota2.startswith('-') and entrada_nota2[1:].replace('.', '', 1).isdigit()):
                nota2 = float(entrada_nota2)
                if 0 <= nota2 <= 10:
                    break
                else:
                    print("  ** Error: La nota debe estar entre 0 y 10 **")
            else:
                print("  ** Error: Ingrese un valor numérico válido **")
        
        # Solicitar y validar la tercera nota
        while True:
            entrada_nota3 = input("  Ingrese la tercera nota: ")
            if entrada_nota3.replace('.', '', 1).isdigit() or (entrada_nota3.startswith('-') and entrada_nota3[1:].replace('.', '', 1).isdigit()):
                nota3 = float(entrada_nota3)
                if 0 <= nota3 <= 10:
                    break
                else:
                    print("  ** Error: La nota debe estar entre 0 y 10 **")
            else:
                print("  ** Error: Ingrese un valor numérico válido **")
        
        # Guardar el alumno con una tupla de notas
        alumnos[nombre] = (nota1, nota2, nota3)
    
    print("\nAlumnos registrados exitosamente!")
    print()
    print("Promedio de cada alumno:")

    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: Notas {notas} - Promedio: {promedio:.2f}")
    print()

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

def ejercicio_7():
    print("Análisis de aprobados en parciales")
    
    # Solicitar cantidad de estudiantes para Parcial 1 con validación
    print("\n--- Parcial 1 ---")
    while True:
        entrada_cantidad_p1 = input("¿Cuántos estudiantes aprobaron el Parcial 1? ")
        if not (entrada_cantidad_p1.isdigit() and int(entrada_cantidad_p1) >= 0):
            print("** Error: La cantidad debe ser un número entero no negativo **")
        else:
            cantidad_p1 = int(entrada_cantidad_p1)
            break
    
    parcial_1 = set()
    for i in range(cantidad_p1):
        estudiante = input(f"  Ingrese el nombre del estudiante {i+1}: ")
        parcial_1.add(estudiante)
    
    # Solicitar cantidad de estudiantes para Parcial 2 con validación
    print("\n--- Parcial 2 ---")
    while True:
        entrada_cantidad_p2 = input("¿Cuántos estudiantes aprobaron el Parcial 2? ")
        if not (entrada_cantidad_p2.isdigit() and int(entrada_cantidad_p2) >= 0):
            print("** Error: La cantidad debe ser un número entero no negativo **")
        else:
            cantidad_p2 = int(entrada_cantidad_p2)
            break
    
    parcial_2 = set()
    for i in range(cantidad_p2):
        estudiante = input(f"  Ingrese el nombre del estudiante {i+1}: ")
        parcial_2.add(estudiante)
    
    print("\n" + "=" * 50)
    print("Resultados del análisis:")
    print("-" * 50)
    
    # Estudiantes que aprobaron ambos parciales (intersección)
    ambos_parciales = parcial_1 & parcial_2
    print(f"\nEstudiantes que aprobaron AMBOS parciales: {ambos_parciales}")
    print(f"Total: {len(ambos_parciales)} estudiantes")
    
    # Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
    solo_uno = parcial_1 ^ parcial_2
    print(f"\nEstudiantes que aprobaron SOLO UNO de los parciales: {solo_uno}")
    print(f"Total: {len(solo_uno)} estudiantes")
    
    # Desglose de quienes aprobaron solo uno u otro
    solo_parcial_1 = parcial_1 - parcial_2
    solo_parcial_2 = parcial_2 - parcial_1
    print(f"  - Solo Parcial 1: {solo_parcial_1}")
    print(f"  - Solo Parcial 2: {solo_parcial_2}")
    
    # Lista total de estudiantes que aprobaron al menos un parcial (unión)
    al_menos_uno = parcial_1 | parcial_2
    print(f"\nEstudiantes que aprobaron AL MENOS UN parcial: {al_menos_uno}")
    print(f"Total: {len(al_menos_uno)} estudiantes")
    print()

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

def ejercicio_8():
    inventario = {
        "Laptop": 15,
        "Mouse": 50,
        "Teclado": 30,
        "Monitor": 20
    }
    
    print("Sistema de Gestión de Inventario")
    
    continuar = True
    while continuar:
        print("\n--- Menú de opciones ---")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades al stock (producto existente)")
        print("3. Agregar un nuevo producto")
        print("4. Mostrar inventario completo")
        print("5. Salir")
        print("-" * 50)
        
        opcion = input("Seleccione una opción: ")
        print()
        
        if opcion == "1":
            # Consultar stock de un producto
            producto = input("Ingrese el nombre del producto a consultar: ")
            
            if producto in inventario:
                print(f"Stock de {producto}: {inventario[producto]} unidades")
            else:
                print(f"El producto '{producto}' no existe en el inventario.")
        
        elif opcion == "2":
            # Agregar unidades al stock de un producto existente
            producto = input("Ingrese el nombre del producto: ")
            
            if producto in inventario:
                print(f"Stock actual de {producto}: {inventario[producto]} unidades")
                
                while True:
                    entrada_cantidad = input("Ingrese la cantidad de unidades a agregar: ")
                    if not (entrada_cantidad.isdigit() and int(entrada_cantidad) >= 0):
                        print("** Error: La cantidad debe ser un número entero no negativo **")
                    else:
                        cantidad = int(entrada_cantidad)
                        inventario[producto] += cantidad
                        print(f"Stock actualizado de {producto}: {inventario[producto]} unidades")
                        break
            else:
                print(f"El producto '{producto}' no existe en el inventario.")
                print("Use la opción 3 para agregar un nuevo producto.")
        
        elif opcion == "3":
            # Agregar un nuevo producto
            producto = input("Ingrese el nombre del nuevo producto: ")
            
            if producto in inventario:
                print(f"El producto '{producto}' ya existe con {inventario[producto]} unidades.")
                print("Use la opción 2 para agregar más unidades.")
            else:
                while True:
                    entrada_stock = input(f"Ingrese el stock inicial para {producto}: ")
                    if not (entrada_stock.isdigit() and int(entrada_stock) >= 0):
                        print("** Error: El stock debe ser un número entero no negativo **")
                    else:
                        stock = int(entrada_stock)
                        inventario[producto] = stock
                        print(f"Producto '{producto}' agregado con {stock} unidades.")
                        break
        
        elif opcion == "4":
            # Mostrar inventario completo
            print("=" * 50)
            print("Inventario completo:")
            print("-" * 50)
            if inventario:
                for producto, stock in inventario.items():
                    print(f"  {producto}: {stock} unidades")
            else:
                print("  El inventario está vacío.")
            print("=" * 50)
        
        elif opcion == "5":
            # Salir
            print("Saliendo del sistema de inventario...")
            continuar = False
        
        else:
            print("** Opción no válida. Por favor, seleccione una opción del 1 al 5 **")
    
    print()

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

def ejercicio_9():
    agenda = {
        ("Martes", "14:00"): "Cita médica",
        ("Miércoles", "09:00"): "Clase de yoga",
        ("Jueves", "16:00"): "Entrenamiento en el gimnasio",
    }
    
    print("Sistema de Agenda")
    
    continuar = True
    while continuar:
        print("\n--- Menú de opciones ---")
        print("1. Consultar actividad en día y hora específicos")
        print("2. Agregar nueva actividad")
        print("3. Mostrar toda la agenda")
        print("4. Eliminar una actividad")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        print()
        
        if opcion == "1":
            # Consultar actividad
            dia = input("Ingrese el día (ej: Lunes, Martes, etc.): ")
            hora = input("Ingrese la hora (formato HH:MM, ej: 10:00): ")
            
            # Crear tupla para buscar en la agenda
            clave = (dia, hora)
            
            if clave in agenda:
                print(f"Actividad para {dia} a las {hora}: {agenda[clave]}")
            else:
                print(f"No hay ninguna actividad programada para {dia} a las {hora}.")
        
        elif opcion == "2":
            # Agregar nueva actividad
            dia = input("Ingrese el día (ej: Lunes, Martes, etc.): ")
            hora = input("Ingrese la hora (formato HH:MM, ej: 10:00): ")
            
            clave = (dia, hora)
            
            if clave in agenda:
                print(f"Ya existe una actividad para {dia} a las {hora}: {agenda[clave]}")
                respuesta = input("¿Desea reemplazarla? (s/n): ").lower()
                if respuesta == "s":
                    evento = input("Ingrese la nueva actividad: ")
                    agenda[clave] = evento
                    print(f"Actividad actualizada para {dia} a las {hora}.")
                else:
                    print("Operación cancelada.")
            else:
                evento = input("Ingrese la actividad: ")
                agenda[clave] = evento
                print(f"Actividad agregada: {dia} a las {hora} - {evento}")
        
        elif opcion == "3":
            # Mostrar toda la agenda
            print("=" * 50)
            print("Agenda completa:")
            print("-" * 50)
            if agenda:
                # Ordenar por día y hora para mejor visualización
                for (dia, hora), evento in agenda.items():
                    print(f"  {dia} a las {hora}: {evento}")
            else:
                print("  La agenda está vacía.")
            print("=" * 50)
        
        elif opcion == "4":
            # Eliminar una actividad
            dia = input("Ingrese el día de la actividad a eliminar: ")
            hora = input("Ingrese la hora de la actividad a eliminar: ")
            
            clave = (dia, hora)
            
            if clave in agenda:
                evento_eliminado = agenda[clave]
                del agenda[clave]
                print(f"Actividad eliminada: {dia} a las {hora} - {evento_eliminado}")
            else:
                print(f"No existe ninguna actividad programada para {dia} a las {hora}.")
        
        elif opcion == "5":
            # Salir
            print("Saliendo del sistema de agenda...")
            continuar = False
        
        else:
            print("** Opción no válida. Por favor, seleccione una opción del 1 al 5 **")
    
    print()

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

def ejercicio_10():
    # Diccionario original
    paises_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Chile": "Santiago",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción",
        "Colombia": "Bogotá",
        "Perú": "Lima",
        "Ecuador": "Quito",
        "Venezuela": "Caracas",
        "Bolivia": "La Paz"
    }
    
    print("Inversión de diccionario")
    print("\nDiccionario original (País -> Capital):")
    print("-" * 50)

    for pais, capital in paises_capitales.items():
        print(f"  {pais}: {capital}")
    
    # Invertir el diccionario: 
    capitales_paises = {}
    for pais, capital in paises_capitales.items():
        capitales_paises[capital] = pais
    
    # Mostrar diccionario invertido
    print("\nDiccionario invertido (Capital -> País):")
    print("-" * 50)
    for capital, pais in capitales_paises.items():
        print(f"  {capital}: {pais}")
    
    print("\n" + "=" * 50)
    
    # Demostración de uso: consultar país por capital
    print("\nDemostración: Consultar país por su capital")
    print("-" * 50)
    
    continuar = True
    while continuar:
        capital_buscar = input("\nIngrese una capital para saber a qué país pertenece (o 'salir' para terminar): ")
        
        if capital_buscar.lower() == "salir":
            print("Saliendo de la consulta...")
            continuar = False
        elif capital_buscar in capitales_paises:
            print(f"La capital {capital_buscar} pertenece a: {capitales_paises[capital_buscar]}")
        else:
            print(f"La capital '{capital_buscar}' no se encuentra en el diccionario.")
    
    print()


# Programa principal
def main():
    # Ejercicios 1, 2 y 3
    ejercicio_1_2_y_3()
    # Ejercicio 4
    ejercicio_4()
    # Ejercicio 5
    ejercicio_5()
    # Ejercicio 6
    ejercicio_6()
    # Ejercicio 7
    ejercicio_7()
    # Ejercicio 8
    ejercicio_8()
    # Ejercicio 9
    ejercicio_9()
    # Ejercicio 10
    ejercicio_10()


main()

