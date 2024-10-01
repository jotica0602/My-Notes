#### Grafo Ponderado
Un grafo no dirigido $G = \langle V, E \rangle$ se dice que es **ponderado** si $\forall \langle u,v \rangle \in E$, $\exists \omega(\langle u,v \rangle)$, donde generalmente $\omega:E\to \mathbb{R}$. 
$\omega(\langle u,v \rangle)$ representa el peso o costo de la arista $\langle u,v \rangle$.

#### El problema
Encontrar $E' \subseteq E$ que **conecte todos los vértices** en $V$, cuyo costo total (la suma de todos los costos o pesos de las aristas) sea **mínimo**. Con todo ello formar un árbol $T = \langle V,E' \rangle$.

Este árbol existe pues:
- Como $T$ es acíclico y conexo (conecta todos los vértices), entonces forma un árbol libre, al que se le llama **árbol abarcador**, porque en él están todos los vértices del grafo.
- Si además, **la suma de todos los costos o pesos de las aristas de** $T$ **es mínimo**, entonces $T$ es **abarcador de costo mínimo**, al cual denominaremos como **AACM** por sus siglas o **MST** por sus siglas en inglés.

#### Marco Teórico
Asumamos que $G = \langle V,E \rangle$ es un grafo no dirigido y ponderado.
##### Definiciones
- Un **corte** $(S,V-S)$ es una partición del conjunto de vértices $V$.
- Una arista $\langle u,v \rangle$ **cruza el corte** $(S,V-S)$ si uno de los extremos de la misma está en $S$ y el otro en $V-S$.
- Un **corte respeta un conjunto de aristas** $A$ si **NO** existen aristas en $A$ que crucen el corte.
- Una **arista** es **liviana** cruzando el corte, si tiene el menor peso entre todas las que lo cruzan.
##### Teorema: para reconocer aristas seguras

^6c3eca

- Sea $G = \langle V,E \rangle$ un grafo conexo, no dirigido y ponderado.
- Sea $A \subseteq E$ incluido en algún AACM de $G$.
- Sea $(S,V-S)$ un corte de G que respeta A.
- Sea $\langle u,v \rangle \in E$ una arista liviana que cruza el corte $(S,V-S)$
$\implies$ $\langle u,v \rangle$ es **segura** para A.
Esto significa que  $A \cup \set{\langle u,v \rangle} \subseteq MST(G)$ 

**Demostración**:
Sea $T$ un $MST(G)$ tal que $A \subseteq T$. (Por hipótesis $A \subseteq T$).
- Si $\langle u,v \rangle \in T \implies \langle u,v \rangle$ es segura y queda demostrado el Teorema.
- Si $\langle u,v \rangle \notin T$ entonces:
Como $T$ es AACM de $G$, en él están todos los vértices de $G$ y además están conectados, por lo que **tiene que existir un camino** de $u$ a $v$ en $T$ y además, en el mismo **tiene haber alguna arista que cruce el corte**, pues de lo contrario $u$ y $v$ pertenecerían ambos al corte, lo que contradice que $\langle u,v \rangle$ sea arista que lo cruza. Sea $\langle x,y \rangle$ la arista que cruza el corte en $T$, podemos **construir otro AACM** $T'$ que incluya a $A \cup \set{\langle u,v \rangle}$ y demostrar que $\langle u,v \rangle$ es segura para $A$.

¿**Cómo construir dicho AACM**?
Observemos que agregar la arista $\langle u,v \rangle$ formaría un ciclo en $T$, por lo que debemos eliminar la arista $\langle x,y \rangle$ para luego agregar $\langle u,v \rangle$. Sea $T'$ el árbol resultante, este **también** es abarcador de costo mínimo.
**Demostración**:
$$
T' = T -\set{\langle x,y \rangle} + \set{\langle u,v\rangle}
$$
Sea $\omega(T)$ el costo total de $T$, entonces $\omega(T) = \sum_{i=1}^m e_i$, donde $e_i \in E(T)$.

Por lo que:
$$
\omega(T') = \omega(T) - \omega(\langle x,y \rangle) + \omega(\langle u,v \rangle)
$$

Conocemos que $\omega(\langle u,v \rangle) \leq \omega(\langle x,y \rangle)$ porque $\langle u,v \rangle$ es liviana.
$$
\implies \omega(T') \leq \omega(T)
$$
No es posible que $\omega(T') < \omega(T)$ porque entonces $T$ no sería AACM. Por lo que $\omega(T) = \omega(T')$.

$\therefore T'$ AACM.

##### Corolario

^6fce37

- Sea $G = \langle V,E \rangle$ conexo, no dirigido y ponderado.
- Sea $A \subseteq E$ incluido en algún AACM de $G$.
- Sea $C = (V_c, E_c)$ componente conexa (árbol) en el bosque $G[A] = (V,A)$.

**Nota:** $G[A]$ es el bosque inducido por las aristas de $A$.

**Demostración:**
El corte $(V_C, V-V_C)$ respeta a $A$ y $\langle u,v \rangle$ es una arista liviana de las que cruzan el corte, por lo que por [[MST#^6c3eca]], $\langle u,v \rangle$ es **segura** para $A$.


#### Algoritmo de Kruskal
Encuentra la **arista segura** para añadir a $A$ bajo el siguiente criterio:
Seleccionar, entre todas las aristas que enlazan **árboles distintos** del bosque $G[A]$, la arista $\langle u,v \rangle$ de menor peso.

Lo siguiente justifica la credibilidad del criterio planteado:
- Sean $C_1$ y $C_2$ dos árboles del bosque $G[A]$ 
- Sea $u \in C_1, v \in C_2$ y $\langle u,v \rangle \in E$ (observemos que $\langle u,v \rangle$ conecta a $C_1$ con $C_2$).
- Sea el corte $(C_1,V-C_1)$, entonces:
Si $\langle u,v \rangle$ es **liviana**, entonces por [[MST#^6fce37]] es segura para $A$.

##### Pseudocódigo

```python
def kruskal(G,w):
	A = []
	V_A = Disjoint_Sets(V(G))                -O(|V|)
	edge_weights = [w(e) for e in E(G)]      -O(|E|)
	MergeSort(edge_weights)                  -O(|E|log|E|)
	#e[0] = u
	#e[1] = v
	---------------------------------------------- |E|log|E|
	for e in edge_weights:                   -O(|E|)
		if SetOf(e[0]) != SetOf(e[1]):       -O(log|V|)
			A.append(e)                      -O(1)
			Merge(e[0],e[1])                 -O(log|V|)
return A
```

**Complejidad Temporal**:
- $O(|E|\log{|V|})$ si $G$ está representado por una **lista de adyacencia**.
- $O(|V|^2\log{|V|}$ si $G$ está representado por una **matriz de adyacencia**.

**Observación:** Si $G$ no fuera conexo, puede aplicarse Kruskal a cada componente conexa, y, al finalizar se obtendrá un AACM para cada una.

#### Algoritmo de Prim
Inicialmente, $G[A]$ posee un nodo raíz $r$ que se selecciona de forma arbitraria. Durante la ejecución del algoritmo, $G[A]$ crece (agregándole en cada pasada una arista más) hasta llegar a contener todos los vértices de $V$.

**Estrategia**:
En cada iteración se considera el corte $(V_A, V-V_A)$, el cual respeta a $A$ y se selecciona una **arista liviana para dicho corte**, o sea una arista que conecte algún vértice de $V_A$ con alguno de $V-V_A$, por [[MST#Teorema para reconocer aristas seguras]] dicha arista es segura para $A$ y por tanto se añade al conjunto.

Tras $|V|-1$ iteraciones las aristas de $A$ forman un AACM.

##### Código

```python
import heapq

def prim(G, r):

	n = len(E(G))            # Número de nodos en el grafo
    visited = [False] * n    # Para marcar los nodos visitados
    
    min_heap = [(0, r)]      # (peso, nodo) -> heap de prioridad, inicializado                                # en el nodo de inicio
    
    A = []                   # Lista para guardar las aristas del MST 

    while min_heap is not empty:
        weight, u = heapq.heappop(min_heap)  # Extraer el nodo con menor peso
        
        if visited[u]: continue  # Si ya fue visitado, lo ignoramos9
        
        visited[u] = True        # Marcar como visitado y agregar costo
		A.append((u, weight))    # Añadir las aristas a la lista del MST

        # Explorar las aristas adyacentes del nodo u
        for v, w in graph[u]:  # v es el vecino, w es el peso de la arista (u, v)
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))  # Añadir el vecino y el peso                                                     # al heap

    return A
```

**Complejidad Temporal:**
- $O(|E|\log|V|)$.
- $O(|V|^2\log{|V|})$ para grafos densos, porque $|E|$ es $O(|V|^2)$