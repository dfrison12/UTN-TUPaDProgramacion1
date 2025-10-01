# Generador de tabla de verdad (1..3 vars) SIN XOR
# Paso 1: cantidad de variables (1, 2 o 3)
# Paso 2: por cada variable, elegir si va negada (NOT)
# Paso 3: entre variables, elegir conector (AND/OR)
# Luego arma la expresión y genera la tabla.

print("=== Generador de Tabla de Verdad (AND/OR) ===")

# ---- Paso 1: cantidad de variables (1..3) ----
n = 0
while True:
    s = input("¿Cuántas variables? (1, 2 o 3): ").strip()
    if s.isdigit():
        n = int(s)
        if n in [1, 2, 3]:
            break
    print("Entrada inválida. Debe ser 1, 2 o 3.")

vars_all = ["A", "B", "C"]
vars_used = vars_all[:n]

# ---- Paso 2: negación por variable ----
neg = [0] * n  # 1 = NOT, 0 = normal
i = 0
while i < n:
    ans = input(f"¿Negar {vars_used[i]}? (S/N): ").strip().upper()
    if ans == "S":
        neg[i] = 1
        i += 1
    elif ans == "N":
        neg[i] = 0
        i += 1
    else:
        print("Respuesta inválida. Escribí S o N.")

# ---- Paso 3: conectores entre variables (n-1 conectores) ----
# Mapeo: 1 AND, 2 OR
def_conn_txt = ["", "AND", "OR"]
def_py_op     = ["", "and", "or"]

conns = []  # guardo índices 1..2
if n >= 2:
    print("\nElegí conectores entre variables:")
    print("1) AND   (a and b)")
    print("2) OR    (a or  b)")

    k = 0
    while k < (n - 1):
        s = input(f"Conector entre {vars_used[k]} y {vars_used[k+1]} (1..2): ").strip()
        if s.isdigit():
            op = int(s)
            if 1 <= op <= 2:
                conns.append(op)
                k += 1
                continue
        print("Entrada inválida. Debe ser 1 o 2.")

# ---- Construcción de la expresión (string) ----
# Termino cada variable con o sin NOT
terms = []
i = 0
while i < n:
    if neg[i] == 1:
        terms.append(f"not {vars_used[i]}")
    else:
        terms.append(vars_used[i])
    i += 1

# Plegado izquierda con paréntesis según conectores elegidos
# Ej: (((term0 op0 term1) op1 term2) ...)
if n == 1:
    expr = terms[0]
else:
    expr = f"({terms[0]} {def_py_op[conns[0]]} {terms[1]})"
    i = 2
    idx_conn = 1
    while i < n:
        expr = f"({expr} {def_py_op[conns[idx_conn]]} {terms[i]})"
        i += 1
        idx_conn += 1

print("\n=== Expresión final (Python) ===")
print(expr)

# ---- Generación de la tabla de verdad ----
header = " ".join(vars_used)
print("\n=== Tabla de Verdad ===")
print(f"{header} | {expr}")
print("-" * (len(header) + 3 + len(expr)))

# total combinaciones = 2^n
total = 1
i = 0
while i < n:
    total *= 2
    i += 1

fila = 0
while fila < total:
    # asigno True/False a cada variable según bits
    ctx = {}
    i = 0
    while i < n:
        bit = (fila >> (n - 1 - i)) & 1
        ctx[vars_used[i]] = True if bit == 1 else False
        i += 1

    # eval controlado (sin builtins)
    try:
        res = eval(expr, {"__builtins__": None}, ctx)
    except Exception:
        print("Error al evaluar la expresión. Revisá entradas.")
        break

    # imprimo 0/1
    izq = []
    i = 0
    while i < n:
        izq.append("1" if ctx[vars_used[i]] else "0")
        i += 1
    print(f"{' '.join(izq)} | {'1' if res else '0'}")

    fila += 1

print("\nListo. Volvé a ejecutar para otra combinación de negaciones y conectores (AND/OR).")
