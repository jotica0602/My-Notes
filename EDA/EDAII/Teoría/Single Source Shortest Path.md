#### Problema

Dado un grafo $G = \langle V,E \rangle$ dirigido y ponderado, encontrar el **camino de costo mínimo** desde un **vértice origen** $s \in V$ hasta los restantes vértices de $V$.

**Colateralmente podemos resolver otros problemas como**:
- Encontrar el camino de costo mínimo desde cada vértice del grafo a un vértice de destino $v$ de $G$.
- Hallar el camino de costo mínimo entre un par de vértices dados $u$ y $v$ de $G$.
- Encontrar el camino de costo mínimo entre $u$ y $v$ para cualquier par de vértices $u$ y $v$ de $G.$


#### Consideraciones para el problema de los caminos de costo mínimo

El grafo en cuestión $G = \langle V,E \rangle$ es dirigido, ponderado y $s \in V(G)$ es el vértice de origen.

##### Camino de costo mínimo
Sea $p$ un camino de la forma $p = \langle v_0,...,v_k\rangle, v_i \in V(G)$, el costo del camino se define de la siguiente forma:
$$
w(p) = \sum_{i=1}^{k}w(\langle v_{i-1},v_i \rangle)
$$

El costo del camino de costo mínimo de $u$ a $v$, denotado por $\delta(u,v)$ se define de la siguiente forma:

$$
\delta(u,v) = 
\begin{cases}
min\set{w(p):u \stackrel{p}{\to} v}, && \text{si existe un camino de } u \text{ a } v\\
\infty, && \text{en otro caso}
\end{cases}
$$

Un **camino de costo mínimo** de $u$ a $v$ es cualquier camino $p$ de $u$ a $v$ tal que $w(p) = \delta(u,v)$.

El camino de costo mínimo **no es único**.

##### Subestructura óptima de un camino de costo mínimo
Los algoritmos relacionados con el problema de los caminos de costo mínimo se basan fundamentalmente en la siguiente propiedad:

> Todo camino de costo mínimo entre dos vértices contiene dentro de sí otros caminos de costo mínimo.

##### Arcos de costo negativo
En este tipo de problemas no se excluye la posibilidad de que en el grafo **existan arcos de costo negativo**.

> Si existe un ciclo de costo negativo alcanzable desde $s$ entonces los caminos de costo mínimo no están bien definidos.

- Si existe un ciclo de costo negativo sobre algún camino de $s$ a $v$ entonces se define $\delta(s,v) = -\infty$
- Si $v$ **no** es alcanzable desde $s$ entonces $\delta(s,v) = \infty$
#### Algoritmos que dan solución al problema
- Algoritmo de Dijkstra:
	Asume que el costo de todos los arcos del grafo son **no negativos**.
- Algoritmo $DAG$ y Bellman-Ford:
	En el grafo pueden haber arcos de costo negativo. Resuelve el problema de manera correcta, siempre y cuando en dicho grafo no existan ciclos de costo negativo alcanzables desde el origen.


#### Existencia de ciclos en el camino de costo mínimo

Sea $p$ camino que contiene a un ciclo $c$ en él, $p =\langle v_0,\dots,\underbrace{\boxed{v_i,v_j=v_i}}_{w(c)>0},v_{j+1},\dots,v_k\rangle$. 
¿Podría ser $p$ de costo mínimo?

R\\ No, pues podríamos crear $p' = \langle v_0,v_1,\dots,v_j,v_{j+1},\dots,v_k \rangle$ con $w(p') = w(p) - w(c) < w(p)$, por tanto $p$ no es de costo mínimo.

Ahora, si $w(c) = 0$ también podríamos encontrar $p'$ camino simple con el mismo costo que $p$ que contiene a un ciclo.

Por consiguiente podemos asumir que:

> Cuando estamos encontrando caminos de costo mínimo, en ellos no hay ciclos.

#### Relax
Se basa en emplear un array $d[v]$, que es el costo mínimo estimado hasta el vértice $v$, y representa la **cota superior** para el costo del camino de costo mínimo de $s$ a $v$.

$d[v]$ se inicializa con el siguiente método cuya complejidad temporal es $O(|V|)$.

```python
def initialize_single_source(G,s):
	for v in V(G):
		d[v] = oo
		pi[v] = None
	d[s] = 0
```

**Relax** se aplica sobre los arcos y su funcionalidad se basa en preguntar si es posible mejorar el costo del camino para ir desde $s$ hasta $v$ hasta ahora **asumido** como mínimo ($d[v]$) pasando por el vértice $u$. Si es posible entonces se actualiza $d[v]$ y $\pi[v]$.
```python
relax(u,v,w):
	if (d[v] > d[u] + w(u,v)):
		d[v] = d[u] + w(u,v)
		pi[v] = u
```

> Los algoritmos difieren entre sí en el número de veces y en el orden en que se aplica **Relax** a los arcos:

1. En Dijkstra y en el *DAG* a cada arco se le hace **Relax** exactamente **una sola vez**.
2. En Bellman-Ford se aplica **Relax** varias veces.

#### Propiedades

##### Desigualdad triangular
 Para todo arco $\langle u,v \rangle \in E$ se cumple que: 
 
$$
\delta(s,v) \leq \delta(s,u) + w(u,v)
$$

**Demostración**:
Supongamos que existe un camino $p$ de costo mínimo de $s$ a $v$. Entonces $w(p) \leq w(p')$, donde $p'$ es cualquier otro camino de $s$ a $v$. En particular no puede tener un costo mayor que $p' = \langle v_0 = s, \dots, v_k=u \rangle + \langle u,v \rangle$. Por tanto:
$$
w(p) \leq w(p') \implies \delta(s,v) \leq \delta(s,u) + w(u,v). \text{ }\blacksquare$$

##### Propiedad de la Cota Superior
Para todo $v \in V(G)$ se cumple que 
$$
d[v] \geq \delta(s,v)$$
y una vez que $d[v]$ alcanza el valor $\delta(s,v)$ este no varía nunca más.

**Demostración**:
Demostremos por inducción, sobre la cantidad de pasos de relajación que se cumple la invariante :

$$
d[v] \geq \delta(s,v), \forall v \in V(G)
$$

**Caso base**:
Tras las inicializaciones se cumplirá la invariante, pues:

$$
d[v] = \infty, \forall v \in V(G) - \set{s} \implies d[v] \geq \delta(s,v)
$$
Para el caso del origen $s$ :

$$
d[s] = 0 \geq \delta(s,s)
$$
- Si $s$ está sobre un ciclo de costo negativo, $\delta(s,s) = -\infty \implies 0 > -\infty$
- En otro caso $\delta(s,s) = 0 \implies 0 = 0$

**Paso Inductivo**: 
Consideremos el momento en el que se hace **Relax** a un arco $\langle u,v \rangle$.

Por hipótesis de inducción

$$
d[x] \geq \delta(s,x), \forall x \in V(G)
$$

antes de hacer `relax(u,v,w)`.

Tras `relax(u,v,w)` el único valor que podría cambiar es $d[v]$ y si así fuera:
$$
d[v] = d[u] + w(u,v) 
$$

$$
d[u] + w(u,v) \geq \boxed{\delta(s,u) + w(u,v)}
$$

Pues por hipótesis de inducción $d[u] \geq \delta(s,u)$, observemos que $d[u]$ en dicho instante puede **no ser** el menor costo hasta $u$ y por tanto seguirá siendo mayor que el menor costo.

$$
d[u] + w(u,v) \geq \delta(s,u) + w(u,v) \geq \boxed{\delta(s,v)}
$$

Por [[#Desigualdad triangular]].

Por tanto se cumple la invariante.
Además, una vez se alcanza la igualdad $d[v] = \delta(s,v), d[v]$ alcanzó el valor de su cota inferior y este valor nunca cambiará, pues hemos demostrado que $d[v] \geq \delta(s,v)$ y la única modificación posible que podría hacer **Relax** al valor $d[v]$ sería disminuirlo. $\blacksquare$

##### Propiedad de la no existencia de camino
Si no existe camino de $s$ a $v$ entonces el valor de $d[v]$ se mantendrá invariante y se cumplirá que

$$
d[v] = \delta(s,v) = \infty
$$
**Demostración**:
Por la [[#Propiedad de la Cota Superior]] tenemos que $d[v] = \infty \geq \delta(s,v)$ y por tanto $d[v] = \infty = \delta(s,v)$.


##### Lema
Sea $\langle u,v \rangle \in E$. Inmediatamente después de hacer `relax(u,v,w)` se cumple:

$$
d[v] \leq d[u] + w(u,v)
$$

**Demostración**:
Si antes de hacer `relax(u,v,w)`:
- $d[v] > d[u] + w(u,v)$ tras hacerlo $d[v] = d[u] + w(u,v)$
- $d[v] \leq d[u] + w(u,v)$ tras hacerlo $d[v]$ no cambia, por tanto la desigualdad $d[v] \leq d[u] + w(u,v)$ se mantiene.

##### Propiedad de la Convergencia
Si $p = \langle s,\dots,u,v \rangle$ es un camino de costo mínimo en $G$, $u,v \in V(G)$. Si se alcanza la igualdad $d[u] = \delta(s,u)$ en cualquier momento antes de hacer **Relax** sobre el arco $\langle u,v \rangle$, entonces después de haberlo hecho $d[v] = \delta(s,v)$ y dicha igualdad se mantiene en lo sucesivo.

**Demostración**:
Si antes de hacer `relax(u,v,w)` se alcanza la igualdad $d[u] = \delta(s,u)$ entonces la misma se mantiene en lo sucesivo por [[#Propiedad de la Cota Superior]].

En particular, tras hacer `relax(u,v,w)`:

$$
d[v] \leq d[u] + w(u,v) = \delta(s,u) + w(u,v) = \delta(s,v)
$$

Por tanto $d[v] \leq \delta(s,v)$

Por [[#Propiedad de la Cota Superior]]

$$
d[v] \geq \delta(s,v)
$$

Luego, como $d[v] \leq d[u]$ y $d[v] \geq d[u] \implies d[u] = d[v]$ y la igualdad se mantiene en lo sucesivo.

##### Propiedad del Relax
Si $p = \langle v_0,v_1,\dots,v_k \rangle$ es un **camino de costo mínimo** de $s = v_0$ a $v_k$ y supongamos que a los arcos de $p$ se les aplica **Relax** en el siguiente orden:

$$
\langle v_0,v_1 \rangle, \langle v_1,v_2 \rangle, \dots, \langle v_{k-1}, v_k \rangle
$$
entonces $d[v_k] = \delta(s,v_k)$ después de estas relajaciones. Este propiedad se cumple incluso cuando se mezcle el **Relax** sobre otros arcos con los arcos de $p$. (Notemos que $k$ puede ser $0,1,\dots,|V|-1$).

**Demostración**:
Demostremos por inducción que tras el $i$-ésimo **Relax** sobre un arco de $p$, se cumple $d[v_i] = \delta(s,v_i)$.

**Caso base**
$i = 0$
Antes de hacer **Relax** a ningún arco de $p$, tenemos como resultado de la inicialización $d[v_0] = d[s] = 0 = \delta(s,s)$ y por la [[#Propiedad de la Cota Superior]] el valor de $d[s]$ no cambia en lo sucesivo.

**Paso Inductivo**:
Asumimos que $d[v_{i-1}] = \delta(s,v_{i-1})$ y analicemos qué sucede tras hacer **Relax** sobre el arco $\langle v_{i-1},v_i \rangle$:

Por la [[#Propiedad de la Convergencia]], $d[v_i] = \delta(s,v_i)$ y la igualdad se mantiene en lo  sucesivo. $\blacksquare$

#### Algoritmo DAG

Permite encontrar caminos de costo mínimo desde un vértice origen en **Grafos Dirigidos y Acíclicos**.

##### Precisiones sobre el Algoritmo:
1. Establecer un **orden topológico** sobre el DAG.
2. Para cualesquiera $u,v \in V(G)$, **si existe un camino** entre $u$ y $v$, **entonces** $u$ **precede** a $v$ en el orden topológico.
3. El algoritmo hace exactamente **una sola pasada** sobre los vértices en el orden topológico establecido.
4. Cuando se procesa un vértice en particular, se aplica **Relax** a cada arco que parte de dicho vértice.

##### Pseudocódigo
```python
def DAG_SHORTEST_PATH(G,w,s):
	topological_sort_(G)
	initialize_single_source(G,s)
	for v in topological_sort:
		for u in neighbors(v):
			relax(u,v,w)
```

##### Correctitud del Algoritmo
Demostremos que $d[v] = \delta(s,v) \forall v \in V(G)$ al terminar el algoritmo.

1. Si $v$ no es alcanzable desde $s \implies d[v] = \infty$.
2. Supongamos que $v$ es alcanzable desde $s$, por tanto hay un camino de costo mínimo $p = \langle v_0, v_1, \dots, v_k \rangle$, donde $v_0 = s$ y $v_k = v$.
Como los vértices son procesados en un orden topológico, a los arcos en $p$ se les aplica **Relax** en el siguiente orden:

$$
\langle v_0,v_1 \rangle, \langle v_1,v_2 \rangle \dots \langle v_{k-1},v_k \rangle
$$

Por la [[#Propiedad del Relax]] esto implica que $d[v_i] = \delta(s,v_i)$ al terminar el algoritmo, para $i = 0,1,\dots,k$. $\blacksquare$
##### Complejidad Temporal
- $O(|V|+|E|)$ representado por una lista de adyacencia.

#### Algoritmo de Dijkstra
Resuelve el problema en grafos dirigidos y ponderados $G = \langle V,E \rangle$ donde:

> Todos los arcos **tienen un costo no negativo**, por tanto, se asume que $w(\langle u,v \rangle) \geq 0, \forall \langle u,v \rangle \in E$

##### Idea General del Algoritmo
- **Mantiene un conjunto** $S$ con los vértices para los cuales el costo del camino de costo mínimo de $s$ a ellos **ya ha sido calculado**.
- En cada iteración se selecciona un vértice $u$ tal que $u \in (V-S)$ y además cumple que $\forall v \in (V-S), \, \, d[u] \leq d[v]$
- Adiciona $u$ a $S$
- Hace **Relax** sobre todos los arcos $\langle u,v \rangle$ tales que $v \in (V-S)$ verificando si $d[v]$ mejora, llegando a $v$ desde $u$.

##### Pseudocódigo
```python
def Dijkstra(G,w,s)
	S = []
	Q = V(G) <- Build_Heap(V(G))
	while Q is not empty:
		u = extract_min(Q)
		S.append(u)
		for v in neighbors(u):
			Relax(u,v,w)
```

##### Correctitud del Algoritmo
Basta demostrar que:

$$
d[u] = \delta(s,u),\,\, \forall u \in V(G)
$$

cuando $u$ se inserta en $S$. Una vez demostrado esto se usa la [[#Propiedad de la Cota Superior]] para probar que la igualdad se mantiene después que se alcanza.

**Inicialización**:
Inicialmente $S = \emptyset$ lo que implica que se cumple la invariante.

**Mantenimiento**:
Se desea demostrar que en cada iteración $d[u] = \delta(s,u)$ para el vértice $u$ que se inserta en $S$.

Supongamos que esto no es cierto:

> Sea $u$ el **primer vértice** para el cual $d[u] \neq \delta(s,u)$ en el momento en que dicho vértice se decide insertar en el conjunto $S$.

Centraremos la atención en la situación existente en el **momento en que comienza la iteración del ciclo `while` en el cual se decide que $u$ es el vértice que va a entrar a $S$**:
- $u \neq s$
	$s$ fue el primer vértice que se insertó en $S$ y la propia inicialización garantiza que $d[s] = \delta(s,s) = 0$

- $S \neq \emptyset$ exactamente antes de que $u$ se haya insertado en $S$.

- Existe al menos un camino desde $s$ a $u$
	De lo contrario $d[u] = \delta(s,u) = \infty$ por la [[#Propiedad de la no existencia de camino]]. Esto niega lo asumido, o sea $d[u] \neq \delta(s,u)$.

Ahora: Si existe al menos un camino de $s$ a $u$ entonces existe al menos un camino de costo mínimo de $s$ a $u$. Sea $p$ dicho camino con $p = \langle \underbrace{s,...,x}_{p_1},\underbrace{y,...,u}_{p_2} \rangle$
Donde:
- $p_1$: subcamino de $s$ a $x$. (todos sus vértices están en $S$)
- $p_2$: subcamino de $y$ a $u$ (todos sus vértices están en $(V-S)$ o en $S$)
- $y$ : primer vértice en $p$ tal que $y \in (V-S)$.
- x : último vértice en $p$ tal que $x \in S$ (predecesor de $y$ en el camino $p$).

(Tanto $p_1$ como $p_2$ pueden ser de longitud $0$)

**Situación cuando se decide insertar** $u$ en $S$:
- Se tiene que cumplir que $d[y] = \delta(s,y)$
Justificación:
- $x \in S$ por tanto como asumimos que $u$ es el primer vértice para el cual $d[u] \neq \delta(s,u)$ cuando dicho vértice se adiciona a $S$, se tenía que $d[x] = \delta(s,x)$
- Cuando $x$ se insertó en $S$ al arco $\langle x,y \rangle$ se le hizo $d[y] = \delta(s,y)$ por la [[#Propiedad de la Convergencia]].
A partir de lo anterior lleguemos a una contradicción para probar $d[u] = \delta(s,u)$:
Como $y$ está antes que $u$ en $p$ camino de costo mínimo de $s$ a $u$, donde todos los arcos tienen costo no negativo, entonces:

$$
\delta(s,y) \leq \delta(s,u) \text{ (1)}
$$

$$
d[y] = \delta(s,y) \leq \delta(s,u) \leq d[u]
$$
Por [[#Propiedad de la Cota Superior]].

Como $u$ y $v$ estaban en $(V-S)$ en el momento en que $u$ fue seleccionado, entonces $d[u] \leq d[y]$ y teniendo (1) en cuenta, entonces:

$$
d[u] \leq d[y] = \delta(s,y) \leq \delta(s,u) \leq d[u]
$$
Por tanto:
$$
d[u] = d[y] = \delta(s,y) = \delta(s,u)
$$
Lo cual es una contradicción

**Finalización**:
Al terminar el algoritmo $Q = \emptyset$ lo cual a partir de la invariante $Q = (V-S)$ implica que $S = V$. Por tanto:
$$
d[u] = \delta(s,y), \, \forall u \in V(G). \blacksquare
$$
##### Complejidad Temporal
- $O(|E|\log|V|)$
- $O(|V|^2 \log|V|)$ para grafos densos.

En ambos casos se asume que la implementación utiliza un heap binario.

#### Bellman-Ford

##### Características
- Permite que hayan arcos de costo negativo.
- Se aplica **Relax** varias veces sobre cada arco del grafo.

##### Principio de Funcionamiento
- Determina si desde el origen se alcanza algún ciclo de costo negativo: Si esto sucede, retorna *False*
- En otro caso retorna *True*. Además halla el costo y determina el camino de costo mínimo entre $s$ y los restantes vértices del Grafo.

##### Funcionamiento
A partir de la inicialización hecha con *initialize_single_source*, el algoritmo va reduciendo, progresivamente a través de sucesivas aplicaciones de **Relax** sobre los arcos de $G$, el costo estimado del camino de costo mínimo de $s$ a $v$ hasta que éste alcanza su valor real.

##### Pseudocódigo
```python
def Bellman_Ford(G,w,s):
	n = len(V(G))
	initialize_single_source(G,s)
	for i in range(n):
		for e in E(G):
			u,v = e[0], e[1]
			relax(u,v,w)        #aplica relax n-1 veces
	for e in E(G):
			u,v = e[0], e[1]
		if d[v] > d[u] + w(u,v) #detectando ciclos de costo negativo
			return False
	return True
```

##### Detección de ciclos de costo negativo
Si en la porción de código
```python
for e in E(G):
			u,v = e[0], e[1]
		if d[v] > d[u] + w(u,v)
			return False
```
se detectan vértices de $v \in V(G)$ que cumplen la desigualdad expresada en el cuerpo del mismo, esto implica que en el grafo existen ciclos de costo negativo alcanzables desde $s$ y por tanto después de acabar el proceso de **Relax** quedarán vértices susceptibles a que el costo desde $s$ hacia ellos pueda seguir **bajando**.

**Observación**:
- Los vértices susceptibles a este problema **NO SON SOLO** los comprendidos en el ciclo de costo negativo, sino también aquellos que sean alcanzables desde dicho ciclo.
- Puede parecer que los vértices que **NO son alcanzables desde el origen** también podrían cumplir la desigualdad expresada en el cuerpo de dicho ciclo, pero veamos que no es así. Sea $u$ vértice alcanzable desde $s$ :
	1. Si $d[v] = \infty$ y $v$ está en otra componente diferente a la de $u$, es trivial que no se cumple, pues **no existe arco** de $u$ a $v$ y por tanto, en el ciclo dicho arco no será analizado, pues no existe.

	2. Si existe el arco $\langle u,v \rangle$ dentro de una componente dada y se cumple:
		- $d[v] = \infty$ y $d[u] = \infty$ tampoco se cumple la desigualdad pues al analizar la condición se cumplirá la condición de igualdad.
		- Si $d[v] \neq \infty$ y $d[u] = \infty$ entonces $d[v] < d[u] + w(\langle u,v \rangle)$, o sea, $d[v] < \infty$ y tampoco se cumplirá la desigualdad.

- El algoritmo se basa fundamentalmente en la aplicación consecuente y progresiva de la [[#Propiedad de la Convergencia]]. Primero se calcula correctamente la distancia hacia todos los vértices que se encuentran a distancia $0$ de $s$ (o sea, el propio $s$), luego los que están a distancia $1$, luego los que están a distancia $2$ y así sucesivamente. Como la mayor longitud que puede tener un camino de $s$ a $v$ es $n-1$ se hacen $n-1$ aplicaciones de **Relax** sobre los arcos de $G$.
##### Correctitud del Algoritmo

###### Lema ^1
Sea $G = \langle V,E \rangle$ dirigido y ponderado con función de costo $w: E \to \mathbb{R}$ definida sobre $G$, sea $s$ el vértice de origen. Si $G$ **no tiene ciclos de costo negativo alcanzables desde** $s$, entonces al concluir la ejecución del algoritmo se cumplirá:
$$
d[v] = \delta(s,v), \, \forall v \in V(G) \text{ alcanzable desde s.}
$$
**Demostración**:
Sea $p = \langle v_0=s, v_1,v_2,...,v_k=v \rangle$ un **camino de costo mínimo de** $s$ a $v$, $p$ es **simple** y los ciclos que pudieran haber en $p$, por ser este de costo mínimo, fueron eliminados por el propio algoritmo.

Probemos por inducción que para $i = 1,2,...,k$ se cumplirá que $d[v_i] = \delta(s,v_i)$ después de la $i$-ésima pasada del algoritmo sobre los arcos de $G$ y que esta igualdad se mantendrá posteriormente.

**Caso Base**
Tras las inicializaciones $d[v_0 = s] = \delta(s,s) = 0$ y por la [[#Propiedad de la Cota Superior]] se mantendrá así hasta el final.

**Paso Inductivo**:
Supongamos que $d[v_{i-1}] = \delta(s,v_{i-1})$ después de la $i-1$-ésima pasada.
Como a todos los arcos del grafo, al arco $\langle v_{i-1},v_i \rangle$ en particular se le hará **Relax** en la             $i$-ésima pasada, tengamos en cuenta que por hipótesis de inducción $d[v_{i-1}] = \delta(s,v_{i-1})$, entonces, por [[#Propiedad de la Convergencia]], tras aplicarle **Relax** en dicha pasada se alcanzará $d[v_{i}] = \delta(s,v_i)$ y esta igualdad se mantendrá hasta que concluya la ejecución del algoritmo. $\blacksquare$

##### Teorema
Sea $G = \langle V,E \rangle$ dirigido, ponderado, con función de costo $w: E \to \mathbb{R}$, definida sobre $G$, sea $s$ el vértice de origen. Si desde $s$ no se alcanzan ciclos de costo negativo en $G$, entonces:

1. Si el algoritmo retorna *True* :
	-  a) $d[v] = \delta(s,v), \, \forall v \in V(G)$
	-  b) La secuencia de arcos, en orden inverso, establecida por $\pi[v]$ expresa el camino de costo mínimo de $s$ a $v$.

2. Si el algoritmo retorna *False*:
	$G$ tiene un ciclo de costo negativo que se alcanza desde $s$.

**Demostración:**
1. Probemos que al terminar el algoritmo $d[v] = \delta(s,v), \, \forall v \in V(G)$
	a)
		- Si $v$ se alcanza desde $s$, entonces por [[#^1]] se prueba esta igualdad.
		- SI $v$ no se alcanza desde $s$ entonces por la [[#Propiedad de la no existencia de camino]] se prueba la igualdad.
	b) Es evidente que la secuencia de arcos en orden inverso establecida por $\pi[v], \, \forall v \in V(G)$ establece un camino de costo mínimo de $s$ a $v$.

Al concluir el algoritmo se tiene:
$$
d[v] = \underbrace{\delta(s,v) \leq \delta(s,u) + w(\langle u,v \rangle)}_{\text{desigualdad triangular}} = d[u] + w(\langle u,v \rangle)
$$
Por tanto, ningún arco cumplirá la condición:
$$
d[v] > d[u] + w(\langle u,v \rangle)
$$
de $6$ del algoritmo que es la que provoca que retorne *False*.


2. Supongamos que $G$ contiene un ciclo de costo negativo que se alcanza desde $s$ y sea $c$ dicho ciclo.
$$
c = \langle v_0,v_1,v_2,...,v_k=v_0 \rangle
$$
Entonces se cumplirá:
$$
w(c) = \sum_{i=1}^{k} w(\langle v_{i-1},v_i \rangle) < 0
$$

Por reducción al absurdo supongamos que bajo las condiciones del algoritmo retornara *True,* en tal caso se cumplirá que:
$$
d[v_i] \leq d[v_{i-1}] + w(\langle v_{i-1},v_i \rangle), \, \forall i=1,2,...,k
$$
O sea, se cumple la desigualdad triangular. 
Ahora sumemos las desigualdades alrededor del ciclo $c$ :
$$
\sum_{i=1}^{k}d[v_i] \leq \sum_{i=1}^{k} d[v_{i-1}] + \sum_{i=1}^{k} w(\langle v_{i-1},v_i \rangle)
$$

$$
\implies \cancel{d[v_1] + d[v_2] + \dots + d[v_k]} \leq \cancel{d[v_0] + d[v_1] + d[v_2] + \dots + d[v_{k-1}]} + \sum_{i=1}^{k} w(\langle v_{i-1},v_i \rangle)
$$

$$
\implies 0 \leq \sum_{i=1}^{k} w(\langle v_{i-1},v_i \rangle)
$$
Lo cual contradice el hecho de que el ciclo sea de costo negativo. Luego lo supuesto es falso y en caso de existir ciclos de costo negativo el algoritmo retornará *False*. $\blacksquare$. 