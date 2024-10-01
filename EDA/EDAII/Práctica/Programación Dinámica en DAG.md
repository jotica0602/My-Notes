Muchos son los problemas sobre grafos en los que **computando una función por cada vértice** del mismo se **obtiene la solución**. Un subconjunto de estas funciones, que atrapan gran parte de los problemas a resolver sobre grafos, se calculan exclusivamente en función de los vértices que inciden en un vértice en cuestión. Esto es, dado un grafo $G$ y un vértice $v$ de $G$:

$$
F(v) = 
\begin{cases}
Op(X),       && \text{ si } indegree(v) > 0 \\
Valor\_Base, && \text{ en otro caso}
\end{cases}
$$

donde $X$ es la secuencia $\set{F(w) | \langle w,v \rangle \in E(G)}$.

**Si el grafo $G$ es un DAG**, existe un **algoritmo genérico** que **nos permite computar una función** $\mathbf{F}$ con estas propiedades. Notemos que la única condición necesaria para computar iterativamente la función $F$ sobre los vértices de $G$, es que **cuando se visite un vértice** $v$, **los valores** de $F(w_i)$ ya **se hayan calculado correctamente** $\forall w_i | \langle w_i,v \rangle \in E(G)$. Esto lo podemos lograr exactamente **recorriendo los vértices en un orden topológico** de $G$.

```python nums
def DP_DAG(G):
	ts <-- Topological_Sort(G)
	f[v] <-- Valor Base
	for v in ts:
		v <-- ts[i]
		f[v] <-- F(v)
	
	return f
```

Al enfrentarnos a un problema en específico solamente necesitamos sustituir la línea 6 por un código que compute correctamente la función $F$ en el vértice $v$ y lo guarde en $f[v]$. Y a la hora de explicar un ejercicio de este tipo, solo será necesario definir $F(v)$ correctamente en función de los vértices que inciden en $v$.

#### Complejidad Temporal
- $O(|V| + |E|)$
