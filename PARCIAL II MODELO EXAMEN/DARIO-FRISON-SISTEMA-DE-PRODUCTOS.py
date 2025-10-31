def mostrar_menu():
    while True:
        print('\n--- Menú de Gestión de Productos ---')
        print('-'* 40)
        print('1. Mostrar productos ')
        print('2. Agregar producto ')
        print('3. Editar precio de producto ')
        print('4. Eliminar producto ')
        print('5. Salir ')
        print('-'* 40)

        opcion = input('Ingrese una opción (1-5): ').strip()

        match opcion:
            case '1':
                print('Mostrar productos')
            case '2':
                print('Agregar producto')
            case '3':
                print('Editar precio de producto')
            case '4':
                print('Eliminar producto')
            case '5':
                print('Gracias por usar el sistema. :)')
                break
            case _:
                print('Opción inválida. Por favor, elija una opción del 1 al 5.')

mostrar_menu()