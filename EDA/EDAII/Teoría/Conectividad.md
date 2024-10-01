
#### Grafo $k$-conexo
Un grafo tiene conectividad $k$ si al eliminar del mismo $k-1$ vértices y las aristas incidentes en ellos, **cualesquiera a la vez**, el mismo **NO se desconecta**.

#### Punto de Articulación
Un punto de articulación de un grafo $G = \langle V,E \rangle$ es un vértice $v \in V$, tal que al eliminar $v$ de $G$ y todas las aristas incidentes en él, se divide una componente conexa en **dos o más componentes conexas.**

#### Arista Puente
Dado un grafo $G = \langle V, E \rangle$ no dirigido, se dice que $e \in E$ es una arista puente si al eliminarla se desconecta el grafo $G$, **aumentando en uno la cantidad de componentes conexas del mismo**.

 **Observación**
- Un grafo sin aristas puente tiene al menos un ciclo.

#### ¿Cómo encontrar los puntos de articulación de un grafo?

##### Marco Teórico
Sea $G = \langle V, E \rangle$ **conexo** y no dirigido. 
###### Lema 1
La raíz ($s$) del árbol abarcador en profundidad $G_\pi$ es un punto de articulación $\iff$ tiene al menos dos hijos en $G_\pi$.   

$(\implies)$ Si $s$ es punto de articulación, desconecta al grafo en **dos o más componentes conexas** (por definición), por lo que necesariamente tiene que tener una arista en $G_\pi$ por cada Componente Conexa.

($\impliedby$) Analicemos los siguientes casos:
- Si $s$ **no tiene hijos**: $s$ **NO** es punto de articulación por definición, pues el grafo resultante tras eliminarlo sería el vació.
- Si $s$ tiene **un único hijo**, sea este $t$: Podemos desconectar $s$ y su única arista incidente y el árbol resultante $G_\pi' = G_\pi - s$ continua siendo conexo.
- Si $s$ tiene 2 o más hijos: Sean $u,v$ dos vértices adyacentes a $s$, cualquier camino entre $u$ y $v$ tiene que pasar por $s$, pues de lo contrario, si existiera $c$ camino simple entre ellos tal que $s$ no participa en él, entonces habría un ciclo, lo cual es una contradicción, pues $G_\pi$ es un árbol. Luego $s$ es punto de articulación. $\blacksquare$
###### Lema 2
Un vértice $v$ que no sea raíz del árbol abarcador en profundidad $G_\pi$ es punto de articulación $\iff$ $v$ tiene, al menos, un hijo $w$ tal que **no existe** una arista de retroceso desde $w$, o desde cualquiera de sus descendientes hacia un ancestro de $v$.

**Observación:** Basta con que exista un hijo $w$ que cumpla la proposición para que $v$ sea punto de articulación (pueden haber hijos de $v$ que no la cumplan).

($\implies$) Como $v$ es punto de articulación, entonces al eliminarlo el grafo se divide en al menos 2 componentes conexas, sean estas $CC_1$ y $CC_2$. En una de estas estarán los ancestros de $v$ y posiblemente algunos de sus descendientes sea esta $CC_1$ sin pérdida de generalidad. Toda arista de retroceso de la otra componente conexa $CC_2$ tiene que conectar necesariamente a los descendientes de $v$ entre sí o con el propio $v$, pues de lo contrario al desconectarlo existiría otra forma de llegar desde $CC_2$ hasta $CC_1$ y $v$ no sería punto de articulación. Como $v$ unía por sus aristas a $CC_1$ y $CC_2$, tiene que existir al menos un descendiente suyo en $CC_2$ al que este sea adyacente.

($\impliedby$) Todo camino desde $w$ o cualquiera de sus descendientes hacia $v$ o un ancestro suyo debe pasar necesariamente por $v$, por tanto, al desconectarlo este divide a $G_\pi$ en dos o más componentes conexas. $\blacksquare$

###### Teorema
Un vértice $v$ distinto de la raíz, es punto de articulación $\iff$ existe un vértice $w$, hijo de $v$ en el árbol abarcador correspondiente, tal que $low[w] \geq d[v]$.

**Demostración**: Es una aplicación directa del [[Conectividad#Lema 2]].

#### Pseudocódigo: Puntos de articulación

```python
DFS(G):
	for each v in V(G):
		DFS_Visit_PA(G,v)
	return
	
DFS_Visit_PA(G,u):
	u <- visited
	time = time + 1
	d[u] = time
	low[u] = d[u]

	for each v in N(v):
		if v is not visited:
			pi[v] = u
			DFS_VISIT_PA(G,v)
			low[u] = min(low[u], low[v]) #u es padre de v y <u,v> arista                                                  #de arbol 
			if low[v] >= d[u]:
				print 'u is articulation point'
			else if pi[u] != v:              #v ya visitado, u NO ES padre de v
											 #por tanto <u,v> arista de retroceso
				low[u] = min(low[u],d[v])
	return
```

**Observaciones**:

- $d[u]$: Es el tiempo de descubrimiento (discovery time) de $u$.
- $low[u]$: Es lo más **bajo** que se puede en el árbol desde el vértice $u$. 
- El $low[u]$ se termina de calcular cuando se ha visitado toda la descendencia de $u$. 
- El criterio fundamental en el que nos basamos para detectar un punto de articulación es que si lo más bajo que se pudo desde $u$ y sus descendientes fue hasta el propio $u$ o alguno de sus descendientes, entonces al desconectar $u$, sus descendientes quedarán desconectados del resto del árbol.
- De cierta forma $d[u]$ es el límite de $u$ y toda su descendencia, de forma tal que si **ningún vértice** lo sobrepasa, entonces $u$ **SERÁ punto de articulación**.
				![[Drawing 2024-09-20 23.33.52.excalidraw]]
- **Basta con que exista al menos descendiente** de $u$ que cumpla esta condición para que $u$ sea **punto de articulación**
					![[Drawing 2024-09-21 00.01.02.excalidraw]]
En este caso al desconectar $u$ y sus aristas, el vértice $v$ y sus descendientes aún pueden hacia los descendientes de $u$. No sucede lo mismo con $w$ y sus descendientes, por lo que $u$ es **punto de articulación**.

#### Pseudocódigo: Aristas Puente

```python
DFS(G):
	for each v in V(G):
		DFS_Visit_PA(G,v)
	return
	
DFS_Visit_PA(G,u):
	u <- visited
	time = time + 1
	d[u] = time
	low[u] = d[u]

	for each v in N(v):
		if v is not visited:
			pi[v] = u
			DFS_VISIT_PA(G,v)
			low[u] = min(low[u], low[v]) #u es padre de v y <u,v> arista                                                  #de arbol 
			if low[v] >= d[u]:
				print('u is articulation point.')
			else if pi[u] != v:              #v ya visitado, u NO ES padre de v
											 #por tanto <u,v> arista de retroceso
				low[u] = min(low[u],d[v])
				
	if low[u] == d[u] and pi[u] is not null: #detectar arista puente
		print('<pi[u],u> is bridge edge.')
	return
```

Una vez hayamos explorado toda la descendencia de $u$ y calculado su $low$, si lo más bajo que se puede llegar desde él o sus descendiente es el propio $u$, entonces al remover la arista entre $u$ y su padre, tanto $u$ como sus descendientes quedarán desconectados del árbol.

				![[Drawing 2024-09-21 00.01.02.excalidraw]]
Observemos que a lo más bajo que puede llegar tanto $w$ como su descendencia es al propio $w$, por lo que al remover la arista $\langle u,w \rangle$ el árbol se divide en dos componentes conexas.   

**Observación**: Una arista puente **no necesariamente** conecta a dos puntos de articulación y en el esquema anterior tenemos una demostración clara de ello.
#### ATENCIÓN 
La raíz es un caso aparte para analizar. Para determinar si esta es punto de articulación nos basamos en el [[Conectividad#Lema 1]], verificando que tenga 2 o más hijos.

