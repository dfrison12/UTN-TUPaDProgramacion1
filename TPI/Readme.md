# Sistema de Gestión y Análisis de Datos de Países

## Descripción del Programa

Sistema completo de gestión de información sobre países desarrollado en Python puro (sin uso de librerías externas como `csv` o `pandas`). Este programa permite administrar, consultar y analizar datos geográficos y demográficos de países de todo el mundo.

### Características Principales

- **Carga Automática**: Los datos se cargan automáticamente desde `paises.csv` al iniciar el programa
- **Gestión de Datos**: Agregar y actualizar países
- **Búsquedas Avanzadas**: Búsqueda por nombre con coincidencia parcial o exacta
- **Filtros Múltiples**: Por continente, rango de población y rango de superficie
- **Ordenamiento Flexible**: Por nombre, población o superficie (ascendente/descendente)
- **Estadísticas Detalladas**: Promedios, extremos y distribución por continentes
- **Validaciones Robustas**: Control de errores y validación de entradas
- **Interfaz Profesional**: Menú interactivo con visualización en formato tabla

### Estructura de Datos

Cada país contiene la siguiente información:
- **Nombre** (string): Nombre del país
- **Población** (int): Cantidad de habitantes
- **Superficie** (int): Área en kilómetros cuadrados
- **Continente** (string): Continente al que pertenece

---

## Instrucciones de Uso

### Requisitos

- Python 3.10 o superior (utiliza `match-case`)
- No requiere instalación de librerías adicionales

### Ejecución del Programa

**IMPORTANTE**: El programa debe ejecutarse desde la misma carpeta donde se encuentra el archivo `Aguero_Frison.py` para que la lectura de archivos CSV funcione correctamente.

1. Abrir terminal en el directorio TPI del proyecto
2. Ejecutar el comando:
   ```bash
   python Aguero_Frison.py
   ```

**Ejemplo de ejecución correcta:**
```bash
cd TPI
python Aguero_Frison.py
```

**Carga Inicial de Datos:**
Al iniciar el programa, se cargará automáticamente el archivo `paises.csv` que contiene los datos iniciales de los países. Este proceso es automático y no requiere intervención del usuario.

### Navegación del Menú

Al iniciar el programa, se cargan automáticamente los datos desde `paises.csv` y luego se presenta un menú interactivo con las siguientes opciones:

#### Gestión de Datos (Opciones 1-2)
- **[1] Agregar país manualmente**: Añade un nuevo país ingresando todos sus datos
- **[2] Actualizar datos de país**: Modifica población y superficie de un país existente

#### Consultas y Búsquedas (Opciones 3-6)
- **[3] Buscar país por nombre**: Búsqueda con coincidencia parcial o exacta
- **[4] Filtrar por continente**: Muestra todos los países de un continente
- **[5] Filtrar por rango de población**: Filtra por población mínima y máxima
- **[6] Filtrar por rango de superficie**: Filtra por superficie mínima y máxima

#### Ordenamiento (Opciones 7-9)
- **[7] Ordenar por nombre**: Orden alfabético (A-Z)
- **[8] Ordenar por población**: Orden ascendente o descendente
- **[9] Ordenar por superficie**: Orden ascendente o descendente

#### Análisis y Estadísticas (Opciones 10-11)
- **[10] Mostrar estadísticas generales**: Indicadores clave y distribución
- **[11] Mostrar todos los países**: Lista completa con opciones de ordenamiento

#### Salida
- **[0] Salir del programa**: Finaliza la ejecución

---

## Ejemplos de Entradas y Salidas

### Ejemplo 1: Inicio del Programa

**Al ejecutar el programa:**
```
>> Cargando datos iniciales desde archivo CSV...

============================================================
           RESULTADO DE CARGA DE ARCHIVO
============================================================
Paises cargados exitosamente: 25
============================================================

>> Presione Enter para continuar...
```

### Ejemplo 2: Agregar País Manualmente

**Entrada:**
```
>> Seleccione una opcion: 1
Ingrese el nombre del país: Uruguay
Ingrese la población: 3500000
Ingrese la superficie (km²): 176215
Continentes existentes: América Del Sur, Europa, Asia
Ingrese el continente: América Del Sur
```

**Salida:**
```
==================================================
>>> Pais 'Uruguay' agregado exitosamente! <<<
==================================================
```

### Ejemplo 3: Buscar País

**Entrada:**
```
>> Seleccione una opcion: 3
Ingrese el nombre del pais a buscar: arg
```

**Salida:**
```
Se encontraron 1 resultado(s) para 'arg':

✓ Coincidencias parciales (1):

==================================================================================
PAÍS            │ POBLACIÓN       │ SUPERFICIE      │ CONTINENTE      │ DENSIDAD    
                │ (habitantes)    │ (km²)           │                 │ (hab/km²)   
----------------------------------------------------------------------------------
Argentina       │  45,000,000     │   2,780,400     │ América Del Sur │      16.2
==================================================================================
Total de países mostrados: 1
```

### Ejemplo 4: Filtrar por Continente

**Entrada:**
```
>> Seleccione una opcion: 4
Continentes disponibles:
  1. América Del Sur (2 países)
  2. Europa (2 países)
  3. Asia (1 países)

Ingrese el continente: europa
```

**Salida:**
```
Países en Europa (2 países):

==================================================================================
PAÍS            │ POBLACIÓN       │ SUPERFICIE      │ CONTINENTE      │ DENSIDAD    
                │ (habitantes)    │ (km²)           │                 │ (hab/km²)   
----------------------------------------------------------------------------------
España          │  47,000,000     │     505,990     │ Europa          │      92.9
Francia         │  67,000,000     │     643,801     │ Europa          │     104.1
==================================================================================
Total de países mostrados: 2
```

### Ejemplo 5: Estadísticas Generales

**Entrada:**
```
>> Seleccione una opcion: 10
```

**Salida:**
```
======================================================================
                    ESTADÍSTICAS GENERALES
======================================================================

 ESTADÍSTICAS DE POBLACIÓN:
--------------------------------------------------
País con mayor población: Brasil
  └─ 213,000,000 habitantes
País con menor población: Uruguay
  └─ 3,500,000 habitantes
Población promedio: 75,100,000 habitantes
Población total: 375,500,000 habitantes

 ESTADÍSTICAS DE SUPERFICIE:
--------------------------------------------------
País con mayor superficie: Brasil
  └─ 8,515,767 km²
País con menor superficie: Uruguay
  └─ 176,215 km²
Superficie promedio: 2,524,435 km²
Superficie total: 12,622,173 km²

DISTRIBUCIÓN POR CONTINENTES:
--------------------------------------------------
América Del Sur:
  ├─ Países: 2 (40.0%)
  ├─ Población total: 258,000,000
  └─ Superficie total: 11,296,167 km²
Europa:
  ├─ Países: 2 (40.0%)
  ├─ Población total: 114,000,000
  └─ Superficie total: 1,149,791 km²
Asia:
  ├─ Países: 1 (20.0%)
  ├─ Población total: 3,500,000
  └─ Superficie total: 176,215 km²

RESUMEN GENERAL:
--------------------------------------------------
Total de países: 5
Total de continentes: 3
Densidad poblacional promedio: 29.75 hab/km²
======================================================================
```

---

## Formato del Archivo CSV

El archivo CSV debe seguir este formato:

```csv
nombre,poblacion,superficie,continente
Argentina,45000000,2780400,América del Sur
Brasil,213000000,8515767,América del Sur
España,47000000,505990,Europa
Francia,67000000,643801,Europa
Japón,125000000,377975,Asia
```

### Reglas de Formato

- **Primera línea**: Puede ser un encabezado (será omitido automáticamente)
- **Campos**: 4 campos separados por comas
- **No permitir**: Campos vacíos
- **Población y Superficie**: Deben ser números enteros positivos

### Validaciones Implementadas

El programa valida:
- Cantidad correcta de campos (4)
- Campos no vacíos
- Valores numéricos válidos
- Números positivos
- Formato correcto de datos
- Manejo de errores con reporte detallado

---

## Participación de los Integrantes

### Agüero Maximiliano
- Desarrollo de funciones de gestión de datos (agregar, actualizar, buscar)
- Implementación de validaciones y manejo de errores
- Diseño de la interfaz de usuario y menús
- Funciones de lectura y procesamiento de archivos CSV
- Testing y depuración del código

### Dario Frison
- Desarrollo de funciones de filtrado y ordenamiento
- Implementación de algoritmos de ordenamiento (selección)
- Funciones de estadísticas y análisis de datos
- Diseño de visualización de datos en formato tabla
- Documentación y comentarios del código

### Trabajo Colaborativo
- Diseño conjunto de la arquitectura del sistema
- Definición de estructura de datos
- Revisión cruzada de código
- Pruebas de integración y casos de uso
- Optimización de rendimiento

---

## Características Técnicas

### Estructuras de Datos Utilizadas
- **Listas**: Para almacenar colecciones de países
- **Diccionarios**: Para representar cada país con sus atributos
- **Sets**: Para obtener continentes únicos

### Técnicas de Programación
- **Funciones modulares**: Una función = una responsabilidad
- **Validación robusta**: Control exhaustivo de entradas
- **Algoritmo de ordenamiento**: Método Burbuja - Bubble Sort (O(n²))
- **Búsqueda eficiente**: Comparación normalizada de cadenas
- **Manejo de archivos**: Lectura manual sin librerías CSV

### Conceptos Aplicados
- Estructuras condicionales (`if`, `elif`, `else`, `match-case`)
- Estructuras repetitivas (`for`, `while`)
- Funciones con parámetros y retorno de valores
- Manipulación de cadenas de texto
- Operaciones con listas y diccionarios
- Lectura y procesamiento de archivos
- Formateo avanzado de salida

---

## Algoritmo de Ordenamiento: Bubble Sort

### Descripción
El programa utiliza el **algoritmo de ordenamiento burbuja (Bubble Sort)** para ordenar los países según diferentes criterios (nombre, población, superficie).

### Características del Bubble Sort
- **Complejidad temporal**: O(n²) en el peor y promedio caso
- **Complejidad espacial**: O(1) - ordenamiento in-place
- **Estabilidad**: Algoritmo estable (mantiene el orden relativo de elementos iguales)
- **Método**: Comparación e intercambio de elementos adyacentes

### Funcionamiento
El algoritmo compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que toda la lista está ordenada. En cada pasada, el elemento más grande/pequeño "burbujea" hacia su posición final.

### Ejemplo Visual
```
Lista inicial: [5, 2, 8, 1]

Pasada 1:
  [5, 2, 8, 1] → compara 5 y 2 → [2, 5, 8, 1]
  [2, 5, 8, 1] → compara 5 y 8 → [2, 5, 8, 1]
  [2, 5, 8, 1] → compara 8 y 1 → [2, 5, 1, 8] (8 en posición final)

Pasada 2:
  [2, 5, 1, 8] → compara 2 y 5 → [2, 5, 1, 8]
  [2, 5, 1, 8] → compara 5 y 1 → [2, 1, 5, 8] (5 en posición final)

Pasada 3:
  [2, 1, 5, 8] → compara 2 y 1 → [1, 2, 5, 8] ✓ Lista ordenada
```

### Ventajas
- ✅ Simple de entender e implementar
- ✅ Excelente para propósitos educativos
- ✅ No requiere memoria adicional
- ✅ Es estable (mantiene orden relativo)

### Por qué Bubble Sort para este proyecto
- Ideal para **Programación 1** por su simplicidad conceptual
- Fácil de seguir y depurar
- Perfectamente adecuado para conjuntos de datos pequeños y medianos
- Demuestra claramente el concepto de algoritmos de ordenamiento

---

## Dataset Base

El archivo `paises.csv` incluido contiene datos de ejemplo de países de diferentes continentes para demostrar las funcionalidades del sistema.

---

## Notas Adicionales

- **Sin dependencias externas**: No utiliza `import csv` ni `pandas`
- **Python puro**: Implementación desde cero de todas las funcionalidades
- **Código limpio**: Comentado y siguiendo buenas prácticas
- **Interfaz amigable**: Mensajes claros y diseño visual atractivo
- **Escalable**: Fácil de extender con nuevas funcionalidades

---

## Trabajo Práctico Integrador

**Asignatura**: Programación 1  
**Institución**: Universidad Tecnológica Nacional (UTN)  
**Curso**: Tecnicatura Universitaria en Programación  
**Año**: 2025

---

**Desarrollado por Agüero Maximiliano y Dario Frison**