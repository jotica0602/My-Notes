# Ejercicio 8

Dado un grafo dirigido y acíclico $G = \langle V,E \rangle$ y un vértice $s \in V$, diseñe un algoritmo que determine $\forall u \in V(G)$ la longitud del camino de longitud máxima que va de $s$ a $u$. La complejidad temporal de su algoritmo debe ser $O(|V| + |E|)$.

a) ¿Cómo se puede modificar su algoritmo para encontrar la longitud del camino de longitud máxima que va de $u$ a $s$ para todo vértice $u$?

## Solución

El grafo es dirigido y acíclico, por lo que en él se puede establecer un orden topológico:
Ahora, tengamos en cuenta las siguientes definiciones:
- La distancia mínima de $s$ a $s$ es $0$.
- Para todo vértice $w$ alcanzable desde $s$, diremos que la distancia máxima de $s$ a $w$ será igual al máximo de la distancia entre la distancia calculada hasta $w$ y 1 más la distancia calculada desde $s$ a algún vértice que $u$ cuya arista incida en $w$. O sea:$$
	max\set{d(v),1 + d(w))} | \langle w,v \rangle \in E(G)
	$$
- Diremos que todo vértice no alcanzable por $s$ tendrá distancia máxima $-\infty$.

O sea, estamos definiendo una función $F$ de la siguiente forma:

$$
F(v) =
\begin{cases}
0,                                       && \text{si } v = s \\
-\infty,                                 && \text{si } indeg(v) = 0 \\
1 + max_{w_i | \langle w_i,v \rangle \in E(G)} F(w_i), && \text{e.o.c}
\end{cases}
$$
De esta forma el pseudocódigo podría ser:

```python nums

DP_DAG(G,s):
	ts = Topological_Sort(G)
	f[-oo for v in V(G)]
	f[s] = 0
	for v in ts:
		for w in in_neighbors(v):
			f[v] = max(f[v], 1+f[w])

	return f
```

### Inciso a)

Notemos que existe una biyección entre todos los caminos que empiezan en $v$ en $G$ y los que terminan en $v$ en $G^T$, por lo que ambos tienen la misma longitud. Por tanto se puede buscar el máximo en el conjunto de los caminos que empiezan en $s$ en $G^T$

![[Drawing 2024-09-25 16.47.56.excalidraw]]