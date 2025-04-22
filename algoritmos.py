# Gramática definida como diccionario
gramatica = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F": [["(", "E", ")"], ["id"]]
}

# Diccionarios para PRIMEROS, SIGUIENTES y tabla de predicción
primeros = {}
siguientes = {}
tabla_prediccion = {}

# Inicialización de estructuras
for nt in gramatica:
    primeros[nt] = set()
    siguientes[nt] = set()
    tabla_prediccion[nt] = {}

# Función para saber si un símbolo es terminal
def es_terminal(simbolo):
    return not simbolo.isupper() and simbolo != 'ε'

# Función para calcular PRIMEROS
def calcular_primeros(simbolo):
    if simbolo == 'ε':
        return {'ε'}
    if es_terminal(simbolo):
        return {simbolo}
    if primeros[simbolo]:
        return primeros[simbolo]

    for produccion in gramatica[simbolo]:
        for s in produccion:
            if s == 'ε':
                primeros[simbolo].add('ε')
                break
            primeros_s = calcular_primeros(s)
            primeros[simbolo].update(primeros_s - {'ε'})
            if 'ε' not in primeros_s:
                break
        else:
            primeros[simbolo].add('ε')
    return primeros[simbolo]

# Función para calcular PRIMEROS de una secuencia
def calcular_primeros_de_secuencia(secuencia):
    resultado = set()
    for simbolo in secuencia:
        primeros_simbolo = calcular_primeros(simbolo)
        resultado.update(primeros_simbolo - {'ε'})
        if 'ε' not in primeros_simbolo:
            break
    else:
        resultado.add('ε')
    return resultado

# Calcular PRIMEROS de todos los no terminales
for nt in gramatica:
    calcular_primeros(nt)

# Calcular SIGUIENTES
inicio = list(gramatica.keys())[0]
siguientes[inicio].add('$')  # Símbolo de fin de entrada

cambio = True
while cambio:
    cambio = False
    for A in gramatica:
        for produccion in gramatica[A]:
            for i, B in enumerate(produccion):
                if not B.isupper():
                    continue
                beta = produccion[i + 1:]
                primeros_beta = calcular_primeros_de_secuencia(beta)
                antes = len(siguientes[B])
                siguientes[B].update(primeros_beta - {'ε'})
                if 'ε' in primeros_beta or not beta:
                    siguientes[B].update(siguientes[A])
                if len(siguientes[B]) > antes:
                    cambio = True

# Construcción de la tabla de predicción LL(1)
for nt in gramatica:
    for produccion in gramatica[nt]:
        primeros_prod = calcular_primeros_de_secuencia(produccion)
        for terminal in primeros_prod - {'ε'}:
            tabla_prediccion[nt][terminal] = produccion
        if 'ε' in primeros_prod:
            for terminal in siguientes[nt]:
                tabla_prediccion[nt][terminal] = produccion

# Mostrar PRIMEROS
print("=== PRIMEROS ===")
for nt in primeros:
    print(f"PRIMEROS({nt}) = {primeros[nt]}")

# Mostrar SIGUIENTES
print("\n=== SIGUIENTES ===")
for nt in siguientes:
    print(f"SIGUIENTES({nt}) = {siguientes[nt]}")

# Mostrar tabla de predicción LL(1) con formato amigable
print("\n=== MATRIZ DE PREDICCIÓN LL(1) ===")
for nt in tabla_prediccion:
    for terminal in tabla_prediccion[nt]:
        produccion = tabla_prediccion[nt][terminal]
        prod_str = " ".join(produccion)
        print(f"PREDICCION({nt}, '{terminal}') = {prod_str}")
