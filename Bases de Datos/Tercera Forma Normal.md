
# Situación

Se desea desarrollar una base de datos para registrar las notas de los estudiantes de la facultad en cada una de las asignaturas que cursan:

- De cada estudiante se conoce su identificador, su nombre, su grupo y su provincia de residencia.
- De cada asignatura se conoce su identificador y su nombre
- Por cada asignatura se conoce la nota que obtuvo el estudiante en la evaluación final.

Además, se conoce que los estudiantes son organizados en los grupos de acuerdo a su provincia.

## Modelo Conceptual

![[Drawing 2024-08-02 22.01.16.excalidraw]]

## Metodología para obtener un esquema relacional correcto

1. Identificar el universo $U$ de atributos del fenómeno.
2. Identificar el conjunto $F$ de las dependencias funcionales que se establecen entre los atributos.
3. Definir el esquema relacional $R(U,F).$

### Algoritmo para obtener $F$ a partir del diseño conceptual

1. Por cada conjunto de entidades con un conjunto de atributos $X \subseteq U$, se añade la dependencia funcional $K \to X$ donde $K$ es la llave del conjunto de entidades.
2. Por cada conjunto de interrelaciones se toma su llave $K$ y se añade la dependencia funcional $K \to K$. Además, por cada conjunto de entidades en un extremo de cardinalidad máxima 1 en la interrelación, se añade a la dependencia funcional $K - K_E \to K_E$ donde $K_E$ es la llave del conjunto de entidades.
3. Por cada agregación con un conjunto de atributos $X \subseteq U$ se añade la dependencia funcional $K \to X$ donde $K$ es la llave del conjunto de interrelaciones que encierra la agregación.
4. Añadir aquellas dependencias funcionales asociadas a otras restricciones del negocio especificadas en los requerimientos.

## Volviendo a la Situación

Aplicando [[Tercera Forma Normal#Metodología para obtener un esquema relacional correcto]]:

1. $U = \set{\text{\#E, ENombre, Grupo, Provincia, \#A, ANombre, Nota}}$
2. $F = \begin{cases} \text{\#E} \to \text{ENombre, Grupo, Provincia} \\ \text{\#A} \to \text{ANombre} \\ \text{\#E,\#A} \to \text{\#E,\#A} \\ \text{\#E,\#A} \to \text{Nota} \\ \text{Provincia} \to \text{Grupo}\end{cases}$ 
3. Definimos el esquema relacional **Evaluaciones**$(U,F)$ con llave $\set{\text{\#E,\#A}}$. 

## Cuestionamientos


| <u>\#E</u> | ENombre | Grupo   | Provincia         | <u>\#A</u> | ANombre      | Nota |
| ---------- | ------- | ------- | ----------------- | ---------- | ------------ | ---- |
| $e_1$      | Juan    | ==111== | ==La Habana==     | $a_1$      | Análisis     | 3    |
| $e_1$      | Juan    | ==111== | ==La Habana==     | $a_2$      | Lógica       | 2    |
| $e_1$      | Juan    | ==111== | ==La Habana==     | $a_3$      | Álgebra      | 4    |
| $e_1$      | Juan    | ==111== | ==La Habana==     | $a_4$      | Programación | 5    |
| $e_3$      | Pedro   | ==111== | ==La Habana==     | $a_3$      | Álgebra      | 4    |
| $e_2$      | María   | ==112== | ==Matanzas==      | $a_1$      | Análisis     | 3    |
| $e_2$      | María   | ==112== | ==Matanzas==      | $a_2$      | Lógica       | 3    |
| $e_4$      | Rita    | ==112== | ==Mayabeque==     | $a_2$      | Lógica       | 3    |
| $e_4$      | Rita    | ==112== | ==Mayabeque==     | $a_4$      | Programación | 4    |
| $e_5$      | Carlos  | ==113== | ==Pinar del Río== | $a_3$      | Álgebra      | 3    |

¿Es necesaria esta redundancia?

> Por la propia restricción del problema sabemos que la provincia nos permite conocer el grupo del estudiante

¿Se pudiera insertar un alumno que todavía no ha recibido evaluaciones?

$e_6$ Marcos 111 La Habana NULL NULL NULL

> No, pues el atributo \#A que pertenece a la llave primaria de la relación **Evaluaciones**$(U,F)$ no tiene valor. (es nulo)

¿Qué ocurre si se eliminan las notas del estudiante $e_5$?

> Se perdería toda la información relacionada con la provincia Pinar del Río y el grupo C113

¿Cuántas tuplas tendríamos que modificar si queremos cambiar la provincia de Juan?

> 4 tuplas en una misma transacción.

## ¿Cómo solucionar estas anomalías?


Separando la tabla original en tablas:

Estudiante

| <u>\#E</u> | ENombre | Provincia     |
| ---------- | ------- | ------------- |
| $e_1$      | Juan    | La Habana     |
| $e_2$      | María   | Matanzas      |
| $e_3$      | Pedro   | La Habana     |
| $e_4$      | Rita    | Mayabeque     |
| $e_5$      | Carlos  | Pinar del Río |
Provincia-Grupo

| <u>Provincia</u> | Grupo |
| ---------------- | ----- |
| La Habana        | 111   |
| Matanzas         | 112   |
| Mayabeque        | 112   |
| Pinar del Río    | 113   |

Asignatura

| <u>\#A</u> | ANombre      |
| ---------- | ------------ |
| $a_1$      | Análisis     |
| $a_2$      | Lógica       |
| $a_3$      | Álgebra      |
| $a_4$      | Programación |

Evaluar

| <u>\#E</u> | <u>\#A</u> | Nota |
| ---------- | ---------- | ---- |
| $e_1$      | $a_1$      | 3    |
| $e_1$      | $a_2$      | 2    |
| $e_1$      | $a_3$      | 4    |
| $e_1$      | $a_4$      | 5    |
| $e_3$      | $a_3$      | 4    |
| $e_2$      | $a_1$      | 3    |
| $e_2$      | $a_2$      | 3    |
| $e_4$      | $a_2$      | 3    |
| $e_4$      | $a_4$      | 4    |
| $e_5$      | $a_3$      | 3    |

# Proyección de Dependencias Funcionales

Dados un esquema relacional $R(U,F)$ y un conjunto de atributos $Z$ tal que $Z \subseteq U$, la proyección de un conjunto de dependencias funcionales $F$ sobre un conjunto de atributos $Z$, denotada por $\Pi_Z(F)$ consiste en el conjunto de dependencias funcionales $X \to Y$ de $F^+$ tales que $XY \subseteq Z$.

$$
\Pi_Z(F) = \set{X \to Y \, | \, F  \models X \to Y \land XY \subseteq Z}
$$

# Descomposición de un esquema relacional $R(U,F)$

La descomposición de un esquema relacional $R(U,F)$ se representa por:

$$
\rho = \set{R_1(U_1,F_1),R_2(U_2,F_2),...,R_n(U_n,F_n)}
$$
de manera tal que:

- $U = \bigcup_{i=1}^n U_i$
- Para todo $i = 1,2,...,n$ se cumple que $F_i = \Pi_{U_i}(F)$

**Estudiante**$(U_1,F_1):$                                        **Provincia-Grupo**$(U_2,F_2):$
$U_1 = \set{\text{\#E, Enombre, Provincia}}$                       $U_2 \set{\text{Provincia, Grupo}}$ 
$F_1 = \set{\text{\#E} \to \text{ENombre, Provincia}}$                   $F_2 = \set{\text{Provincia} \to \text{Grupo}}$

**Asignatura**$(U_3,F_3):$                                        **Evaluar**$(U_4,F_4):$
$U_3 = \set{\text{\#A, ANombre}}$                                      $U_4 = \set{\text{\#E, \#A, Nota}}$
$F_3 = \set{\text{\#A} \to \text{ANombre}}$                                  $F_4 = \set{\text{\#E,\#A} \to \text{Nota}}$ 

# Primera Forma Normal

Un esquema relacional $R(U,F)$ está en primera forma normal (1FN) si todos los atributos toman un solo valor del dominio subyacente.

> Toda relación se encuentra en Primera Forma Normal.

# Dependencia funcional completa

Dado un esquema relacional $R(U,F)$ y los atributos $X$, $Y$ de $R$ (posiblemente compuestos), se dice que $Y$ depende funcional y completamente de $X$ si y solo si $Y$ depende funcionalmente de $X$ y no depende de algún subconjunto propio de $X$.

$$
X \stackrel{C}{\to} Y \iff [X \to Y] \land [\nexists X' \subset X : X' \to Y] 
$$

# Segunda Forma Normal

Un esquema relacional $R(U,F)$ está en segunda forma normal (2FN), si está en 1FN y todos los atributos no llaves dependen completamente de la llave.

# Dependencia Funcional Transitiva

Dado un esquema relacional $R(U,F)$ y los atributos $X$, $Y$ y $Z$ de $R$ (posiblemente compuestos), se dice que $Z$ depende funcional y transitivamente de $X$ si y solo si $Y$ y $Z$ dependen funcionalmente de $X$ y, además, $Z$ depende funcionalmente de $Y$. Si $Z$ no dependiera funcionalmente de $Y$, entonces se dice que $Y$ y $Z$ son mutuamente independientes.

**Ejemplo:**

Si tuviéramos la tabla

Estudiante

| <u>\#E</u> | ENombre | Provincia     | Grupo |
| ---------- | ------- | ------------- | ----- |
| $e_1$      | Juan    | La Habana     | 111   |
| $e_2$      | María   | Matanzas      | 112   |
| $e_3$      | Pedro   | La Habana     | 111   |
| $e_4$      | Rita    | Mayabeque     | 112   |
| $e_5$      | Carlos  | Pinar del Río | 113   |

Todavía existe redundancia innecesaria

$$
\#E \to Provincia, Provincia \to Grupo \models \#E \to Grupo 
$$

Existe una dependencia funcional transitiva

# Tercera Forma Normal

Un esquema relacional $R(U,F)$ está en tercera forma normal (3FN), si está en 2FN y los atributos no llaves son mutuamente independientes.

# Cubrimiento Minimal

Dado dos conjuntos de dependencias funcionales $F$ y $G$, se dice que $G$ es un cubrimiento minimal o cobertura irreducible de $F$ si se cumple que:

1. $G \equiv F$ 
2. $G$ no contiene atributos redundantes
3. $G$ no contiene dependencias redundantes

## Algoritmo para obtener un cubrimiento minimal

**Entrada**: Un conjunto de dependencias funcionales $F$ sobre un universo de atributos $U$.
**Salida**: Un conjunto de dependencias funcionales $G$, $G \equiv F$ , sin atributos ni dependencias redundantes.
**Método**:
1. A partir de $F$ construir un conjunto de dependencias funcionales $F'$ tal que cada dependencia funcional sea de la forma $X \to A$.
2. A partir de $F'$ construir un conjunto de dependencias funcionales, $F''$, donde ningún determinante contiene atributos redundantes; o sea, que para ninguna $X \to A$ en $F'$ y $Z \subset X$ se cumpla que $F' - \set{X \to A} \cup \set{Z \to A}$ sea equivalente a $F'$.
3. A partir de $F''$ construir un conjunto de dependencias funcionales $F'''$ que no contenga dependencias redundantes; o sea, que para ninguna $X \to A$ en $F''$ el conjunto de dependencias funcionales $F'' - \set{X \to A}$ sea equivalente a $F''$.

## Algoritmo para obtener una descomposición en 3FN

**Entrada**: Un esquema relacional $R(U,F)$, $F$ es un conjunto irreducible de dependencias funcionales.
**Salida**: Una descomposición $\rho = (R_1,R_2,...,R_n)$, tal que los esquemas relacionales $R_i(U_i,F_i)$ están en 3FN con respecto a $\Pi_{U_i}(F), \, \forall i = 1,...,n$.
**Método**:
1. Por cada dependencia funcional $X \to A_i$ en $F$ crear el esquema relacional $R_i(U_i,F_i)$ tal que $U_i = X \cup \set{A_i}$ y $F_i = \set{X \to A_i}$. Si en $F$ se tiene $X \to A_1, X \to A_2,..., X \to A_k$ se puede utilizar un esquema relacional de la forma $R_j(U_j,F_j)$ con $U_j = X \cup \set{A_1,A_2,...,A_k}$ y $F_j = \Pi_{U_j}(F).$
2. Si en $U$ existe algún atributo que no está contenido en ninguna dependencia funcional de $F$, este atributo puede formar un esquema relacional por sí mismo.
3. Luego, $\rho = (R_1,R_2,...,R_n)$
