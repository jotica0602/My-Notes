#### Componente Fuertemente Conexa (SCC)
Una componente fuertemente conexa de un grafo dirigido $G = \langle V,E \rangle$ es un **conjunto maximal** de vértices $C \subset V$ que cumple que para todo par de vértices $u,v \in V(C)$, existe un camino de $u$ a $v$ y uno de $v$ a $u$, o sea, **hay caminos en ambas direcciones**.
#### Problema
Determinar las componentes fuertemente conexas (SCC) de un grafo dirigido $G = \langle V,E \rangle$.

Para resolver este problema clásicamente se utilizan dos recorridos $DFS$.

**Observaciones**: En un grafo dirigido $G = \langle V,E \rangle$
- Todos los vértices de G están en alguna componente fuertemente conexa, pero  ciertos arcos pueden no estarlo, estos son los arcos de cruce entre componentes, los cuales van de un vértice de una componente fuertemente conexa a otro vértice de otra.

##### Traspuesta de un Grafo Dirigido

**Definición**
La traspuesta de un grafo dirigido $G = \langle V,E \rangle$ es el grafo $G^T = \langle V,E^T \rangle$, donde $E^T = \set{\langle v,u \rangle) \in V \times V: \langle u,v \rangle \in E}$.
O sea, $G^t$ es el grafo $G$ con todos sus arcos invertidos.

**Observación**: Tanto $G$ como $G^T$ tienen las mismas componentes fuertemente conexas.

##### Teorema
En $G$ hay un camino en ambas direcciones entre $u$ y $v$ $\iff$ en $G^T$ lo hay también.

#### Grafo Reducido de un Grafo Dirigido
Las interconexiones entre las componentes fuertemente conexas de un grafo dirigido $G$ se pueden representar construyendo un **Grafo Reducido de G**.

**Grafo Reducido**: Se le llama así al grafo $G^{SCC} = \langle V^{SCC},E^{SCC} \rangle$ que se define de la siguiente forma:
- Sean $C_1,C_2,...,C_k$ las componentes fuertemente conexas de $G$.
- Sea $V^{SCC} = \set{v_1,v_2,...,v_k}$ el conjunto de vértices de $G^{SCC}$. En $V^{SCC}$ hay un vértice $v_i$ por cada componente fuerte de $C_i$ de $G$.
- $\langle v_i,v_j \rangle \in E^{SCC}$ si en $G$ **existe** al menos un arco $\langle x,y \rangle \in E$ para algún $x \in C_i$ y para algún $y \in C_j$.

A este grafo suele llamársele también **grafo de componentes**.

#### Propiedades del Grafo Reducido

El grafo reducido de $G$ es un $DAG$, o sea, es dirigido y acíclico, lo cual se demuestra a partir del siguiente **Lema**.

##### Lema 1
Sean $C$ y $C'$ dos componentes fuertemente conexas diferentes del grafo dirigido $G = \langle V,E \rangle$ y sean $u,v$ dos vértices en $C$, y sean $u',v'$ dos vértices en $C'$ y supongamos que existe un camino de $u$ a $u'$ en $G$ 
$\implies$ **NO PUEDE** haber un camino de $v'$ a $v$ en $G$.

**Demostración**:
Si hubiera un camino de $v'$ a $v$ en $G$, entonces existirían los caminos $\langle u \sim u' \sim v \rangle$  y $\langle v' \sim v \sim u \rangle$ y por tanto $u$ y $v'$ serían alcanzables entre sí y en ambas direcciones en $G$, lo que contradice que $C$ y $C'$ sean dos componentes fuertemente conexas **diferentes** de $G$. $\blacksquare$

El planteamiento del **Lema 1** puede interpretarse como:
SI en el grafo reducido hubiera un ciclo entonces las componentes fuertemente conexas implicadas en el mismo **no fueran maximales**, pues desde cada vértice de alguna de ellas se puede ir a un vértice de cualquiera de las otras en ambas direcciones.

#### Propiedad fundamental en la que se basa el algoritmo

El grafo reducido de $G$ es un $DAG$, o sea, es dirigido y acíclico.

#### Pseudocódigo
$SCC(G)$:
1. $DFS(G)$ para calcular $f[u], \forall u \in V(G)$
2. Determinar $G^T$
3. $DFS(G^T)$ comenzando por el vértice $u$ de mayor $f[u]$.(Si la búsqueda en profundidad no llega a todos los vértices se inicia la búsqueda desde el siguiente vértice blanco de mayor $f[u]$).
4. Cada árbol del bosque abarcador resultante es una componente fuertemente conexa de $G$.


```python
def SCC(G):
	S = DFS_SCC_1(G)
	transpose(G)
	DFS_SCC_2(G,s)

def DFS_SCC_1(G):
	for v in V(G):
		v.color = white
		pi[u] = None
		
	time = 0
	stack = stack()
	for v in V(G):
		if v.color == white
			DFS_VISIT_1(G,u,s)

def DFS_VISIT_1(G,u,stack):
	time = time + 1
	u.d = time
	u.color = gray
	for v in neighbors(u):
		if v.color == white
		pi[v] = u
		DFS_VISIT_1(G,v,s)
	u.color = black
	time = time + 1
	u.f = time
	stack.push(u)

def DFS_SCC_2(G,stack):
	for v in V(G):
		v.color = white
		
	c = 0
	
	while stack is not empty:
		u = stack.pop()
		if u.color == white
			DFS_VISIT_2(G,u,c)
			c = c+1

def DFS_VISIT_2(G,u,c):
	u.color = gray
	for v in neighbors(u):
		if v.color == white
			DFS_VISIT_2(G,v,c)
	u.color = black
	u.CC = c
```

#### Propiedades de las componentes fuertemente conexas de un grafo dirigido

Extendamos la notación $d[u]$ y $f[u]$ dada para vértices de $G = \langle V,E \rangle : u \in V(G)$ a conjuntos de vértices.

Si $U \subseteq V$ entonces se define:
- $d(U) = min_{u \in U}\set{d[u]}$
- $f(U) = max_{u \in U}\set{f[u]}$

Donde:
- $d(U)$ es el valor del **primer momento** en que se descubre un vértice de $U$.
- $f(U)$ es el último momento en que un vértice de $U$ finaliza la recursividad.

##### Lema 2
Sean $C$ y $C'$ dos $SCC$ **diferentes** del grafo dirigido $G = \langle V,E \rangle$. Supongamos que existe un arco $\langle u,v \rangle \in E$ con $u \in C$ y $v \in C'$. Entonces $f(C) > f(C')$.

**Demostración**:
Existen dos casos en dependencia de cuál de las dos componentes fuertes $C$ o $C'$ tenga el vértice de menor $d$.

- Caso 1: $d(C) < d(C')$:
Sea $x$ el primer vértice que se descubre en $C$. En el instante $d[x]$ los restantes vértices en $C$ y en $C'$ son blancos. Entonces puede decirse que hay un camino en $G$ de $x$ a los restantes vértices de $C$, donde todos los vértices en dicho camino son blancos.
Como $\langle u,v \rangle \in E$, entonces para cualquier vértice $w \in C'$, en el instante $d[x]$ hay también  un camino de $x$ a $w$ en el cual todos los vértices que pertenece al mismo son blancos y dichos caminos tendrán la forma $\langle x \sim u \rightarrow v \sim w \rangle$. Por tanto todos los vértices en $C$ y en $C'$ se convierten en descendientes de $x$ en el árbol en profundidad del cual $x$ es raíz.  

>**Recordemos que** sean $u,v$ dos vértices de un grafo dirigido $G$, $v$ es descendiente propio del vértice $u$ en el $DFS$ de $G$ **si y solo si** $d[u] < d[v] < f[v] < f[u]$. ^5d7ad6

Aplicándolo a nuestro caso tendremos que:
$d[x] < d[u] < d[v] < d[v] < d[w] < f[w] < f[v] < f[u] < f[x]$, de lo cual se deduce que $f[x] = f(C) > f(C')$.

- Caso 2: $d(C) > d(C')$:
Sea $y$ el primer vértice que se descubre en $C'$. En el instante $d[y]$ todos los vértices en $C'$ son blancos y además, hay un camino en $G$ desde $y$ hasta cualquiera de los restantes vértices en $C'$, donde todos los vértices en dicho camino son blancos.
Por tanto todos los vértices en $C'$ se convierten en descendientes de $y$ en el árbol abarcador en profundidad y por el razonamiento anterior ([[SCC#^5d7ad6]]) $f[y] = f(C')$.

> Como existe un arco $\langle u,v \rangle$ de $C$ a $C'$ por el **Lema 1**([[SCC#Lema 1]]) podemos afirmar que no puede existir un arco $C'$ a $C$.

Por tanto, ningún vértice en $C$ es alcanzable desde $C'$.

Por consiguiente, en el instante $f[y]$ todos los vértices de en $C$ siguen aún siendo blancos, lo cual implica $f(C) > f(C')$. $\blacksquare$

![[Drawing 2024-09-22 19.16.32.excalidraw]]

##### Corolario

Sean $C$ y $C'$ dos componentes fuertes diferentes del grafo dirigido $G = \langle V,E \rangle$. Supongamos que existe un arco $\langle u, v \rangle \in E^T$ de $G^T = \langle V,E^T \rangle$, donde $u \in C$ y $v \in C'$. Entonces $f(C) < f(C')$ en $G$.

**Demostración**:
Como $\langle u,v \rangle \in E^T$, entonces $\langle v,u \rangle \in E$. Como las componentes fuertemente conexas en $G$ y en $G^T$ son las mismas, entonces por el **Lema 2** [[SCC#Lema 2]] se tiene $f(C) < f(C')$.
![[Drawing 2024-09-22 19.18.35.excalidraw]]

#### Correctitud del Algoritmo
$SCC(G)$ calcula correctamente las componentes fuertemente conexas de un grafo dirigido $G$.

**Demostración**:
La demostración se hará por inducción sobre el número de árboles calculados tras el segundo $DFS$ que se aplica sobre $G^T$.

**Hipótesis de Inducción**:
Los primeros $k$ árboles que se forman durante la aplicación del segundo $DFS$ sobre $G^T$ se corresponden con $k$ componentes fuertemente conexas de $G$.

**Caso Base**:
$k = 0$, es trivial que se cumple.

**Paso Inductivo**:
Asumimos que se cumple la hipótesis de inducción y consideremos el $k+1$-ésimo árbol que se forma.

Sea el vértice $u$ la raíz de dicho árbol y sea $C$ la componente fuerte a la cual pertenece el vértice $u$.
$\implies f[u] = F(C)$ por la forma en la que se seleccionan las raíces de los árboles en el segundo $DFS$ que se aplica a $G^T$.

$f[u] = f(C) > f(C')$ para cualquier otra componente fuerte $C' \neq C$ **que aún no ha sido visitada**.

En el momento en el que el segundo $DFS$ alcanza a $u$, los restantes vértices en $C$ son **blancos** por hipótesis de inducción.
$\implies$ los restantes vértices que están en la componente $C$ son descendientes de $u$ en el árbol en profundidad del cual $u$ es raíz.

Por la propia hipótesis de inducción y por el **Corolario**[[SCC#Corolario]] puede afirmarse que cualquier otro arco $G^T$ que salga de $C$ tiene que llegar a alguna componente fuerte que ya haya sido visitada.

$\implies$ los vértices accesibles desde $u$ que no pertenezcan a $C$ serán vértices de una componente fuerte ya descubierta.
$\implies$ no serán añadidos al árbol en profundidad del cual $u$ es raíz.
$\implies$ solo quedarán en el mismo los vértices que pertenecen a $C$.
![[Drawing 2024-09-22 19.45.38.excalidraw]]
Observemos que al trasponer las aristas, los $f(C_i)$ permanecen iguales.

**Complejidad Temporal**
- $O(|V| + |E|)$ Asumiendo la representación del grafo por una lista de adyacencia.