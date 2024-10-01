# Algoritmo de Floyd-Warshall

Resuelve el problema de las **rutas más cortas** en un grafo ponderado. Su objetivo es encontrar la distancia más corta entre todos los pares de vértices del grafo, es decir, calcula el camino más corto entre cualquier par de nodos.

## Idea general del algoritmo

El algoritmo parte de la siguiente observación: si queremos encontrar el camino más corto entre dos nodos `i` y `j`, podemos hacerlo al pasar por un tercer nodo intermedio `k`. La idea clave es ir revisando si pasar por el nodo `k` mejora la distancia entre `i` y `j`.

El algoritmo usa una **matriz de distancias**, donde la entrada `d[i][j]` representa la distancia más corta conocida entre el nodo `i` y el nodo `j`. Al principio, la matriz se inicializa con las distancias directas entre los nodos (es decir, los pesos de las aristas), o infinito si no hay un camino directo.

Luego, el algoritmo itera sobre todos los nodos posibles, y en cada iteración trata de mejorar la distancia entre los nodos `i` y `j` considerando si pasar por el nodo `k` da un camino más corto.

## Significado de los índices (`k`, `i`, `j`)

- **`k`**: Representa el nodo intermedio que estamos considerando en esa iteración. En otras palabras, en el paso `k`, estamos verificando si la distancia entre los nodos `i` y `j` puede ser más corta al pasar por el nodo `k`.

- **`i`**: Representa el nodo de inicio del par que estamos evaluando (el origen).

- **`j`**: Representa el nodo de destino del par que estamos evaluando (el destino).

En cada iteración del algoritmo, se actualiza la distancia entre `i` y `j` con la siguiente fórmula:

$$
d[i][j] = \min(d[i][j], d[i][k] + d[k][j])
$$

Esto significa que la nueva distancia entre `i` y `j` será la menor entre la distancia actual `d[i][j]` y la distancia que se obtiene pasando por el nodo intermedio `k` (es decir, `d[i][k] + d[k][j]`).

## Explicación paso a paso del proceso

1. **Inicialización**: Al inicio, la matriz de distancias `d[i][j]` se inicializa con los pesos de las aristas. Si no existe una arista entre dos nodos, se usa el valor infinito (`∞`). Si un nodo es el mismo (distancia de un nodo a sí mismo), la distancia es 0.

2. **Iteraciones sobre `k`**: El algoritmo itera sobre cada nodo `k` y trata de usar `k` como un nodo intermedio para mejorar las distancias entre todos los pares de nodos `(i, j)`.

    - Para cada nodo `i` (nodo de origen).
    - Para cada nodo `j` (nodo de destino).
    - Se verifica si pasar por el nodo intermedio `k` mejora la distancia entre `i` y `j`, comparando `d[i][j]` con `d[i][k] + d[k][j]`.

3. **Actualización**: Si se encuentra que `d[i][k] + d[k][j]` es menor que `d[i][j]`, se actualiza la distancia entre `i` y `j`.

## Finalización

Después de que el algoritmo haya considerado todos los nodos como posibles intermediarios (`k`), la matriz `d[i][j]` contendrá las distancias más cortas entre todos los pares de nodos.

## Resumen

El índice:
- **`i`**: Nodo de origen del par de nodos que estamos considerando.
- **`j`**: Nodo de destino del par de nodos que estamos considerando.
- **`k`**: Nodo intermedio que se está usando para intentar mejorar el camino entre `i` y `j`.

El algoritmo explora todas las combinaciones de pares de nodos y se asegura de que cualquier camino más corto que pase por nodos intermedios sea considerado. Al finalizar, la matriz contiene la solución al problema de caminos más cortos entre todos los pares de nodos del grafo.

## Código
```python
def floyd_warshall(graph):
    # Número de nodos en el grafo
    n = len(graph)
    
    # Inicializar la matriz de distancias con los valores del grafo
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    # Aplicar el algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Actualizar la distancia entre i y j al mínimo valor posible
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

# Algoritmo de Warshall


El **algoritmo de Warshall** se utiliza para encontrar la **clausura transitiva** de un grafo dirigido. La clausura transitiva de un grafo es otro grafo que contiene todas las conexiones directas e indirectas posibles entre los nodos. En otras palabras, si existe un camino de un nodo `i` a un nodo `j`, entonces debe existir una arista directa entre `i` y `j` en la clausura transitiva.

El objetivo del algoritmo de Warshall es determinar si existe un camino entre cada par de nodos en un grafo dirigido. Para hacer esto, convierte una **matriz de adyacencia** en una **matriz de accesibilidad**, donde cada entrada `(i, j)` en la matriz será `1` si existe un camino del nodo `i` al nodo `j`, y `0` si no existe tal camino.

### Pasos del algoritmo

El algoritmo parte de la **matriz de adyacencia** `A`, donde `A[i][j] = 1` indica que existe una arista directa entre el nodo `i` y el nodo `j`, y `A[i][j] = 0` indica que no hay conexión directa.

El algoritmo realiza varias iteraciones considerando nodos intermedios para ver si se puede llegar de un nodo `i` a un nodo `j` indirectamente pasando por otro nodo `k`.

La regla que aplica el algoritmo es la siguiente:

$$
A[i][j]=A[i][j] OR (A[i][k] AND A[k][j])A[i][j] = A[i][j] \, \text{OR} \, (A[i][k] \, \text{AND} \, A[k][j])A[i][j]=A[i][j]OR(A[i][k]ANDA[k][j])
$$

Esto significa que si ya existe una conexión directa entre `i` y `j` (es decir, `A[i][j] = 1`), o si se puede llegar a `j` desde `i` pasando por un nodo intermedio `k` (es decir, `A[i][k] = 1` y `A[k][j] = 1`), entonces `A[i][j]` debe ser 1.

### Significado de los índices (`k`, `i`, `j`)

- **`i`**: Nodo de origen del par que estamos considerando.
- **`j`**: Nodo de destino del par que estamos considerando.
- **`k`**: Nodo intermedio que estamos evaluando para ver si mejora la conectividad entre `i` y `j`.

### Pasos del algoritmo:

1. **Inicialización**: La matriz de adyacencia `A` es la entrada del algoritmo.
    
2. **Iteraciones**: Para cada nodo intermedio `k`, verificamos para cada par de nodos `(i, j)` si el nodo `k` puede mejorar la conectividad entre `i` y `j`.
    
3. **Actualización**: Si el nodo `k` permite conectar `i` con `j`, actualizamos `A[i][j]` a `1`.
    
4. **Resultado**: Después de las iteraciones, la matriz `A` se convierte en la **matriz de accesibilidad**, que representa la clausura transitiva del grafo original.

```python
def warshall_transitive_closure(graph): 
	# Número de nodos en el grafo 
	n = len(graph)
	# Inicializar la matriz de accesibilidad con los valores del grafo 
	reachable = [[graph[i][j] for j in range(n)] for i in range(n)] 
	# Aplicar el algoritmo de Warshall 
	for k in range(n): 
		for i in range(n): 
			for j in range(n): 
				# Actualizar si es posible llegar de i a j pasando por k 
				reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j]) 
	return reachable
```