opciones_menu = [
    "1. Ingresar titulo (sin ejemplares)",
    "2. Ingresar ejemplares disponibles (sin titulo)",
    "3. Motrar catalogo de libros",
    "4. Consultar disponibilidad de un titulo especifico",
    "5. Listar agotados",
    "6. Agregar titulo (con ejemplares)",
    "7. Actualizar ejemplares (prestamo / devolucion)",
    "8. Salir"
]
titulos = []
ejemplares = []

salir = False
while not salir:
    print()
    print("--------------------------------")
    print(" * Menu Biblioteca")
    print("--------------------------------")
    for opcion in opciones_menu:
        print(opcion)
    print('--------------------------------')
    print()
    seleccion = input("- Seleccione una opcion: ")

    print()

    match seleccion:
        case "1":
            titulo = input("- Ingresar titulo: ")
            while titulo in titulos or titulo == "":
                print(" ** ** **")
                print("- El titulo ya existe o esta vacio")
                titulo = input("- Ingrese nuevamente el titulo: ")
                print("** ** ** ")
            print(f"- Titulo ingresado: {titulo}")
            titulos.append(titulo)
            posicion = titulo.index(titulo)
            # Aca no se uso append porque no se sabe la posicion del titulo en la lista
            ejemplares.insert(posicion, 0)

        case "2":
            if not titulos:
                print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                continue
            
            # Listar titulos disponibles
            print('--------------------------------')
            print('Listado de titulos disponibles:')
            for i, titulo in enumerate(titulos):
                print(f"{i + 1}. {titulo}")

            print()
            posicion = int(input("- Seleccione el numero de titulo para ingresar cantidad de ejemplares:  ")) - 1

            # Validar que la posicion sea valida

            while posicion < 0 or posicion >= len(titulos):
                print("Posicion invalida, intente nuevamente")
                posicion = int(input("- Seleccione el numero de titulo para ingresar cantidad de ejemplares: ")) - 1

            cantidad = int(input("- Ingrese la cantidad de ejemplares: "))
            ejemplares[posicion] += cantidad
            print(f"Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]}")

        case "3":
            if not titulos:
                print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                continue
            print('--------------------------------')
            print("Catalogo de libros:")
            print('--------------------------------')
            print()
            for i, titulo in enumerate(titulos):
                print(f"{i + 1}. {titulo}: {ejemplares[i]} ejemplares disponibles")

        case "4":
            if not titulos:
                print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                continue
            
            titulo_consulta = input("- Ingresar titulo a consultar: ")

            while True:
                if titulo_consulta in titulos:
                    posicion = titulos.index(titulo_consulta)
                    print(f"Cantidad de ejemplares disponibles para {titulo_consulta}: {ejemplares[posicion]}")
                    break
                else:
                    print(f"El titulo {titulo_consulta} no se encuentra en el catalogo")
                    print("Desea ingresarlo nuevamente? (S: Vuelve a ingresar / N: Vuelve al menu)")

                    if input().lower() == "s":
                        titulo_consulta = input("- Ingresar titulo a consultar: ")
                    else:
                        break

        case "5":
            if not titulos:
                print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                continue
            
            agotados = False

            for i in ejemplares:
                if i == 0:
                    agotados = True
                    break
            
            if agotados:
                print('--------------------------------')
                print("Libros agotados:")
                print('--------------------------------')
                for titulo in titulos:
                    posicion = titulos.index(titulo)
                    if ejemplares[posicion] == 0:
                        print(f"- {titulo} - 0 ejemplares disponibles")
            else:
                print('--------------------------------')
                print("No hay libros agotados")
                print('--------------------------------')

        case "6":
            nuevo_titulo = input("- Ingresar titulo a agregar: ")

            if nuevo_titulo in titulos:
                print(f"El titulo {nuevo_titulo} ya existe")
            else:
                cantidad = int(input(f"- Ingresar cantidad de ejemplares para {nuevo_titulo}: "))
                titulos.append(nuevo_titulo)
                posicion = titulos.index(nuevo_titulo)
                ejemplares.insert(posicion, cantidad)
                print(f"Titulo {nuevo_titulo} agregado con {cantidad} ejemplares")
            
        case "7":
            if not titulos:
                print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
                continue

            for i, titulo in enumerate(titulos):
                print(f"{i + 1}. {titulo}")

            posicion = int(input("- Ingresar numero de titulo a actualizar: ")) - 1

            while posicion < 0 or posicion >= len(titulos):
                print("Posicion invalida, intente nuevamente")
                posicion = int(input("- Seleccione el numero de titulo para ingresar cantidad de ejemplares: ")) - 1

            accion = input("- Ingrese 'p' para prestamo o 'd' para devolucion: " ).lower()

            if accion == "p":
                if ejemplares[posicion] > 0:
                    ejemplares[posicion] -= 1
                    print(f"Prestamo realizado para {titulos[posicion]} Ejemplares disponibles: {ejemplares[posicion]}")
                else:
                    print(f"No hay ejemplares disponibles para {titulos[posicion]}")
            elif accion == "d":
                    ejemplares[posicion] += 1
                    print(f"Devolucion realizada para {titulos[posicion]} Ejemplares disponibles: {ejemplares[posicion]}")
            else:
                print("Opcion no valida. Use 'p' para prestamo o 'd' para devolucion")

        case "8":
            print("Hasta luego!")
            salir = True
            
        case _:
            print("Opcion no valida")
        