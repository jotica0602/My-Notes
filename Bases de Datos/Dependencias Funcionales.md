
# Recordando...
Recordemos qué es una [[Modelo Relacional#Llave Candidata]].

# ¿Cómo encontrar las llaves candidatas de una relación?

Sea $U = \set{A_1,\dots,A_n}$ el conjunto universo de los atributos de una relación $R$, por cada subconjunto de atributos $X \subseteq U$ comprobar la unicidad y minimalidad.

## Minimalidad

Un conjunto $C$ es minimal con respecto a una propiedad $P$ si y solo si:
1. $P(C)$
2. $\nexists C' \subset C : P(C')$ 

Para comprobar minimalidad debemos comprobar **unicidad**.

## Unicidad

Sea $K = \set{A_1,A_2,\dots,A_n}$ un conjunto de atributos de una relación $R$, en cualquier momento dado, no existen dos tuplas distintas de $R$ con los mismos valores para $A_1,A_2,\dots,A_n.$

> No necesariamente es una función inyectiva.

**Ejemplo:**

- Los proveedores de correo (Google, Yahoo, Outlook, etc.) asocian al correo algunos datos personales como el nombre y el apellido.
- Existe un convenio internacional en el que los países acuerdan códigos para identificar la ubicación geográfica (código postal).

Si se desea desarrollar un sistema que requiera tanto los datos personales como la ubicación geográfica del usuario, ¿cuál sería la llave primaria de la relación Usuario?

**Buscando una llave candidata:**

**Usuario**(Email, Nombre, Apellido, C. Postal, Provincia, País)

- Si conocemos el email de un usuario también conocemos su nombre y apellido.
	$$
	\text{Email} \to \text{Nombre, Apellido}
	$$
- Si conocemos el código postal de un usuario también conocemos su provincia y país.	
	$$
	\text{C. Postal} \to \text{Provincia, País}
	$$
Componiendo las funciones que ya conocemos:

$$
\text{Email, C. Postal} \to \text{Nombre, Apellido, Provincia, País}
$$

# Dependencia Funcional

Dada una relación $R$ y los atributos $X$, $Y$ de $R$, se dice que **$Y$ depende funcionalmente de $X$ si y solo si el valor de $X$ en cada tupla de $R$ determina el valor de $Y$ en dicha tupla**. Se representa como $R.X \to R.Y$ o simplemente:

$$
X \to Y
$$

**Notación**:
- Atributo simple: $A,B,C,D,E$.
- Atributo compuesto (conjunto de atributos simples): $W,X,Y,Z.$
## Cumplimiento de una Dependencia Funcional

Sean $U = A_1, A_2,\dots, A_n$ el universo de los atributos de la relación $R$, $X \subseteq U$ y $Y \subseteq U$. La dependencia funcional $X \to Y$ se cumple en $R$ si para toda instancia de $r(R)$ para todos los pares de tuplas $t_1$ y $t_2$ en $r$ se cumple que:

$$
t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]
$$

## ¿Cómo representar una relación?

Un **esquema relacional** expresado por $R(U,F)$ constituye una manera abreviada de representar la descripción de una relación mediante:
- Su nombre $R$.
- El conjunto de atributos que la componen $U$.
- El conjunto de dependencias funcionales $F$ que se cumplen en $R$.

### ¿Para qué es útil esto?

- Permite especificar las restricciones en el conjunto de instancias legales de una relación $R$ (instancias $r$ de $R$ que satisfacen un conjunto de dependencias funcionales $F$): 
	$$
	\textbf{F se cumple en R}
	$$
- Probar si una instancia $r$ de una relación $R$ es legal bajo un conjunto de dependencias funcionales $F:$  
	$$
	\textbf{r satisface a F}
	$$

## Algoritmo para determinar si un conjunto de atributos cumple la unicidad

**Entrada**: $U = \set{A_1,A_2,\dots,A_n}$, $F$ conjunto de dependencias funcionales y $X$, $X \subseteq U$.
**Salida**: 1 si el conjunto $X$ cumple la unicidad en $R(U,F)$ o 0 en otro caso.
**Método**:
1. Sea $X$ el conjunto de atributos que se desea comprobar. Primero inicializamos $X_0 = X.$
2. En cada iteración $i$ se busca una dependencia funcional $Y  \to A$ tal que $Y \subseteq X_{i-1}$, pero $A \notin X_{i-1}$. Entonces se asigna $X_i = X_{i-1} \cup \set{A}.$   
3. Repetir el paso 2 tantas veces como sea necesario hasta que no puedan añadirse más atributos. Dado que el conjunto resultante solo puede crecer y la cantidad de atributos en el universo es finito, eventualmente el algoritmo termina.
4. Sea $k$ la iteración final del algoritmo, se comprueba que $X_k = U$.

**Ejemplo:**

Sea $R(U,F)$ con:

- $U = \set{A,B,C,D,E,G}$
- $F = \set{AB \to C, C \to A, BC \to D, ACD \to B, D \to EG, BE \to C}$

Compruebe si $CD$ cumple la unicidad.

**Solución**:

Inicializamos $X_0 = CD$
1. $X_1 = ACD$
2. $X_2 = ABCD$
3. $X_3 = ABCDEG$

$X_3 = U$, se cumple la unicidad.

## Implicación Lógica

Sea un esquema relacional $R(U,F)$ y $X \to Y$ una dependencia funcional. Se dice que $F$ implica lógicamente a $X \to Y$ o que $X \to Y$ se deduce lógicamente de $F$ si cada instancia $r$ de $R$ que satisfaga las dependencias funcionales en $F$ también satisface $X \to Y$.

$$
F \models X \to Y
$$

### Herramientas para inferir lógicamente

**Axiomas de Inferencia (Armstrong)**
Sea un esquema relacional $R(U,F):$
1. **Reflexividad**: Si $Y \subseteq X \subseteq U$, entonces $X \to Y$ se deduce lógicamente de $F$.
2. **Aumentatividad**: Si se cumple que $X \to Y$ y $Z \subseteq U$, entonces $XZ \to YZ$.
3. **Transitividad**: Si se cumple que $X \to Y$ y $Y \to Z$, entonces $X \to Z$.

**Propiedades de los Axiomas**
- Sólidos: Si $X \to Y$ se deduce de $F$ aplicando los axiomas de Armstrong, entonces $X \to Y$ es verdadera en cualquier instancia de $R(U,F)$.
- Completos: Si $X \to Y$ es verdadera en cualquier instancia de $R(U,F)$, entonces $X \to Y$ se deduce lógicamente de $F$ aplicando los Axiomas de Armstrong.

**Lemas derivados**

Sea un esquema relacional $R(U,F):$
1. **Composición:** $\set{X \to Y, W \to Z | W \subseteq X} \models X \to YZ$
2. **Descomposición**: $\set{X \to Y, Z \subseteq Y} \models X \to Z$
3. **Pseudotransitividad**: $\set{X \to Y, WY \to Z} \models XW \to Z$


## Clausura de un conjunto de atributos

Sea un esquema relacional $R(U,F)$, un conjunto de atributos $X$ tal que $X \subseteq U$. La clausura del conjunto de atributos $X$ con respecto a un conjunto de dependencias funcionales $F$, denotada por $X_F^+$ o abreviadamente $X^+$, es el conjunto de atributos **simples** que se determina funcionalmente por $X$ a partir de las dependencias funcionales de $F$.

$$
X_F^+ = \set{A_i \in U \, | \, F \models X \to A_i}
$$

## Clausura de un conjunto de dependencias funcionales

Sea un esquema relacional $R(U,F)$. La clausura del conjunto de dependencias $F$, denotada por $F^+$ es el conjunto de las dependencias funcionales implicadas lógicamente por $F$. Formalmente se define como:

$$
F^+ = \set{X \to Y \, | \, F \models X \to Y}
$$

## Clasificación de dependencias funcionales

Sea una dependencia funcional $A_1, A_2, \dots, A_n \to B_1, B_2, \dots, B_m:$
- Es trivial si $\set{B_1,B_2,...,B_m} \subseteq \set{A_1,A_2,...,A_n}$
- Es no trivial si existe $B_i \notin \set{A_1,A_2,...,A_n}$
- Es completamente no trivial si $\set{B_1,B_2,...,B_m} \cap \set{A_1,A_2,...,A_n} = \emptyset$

**Ejemplos:**

- Trivial: $A \to A$
- No trivial: $A \to AB$
- Completamente no trivial: $A \to B$

## ¿Cómo podemos determinar si una dependencia funcional $X \to Y$ pertenece a $F^+$?

La primera idea intuitiva sería computar $F^+$, pero ¿es realmente viable hacer esto?

¿Cuántas dependencias funcionales **triviales** existen en $F^+$?
- Sea un conjunto de atributos $X$ se tiene que $X \to X', \, \forall X' : X' \subseteq X, X' \neq \emptyset$
- El conjunto de dependencias funcionales triviales cuyo determinante es $X$ tiene $2^{|X|} - 1$ elementos.
- La cantidad de dependencias funcionales triviales con respecto a la cantidad de atributos de $U$ es exponencial.

Una vía más eficiente sería utilizar la clausura del conjunto de atributos $X$.

**Respuesta** 
Siguiendo los siguientes pasos:
1. Calcular $X_F^+$
2. Comprobar que $Y \subseteq X_F^+$ 

## Equivalencia de conjuntos de dependencias funcionales

$$
F \equiv G \iff F^+ = G^+
$$

- Se debe considerar cada $X \to Y$ en $F$ y determinar si $X_G^+$ contiene a $Y$.
- Se debe considerar cada $Z \to W$ en $G$ y determinar si $Z_F^+$ contiene a $W$.

# Mejorando la definición de Llave Candidata

Sea $K$ un conjunto de atributos $\set{A_1,A_2,\dots,A_n}$ de un esquema relacional $R(U,F)$, este es llave candidata del esquema si cumple las siguientes propiedades:
1. **Unicidad**: $K_F^+ = U$
2. **Minimalidad**: Ningún subconjunto propio de $K$ tiene la propiedad de unicidad.

El conjunto de atributos $X$ cumple la unicidad en $R(U,F)$ si y solo si $X_F^+ = U.$

