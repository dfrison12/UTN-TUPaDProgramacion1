# Sistema de Gestión de Países

## Descripción

Sistema desarrollado en Python para gestionar información sobre países del mundo. Permite realizar operaciones de consulta, filtrado, ordenamiento y análisis estadístico sobre un catálogo de países almacenado en formato CSV.

Este proyecto fue desarrollado como Trabajo Práctico Integrador (TPI) para la materia **Programación 1** de la Universidad Tecnológica Nacional (UTN).

## Características principales

- **Gestión de datos**: Agregar países y actualizar su información (población y superficie)
- **Búsqueda**: Buscar países por nombre con coincidencia parcial o exacta
- **Filtros avanzados**:
  - Por continente
  - Por rango de población
  - Por rango de superficie
- **Ordenamiento**: Ordenar países por nombre, población o superficie (ascendente/descendente)
- **Estadísticas**:
  - País con mayor y menor población
  - Promedio de población y superficie
  - Cantidad de países por continente
- **Persistencia**: Todos los datos se guardan automáticamente en archivo CSV
- **Validaciones robustas**: Sistema de validación con loops bloqueantes que garantiza la integridad de los datos

## Estructura del proyecto

```
TPI PAISES/
├── gestion_paises.py    # Programa principal
├── paises.csv           # Base de datos de países (CSV)
└── README.md            # Este archivo
```

## Requisitos

- **Python 3.x** (se recomienda Python 3.10 o superior)
- Biblioteca estándar de Python (csv, os)
- No requiere instalación de paquetes externos

## Instrucciones de uso

### 1. Ejecutar el programa

Abrir una terminal en la carpeta `TPI PAISES` y ejecutar:

```bash
python gestion_paises.py
```

### 2. Navegación por el menú

El programa presenta un menú interactivo con las siguientes opciones:

```
1.  Agregar país
2.  Actualizar población/superficie de un país
3.  Buscar país por nombre
4.  Filtrar por continente
5.  Filtrar por rango de población
6.  Filtrar por rango de superficie
7.  Ordenar países
8.  Mostrar estadísticas
9.  Mostrar todos los países
10. Salir
```

### 3. Ejemplos de uso

#### Agregar un país

```
Opción: 1
Nombre del país: Italia
Población: 60317000
Superficie (km²): 301340
Continentes válidos: América, Europa, Asia, África, Oceanía
Continente: Europa

País "Italia" agregado exitosamente.
```

#### Buscar un país

```
Opción: 3
Ingrese el nombre (o parte del nombre) a buscar: Ar

Se encontraron 2 resultado(s):
Nombre               Población       Superficie (km²)     Continente
Argentina            45,376,763      2,780,400            América
```

#### Filtrar por continente

```
Opción: 4
Continentes válidos: América, Europa, Asia, África, Oceanía
Continente: América

Países de América (3 encontrado(s)):
Nombre               Población       Superficie (km²)     Continente
Argentina            45,376,763      2,780,400            América
Brasil               213,993,437     8,515,767            América
Canadá               38,005,238      9,984,670            América
```

#### Ordenar países

```
Opción: 7
¿Por qué criterio desea ordenar?
1. Nombre
2. Población
3. Superficie
Ingrese una opción (1-3): 2

¿En qué orden?
1. Ascendente
2. Descendente
Ingrese una opción (1-2): 2

Países ordenados por población (descendente):
Nombre               Población       Superficie (km²)     Continente
Brasil               213,993,437     8,515,767            América
Japón                125,800,000     377,975              Asia
Egipto               102,334,404     1,002,450            África
...
```

#### Ver estadísticas

```
Opción: 8

Total de países registrados: 8

País con mayor población:
  Brasil: 213,993,437 habitantes

País con menor población:
  Australia: 25,687,041 habitantes

Promedio de población: 87,718,221 habitantes
Promedio de superficie: 3,945,998 km²

Cantidad de países por continente:
  América: 3 país(es)
  Asia: 1 país(es)
  Europa: 2 país(es)
  Oceanía: 1 país(es)
  África: 1 país(es)
```

## Estructura de datos

### Formato del archivo CSV

El archivo `paises.csv` contiene los siguientes campos:

| Campo      | Tipo    | Descripción                    |
|------------|---------|--------------------------------|
| nombre     | string  | Nombre del país                |
| poblacion  | int     | Población total del país       |
| superficie | int     | Superficie en kilómetros cuadrados |
| continente | string  | Continente (América, Europa, Asia, África, Oceanía) |

### Ejemplo de datos CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## Validaciones implementadas

El sistema incluye las siguientes validaciones:

1. **Campos obligatorios**: No se permite dejar campos vacíos
2. **Números enteros positivos**: Población y superficie deben ser números enteros mayores a 0
3. **Continentes válidos**: Solo se aceptan los 5 continentes predefinidos
4. **Países únicos**: No se permite agregar países con nombres duplicados
5. **Rangos válidos**: En filtros, el valor mínimo no puede ser mayor que el máximo
6. **Loops bloqueantes**: Todas las validaciones re-solicitan datos hasta obtener valores válidos

## Conceptos de programación aplicados

Este proyecto integra los siguientes conceptos vistos en Programación 1:

- **Estructuras de datos**: Listas y diccionarios
- **Funciones**: Modularización del código (una función = una responsabilidad)
- **Estructuras condicionales**: if/else, match/case
- **Estructuras repetitivas**: while con contadores manuales
- **Manejo de archivos**: Lectura y escritura de archivos CSV
- **Validación de entrada**: Verificación de datos ingresados por el usuario
- **Ordenamiento**: Uso de sorted() con key
- **Estadísticas básicas**: Cálculos de máximo, mínimo, promedio y conteo

## Decisiones de diseño

### Arquitectura modular

Siguiendo el feedback del profesor, el programa implementa:

- **Carga única de datos**: El CSV se lee una sola vez al inicio del programa
- **Paso de parámetros**: La lista de países se pasa entre funciones, evitando variables globales implícitas
- **Guardado selectivo**: Solo se escribe al CSV cuando hay cambios (agregar o actualizar)

### Validaciones robustas

Todas las funciones de validación usan **loops bloqueantes** que re-solicitan datos hasta obtener valores válidos:

```python
def solicitar_numero_positivo(mensaje):
    while True:
        valor = input(mensaje).strip()

        if '.' in valor:
            print('Debe ingresar un número entero (sin decimales). Intente nuevamente.')
            continue

        if not valor.isdigit():
            print('Debe ingresar un número válido. Intente nuevamente.')
            continue

        numero = int(valor)

        if numero <= 0:
            print('El número debe ser mayor a 0. Intente nuevamente.')
            continue

        break

    return numero
```

### Uso de while con contadores manuales

Para cumplir con los requisitos de la materia, se priorizan los loops `while` con contadores manuales en lugar de `for`:

```python
# Mostrar países usando while
i = 0
while i < len(paises):
    pais = paises[i]
    print(f"{pais['nombre']:<20} {pais['poblacion']:<15,}")
    i += 1
```

## Participación de los integrantes

**Desarrollador**: Dario Frison

**Tareas realizadas**:
- Diseño de la arquitectura del sistema
- Implementación de todas las funcionalidades
- Validaciones y manejo de errores
- Documentación del proyecto
- Testing y ajustes finales

## Fuentes consultadas

- Documentación oficial de Python 3: https://docs.python.org/3/
- Módulo CSV de Python: https://docs.python.org/3/library/csv.html
- Material de estudio de Programación 1 - UTN
- Código de ejemplo del Parcial II (Sistema de Biblioteca)

## Mejoras futuras

Posibles extensiones del proyecto:

- Agregar más campos (capital, idioma, moneda, PIB)
- Implementar filtros combinados (ej: continente + rango de población)
- Exportar resultados de consultas a archivos separados
- Gráficos estadísticos con bibliotecas como matplotlib
- Interfaz gráfica con tkinter
- Importación de datos desde APIs externas

## Licencia

Este proyecto es de uso educativo para la materia Programación 1 de la UTN.

---

**Universidad Tecnológica Nacional (UTN)**
**Materia**: Programación 1
**Año**: 2024
