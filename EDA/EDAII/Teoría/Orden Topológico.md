#### DFS
Al construir el bosque abarcador en profundidad de un grafo dirigido la clasificación de los arcos varía. Además de los arcos de árbol y arcos de retroceso aparecen dos nuevos tipos de arcos:
- Arcos de avance: Van **desde un ancestro hacia un descendiente propio** en un cierto árbol del bosque abarcador.
- Arcos de cruce: Conectan un vértice a otro que **no es ni descendiente propio, ni antecesor de él en el bosque abarcador** (o sea, ni hacia abajo ni hacia arriba). Pueden ir **de una rama a otra de un mismo árbol o de árboles diferentes**.


#### Orden Topológico
Un orden topológico de un grafo dirigido y **acíclico** $G = \langle V,E \rangle$ es **una ordenación lineal de todos sus vértices**, de manera tal que si el arco $\langle u,v \rangle$ está en $E$, entonces el vértice $u$ aparece antes que el vértice $v$ en el orden lineal establecido.

**Observación**: No tiene sentido hablar de esta ordenación si en el grafo hay ciclos, pues la misma no sería posible de obtener.

La ordenación topológica puede verse como una ordenación de los vértices del grafo a través de una línea horizontal de manera tal que la dirección de todos los arcos es de izquierda a derecha.

##### Pseudocódigo
```python
def DFS(G):
	n = len(V(G))
	visited = [False] * n
	pi = [None] * n
	stack = []
	
	for v in V(G):
		DFS_Visit_Topological_Sort(G,v)
		
def DFS_Visit_Topological_Sort(G,u):
	visited[u] = True
	time = time + 1
	d[u] = time

	for v in neighbors(u):
		if not visited[v]
			pi[v] = u
			DFS_Visit_Topological_Sort(G,v)
	
	time = time + 1
	f[u] = time
	stack.Push(u)
	return
```
##### Complejidad Temporal
- $O(|V|+|E|)$ 
#### Marco Teórico

##### Lema
Un grafo dirigido $G$ es acíclico si y solo si tras realizar un $DFS$ sobre el mismo no aparecen arcos de retroceso.

**Demostración**:
$(\implies)$ **Acíclico** $\implies$ **No arcos de retroceso**
Supongamos que tras el $DFS$ aparece un arco de retroceso $\langle u,v \rangle$. Entonces el vértice $v$ es un ancestro del vértice $u$ en el bosque primero en profundidad que se genera. Por tanto, $G$ contiene un camino de $v$ a $u$ y el arco de retroceso completa un ciclo, lo cual es una contradicción porque $G$ es acíclico.

$(\impliedby)$ **No arcos de retroceso** $\implies$ **acíclico**
Supongamos que en $G$ existe un ciclo c. Sea $v$ el primer vértice en $c$ que fue descubierto. Sea $\langle u,v \rangle$ el arco precedente en $c$. En el instante $d[v]$ los restantes vértices de $c$ son blancos, por tanto, $u$ es un descendiente de $v$ en el árbol abarcador en profundidad, por tanto $\langle u,v \rangle$ es un arco de retroceso, lo cual es una contradicción, pues en $G$ no hay arcos de retroceso.

#### Teorema
$DFS\_Visit\_Topological\_Sort(G,u)$ calcula un orden topológico de un $DAG$ $G$.

**Demostración**: Supongamos que $DFS$ se ejecuta sobre un $DAG$ $G = \langle V,E \rangle$. EN el cual se calcula $f[x], \forall x \in V(G)$. Sería suficiente demostrar que para cualquier par de vértices $u,v \in V(G)$, si existe en $G$ un arco $\langle u,v \rangle$, entonces tras el $DFS$ $f[v] < f[u]$.

Consideremos cualquier arco $\langle u,v \rangle$ explorado durante el $DFS(G)$. Cuando esto sucede:
- $v$ no puede ser gris, pues en tal caso, $v$ sería ancestro de $u$ y el arco $\langle u,v \rangle$ sería un arco de retroceso (contradice el [[Orden Topológico#Lema]] pues $G$ es un $DAG$). Por tanto $v$ tiene que ser blanco o negro.
- Si es blanco, se convierte en un descendiente de $u$ y por ello $f[v] < f[u]$.
- Si $v$ fuese negro, entonces ya se terminó de analizar y por tanto $f[v]$ ya se calculó. Como aún estamos explorando arcos desde $u$, entonces cuando el análisis finalice y se calcule $f[u]$, entonces se cumplirá también $f[v] < f[u]$.

Por tanto, para cualquier arco $\langle u,v \rangle$ en el $DAG$ se cumplirá que $f[v] < f[u]$.

#### Otra variante del Algoritmo de Orden Topológico

Por cada vértice $v \in V(G)$ con $indeg(v) = 0$, eliminar dicho vértice y todas las aristas que salen de él hasta que $V$ y $E$ sean vacíos.

En cada iteración se elimina de $G$ un vértice $v$ con $indeg(v) = 0$ y todos los arcos que salen de él. La secuencia de vértices que se van eliminando van conformando un orden topológico de $G$.

##### Problema

**Dada una ordenación lineal de los vértices de** $G = \langle V,E \rangle$ poder determinar si esta es un Orden Topológico para $G$.

**R/** Vamos por cada vértice $v$ de la lista de izquierda a derecha y si $indeg(v) = 0$ entonces lo eliminamos a él y a todos los vértices sobre los que el mismo incide. 
Si en algún punto encontramos $v \in L: indeg(v) \neq 0$, entonces $L$ no es un orden topológico para $G$.

# Teorema

Existe un orden topológico en $G \iff G$ es un $DAG$. 