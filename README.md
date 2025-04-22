# Algoritmos de PRIMEROS, SIGUIENTES y PREDICCIÓN LL(1) en Python
# INTEGRANTES
- Juan Balaguera
- Juan Beltran
- Nicolas Garzon

Este proyecto implementa en Python los algoritmos clásicos para el análisis sintáctico de gramáticas independientes del contexto (GIC):

- Cálculo de **conjuntos PRIMEROS**
- Cálculo de **conjuntos SIGUIENTES**
- Construcción de la **tabla de predicción LL(1)**



---

## 📚 Contenido

- `algoritmos.py`: Código principal que define la gramática, calcula PRIMEROS, SIGUIENTES y la matriz de predicción.


---

## ⚙️ Cómo ejecutar

### 1. Requisitos

Asegúrate de tener Python 3 instalado:

```bash
python3 --version
python3 algoritmos.py
```
# SALIDA
```bash
=== PRIMEROS ===
PRIMEROS(E) = {'id', '('}
PRIMEROS(E') = {'+', 'ε'}
PRIMEROS(T) = {'id', '('}
PRIMEROS(T') = {'*', 'ε'}
PRIMEROS(F) = {'id', '('}

=== SIGUIENTES ===
SIGUIENTES(E) = {')', '$'}
SIGUIENTES(E') = {')', '$'}
SIGUIENTES(T) = {'+', ')', '$'}
SIGUIENTES(T') = {'+', ')', '$'}
SIGUIENTES(F) = {'+', ')', '$', '*'}

=== MATRIZ DE PREDICCIÓN LL(1) ===
PREDICCION(E, 'id') = T E'
PREDICCION(E, '(') = T E'
PREDICCION(E', '+') = + T E'
PREDICCION(E', ')') = ε
PREDICCION(E', '$') = ε
PREDICCION(T, 'id') = F T'
PREDICCION(T, '(') = F T'
PREDICCION(T', '+') = ε
PREDICCION(T', ')') = ε
PREDICCION(T', '$') = ε
PREDICCION(T', '*') = * F T'
PREDICCION(F, 'id') = id
PREDICCION(F, '(') = ( E )









