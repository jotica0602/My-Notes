> Diseño Lógico. Modelo Relacional.

# Modelo Relacional

Se introducen una serie de conceptos para poder conformar lo que posteriormente serían las estructuras de datos que utilizaremos: las tablas.

## Dominio 

Conjunto de valores que puede tomar un atributo.

## Relación

**Teoría de Conjuntos**: La relación *n-aria* sobre los dominios $D_1,D_2,\dots,D_n$ es el conjunto de tuplas ordenadas $(a_1,a_2,\dots,a_n)$ pertenecientes al producto cartesiano $D_1 \times D_2 \times \dots \times D_n$, donde $a_i \in D_i$ para cada $i \in 1,\dots,n$, cuya condición $R(a_1,a_2,\dots,a_n)$ se satisface.

$$
R = \set{(a_1,a_2,\dots,a_n) \in D_1 \times D_2 \times \dots \times D_n | R(a_1,a_2,\dots,_an)}
$$

**Bases de Datos**: Una relación $R$ definida sobre un conjunto de dominios $D_1,D_2,\dots,D_n$, no necesariamente distintos se compone de:

- **La cabecera**: formada por un conjunto finito de pares de atributo-dominio
	$$
	\set{(A_1 : D_1), (A_2 : D_2),\dots,(A_n : D_n)},
	$$
	tal que el atributo $A_j$ corresponde al y solo al dominio $D_j, \forall j = 1,2,\dots,n$
	
- **El cuerpo**: está formado por un conjunto finito de tuplas, el cual varía en el tiempo. Cada tupla, a su vez está formada por un conjunto de pares atributo-valor.
	$$\set{(A_1:V_{i1}),(A_2:V_{i2}),\dots, (A_n:V_{in})}, (i = 1,2,\dots,m)$$
	tal que $m$ es el número de tuplas en el conjunto $V_{ij} \in D_j$ para todo par $(A_j:V_{ij})$ con $j = 1,2,\dots,n$ 
	(A nivel de tabla $i$ sería el número de la fila y $j$ el número de columna)


**Ejemplo de cabecera para la relación Jugador:**

$\set{(\#J:\mathbb{N}),(Nombre: \mathbb{S}),(Trofeos:\mathbb{N}),(TrofeosMax:\mathbb{N})}$

> Donde $(\#J, Nombre, Trofeos, TrofeosMax)$ es la cabecera.

**Ejemplo de tupla para la relación Jugador:**

$\set{(\#J : 1), (Nombre : Juan), (Nivel : 13), (Trofeos : 7500), (TrofeosMax : 7560)}$

> Donde  $(1,Juan,13,7500,7560)$ es el cuerpo.

A nivel de tabla la cabecera serían las columnas y el cuerpo las filas, ilustrémoslo con el siguiente ejemplo:

**Cabecera:**

| ID_Estudiante | Nombre | Apellido | Edad | Carrera |
|---------------|--------|----------|------|---------|
| INT           | INT    | VARCHAR  | INT  | VARCHAR |

Donde los pares atributo-dominio $(A_i,D_i)$ son: 
- $(\text{ID\_Estudiante}, \text{INT})$
- $(\text{Nombre},\text{INT})$
- $(\text{Apellido},\text{VARCHAR})$
- $(\text{Edad},\text{INT})$
- $(\text{Carrera},\text{VARCHAR})$


**Cuerpo:**


| ID_Estudiante | Nombre | Apellido | Edad | Carrera      |
| ------------- | ------ | -------- | ---- | ------------ |
| 1             | Ana    | Pérez    | 21   | Ingeniería   |
| 2             | Juan   | López    | 22   | Medicina     |
| 3             | María  | García   | 20   | Derecho      |
| 4             | Pedro  | Torres   | 23   | Arquitectura |

Donde las tuplas $(A_i,V_{ij})$ son: 

- $\set{(\text{ID\_Estudiante},1),(\text{Nombre},\text{Ana}),(\text{Apellido},\text{Pérez}),(\text{Edad},21), (\text{Carrera},\text{Ingeniería})}$
- $\set{(\text{ID\_Estudiante},2),(\text{Nombre},\text{Juan}),(\text{Apellido},\text{López}),(\text{Edad},22),(\text{Carrera},\text{Medicina})}$
- $\set{(\text{ID\_Estudiante},3),(\text{Nombre},\text{María}),(\text{Apellido},\text{García}),(\text{Edad},20),(\text{Carrera},\text{Derecho})}$
- $\set{(\text{ID\_Estudiante},4),(\text{Nombre},\text{Pedro}),(\text{Apellido},\text{Torres}),(\text{Edad},23),(\text{Carrera},\text{Arquitectura})}$

> El cuerpo está conformado por todas las filas de la tabla Estudiante, donde cada fila es una **tupla**.

## Llave Candidata

Un conjunto de uno o más atributos $K = \set{A_1,A_2,\dots,A_n}$ es una llave candidata de la relación $R$ si cumple las siguientes propiedades:

1) **Unicidad**: En cualquier momento dado, no existen dos tuplas distintas de $R$ con los mismos valores para $A_1,A_2,\dots,A_n$.
2) **Minimalidad**: Ningún subconjunto propio de $K$ tiene la propiedad de unicidad.

## Llave Primaria

Es una de las llaves candidatas que se selecciona como llave de la relación.

## Llave Foránea

Un conjunto de uno o más atributos $F = \set{A_1,A_2,\dots,A_n}$ de una relación $R$, correspondientes a los dominios $D_1,D_2,\dots,D_n$ respectivamente, es una llave foránea referente a la relación $R'$ si:
1) La llave primaria de $R'$ es un conjunto de atributos $P = \set{B_1,B_2,\dots,B_n}$ correspondientes a los dominios $D_1,D_2,\dots,D_n$ respectivamente.
2) Existe un acuerdo de correspondencia entre los atributos $A_i$ y $B_i$ para todo $i = 1,2,\dots,n$

Una tupla de $t \in R$ referencia a una tupla $t' \in R'$ si el valor de $A_i$ en la tupla $t$ es igual al valor de $B_i$ en la tupla $t'$ para todo $i = 1,2,\dots,n$.

**Ejemplo:**

Tabla: Pedidos $(R)$^pedidos

| PedidoID | Fecha      | ClienteID |
|----------|------------|-----------|
| 101      | 2023-01-15 | 1         |
| 102      | 2023-02-20 | 2         |
| 103      | 2023-03-25 | 1         |

En este caso el conjunto de atributos foráneos $F$ está constituido por uno solo, el cual es **ClienteID**, cuyo dominio es $\mathbb{N}$.    

Tabla: Clientes $(R')$ 

| ClienteID | Nombre     | Dirección   |
| --------- | ---------- | ----------- |
| 1         | Juan Pérez | Calle 123   |
| 2         | Ana García | Avenida 456 |
| 3         | Luis Gómez | Plaza 789   |
En la tabla [[Modelo Relacional#^pedidos]], la tupla t: $\set{(\text{PedidoID},101),(\text{Fecha},2023-01-15),(\text{ClienteID},1)}$ referencia a la tupla  $t'$: $\set{(\text{ClienteID},1),(\text{Nombre},\text{Juan Pérez}),(\text{Calle},123)}$, donde el valor $A_3:\text{ClienteID}$ de $t$ es igual al valor $B_1 = \text{ClienteID}$ de la tupla $t'$.

## Esquema de una relación

El esquema de una relación es una especificación de su estructura, la cual es independiente de las tuplas que contiene el cuerpo. El esquema se compone de:
- El nombre de la relación.
- La cabecera.
- La llave primaria.
- Las llaves foráneas.

En una misma base de datos una relación se identifica unívocamente por su nombre.

## Instancia de una Relación

Se refiere al conjunto de tuplas que constituye el cuerpo de la relación en un momento específico del tiempo.

**Ejemplo:**

En la tabla Clientes, su instancia está dada por el conjunto de tuplas:

- $\set{(\text{ClienteID},1),(\text{Nombre},\text{Juan Pérez}),(\text{Dirección},\text{Calle 123})}$
- $\set{(\text{ClienteID},2),(\text{Nombre},\text{Ana García}),(\text{Dirección},\text{Avenida 456})}$
- $\set{(\text{ClienteID},3),(\text{Nombre},\text{Luis Gómez}),(\text{Dirección},\text{Plaza 789})}$

> Las relaciones las denotaremos por $R_1,R_2,...,R_n$ respectivamente 

## Estado de una base de datos

- El conjunto de instancias $\set{r_1,r_2,...,r_n}$ de las relaciones $R_1,R_2,...,R_n$ respectivamente que conforman la base de datos en un instante de tiempo específico es a lo que se le denomina **estado de una base de datos**.
- Un **estado** es **consistente** si satisface cada una de las **restricciones de integridad** definidas sobre la base de datos.

## Restricciones de integridad

### Integridad de las Entidades

Todos los atributos de una llave primaria deben ser no nulos, pues como la llave es minimal, si su valor no es único

**Ejemplo:**

| <u>A</u>:$\mathbb{N}$ | <u>B</u>:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | --------------------- | -------------- |
| 1                     | 2022                  | 1000           |
| 1                     | 2021                  | 1000           |
| 2                     | 2022                  | 1200           |
Si quisiéramos insertar la tupla:
$\set{(\text{A}:1),(\text{B}:\text{NULL}),(\text{C}:1000)}$

No sería posible, pues la llave es minimal y si su valor está incompleto entonces no es único.

### Integridad Referencial

- Todos los atributos de una llave foránea deben ser no nulos o todos deben ser nulos.
- El valor de una llave foránea tiene que ser un valor existente de la llave primaria en la relación a la que hace referencia.

**Ejemplo 1:**
Relación R:  ^ejemplo-1

| <u>A</u>:$\mathbb{N}$ | <u>B</u>:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | --------------------- | -------------- |
| 1                     | 2022                  | 1000           |
| 1                     | 2021                  | 1000           |
| 2                     | 2022                  | 1200           |

Relación S:
FK: (A,B) REFERENCES R(A,B)

| <u>D</u>:$\mathbb{N}$ | A:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 2                     | 2              | 2022           |

**Ejemplo 2:**

Utilizando la misma tabla del [[Modelo Relacional#^ejemplo-1]] 
Relación S:
FK: (A,B) REFERENCES R(A,B)

| <u>D</u>:$\mathbb{N}$ | A:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 2                     | NULL           | 2022           |
No es posible distinguir a qué tupla de la relación R referencia la tupla de la relación S, pues tenemos dos tuplas cuyo atributo **B** tiene valor 2022. 

### Integridad de los Dominios

- Todos los valores de un atributo de una relación tiene que provenir del dominio pertinente.

# Operaciones

## Transacciones

Una transacción es un conjunto de operaciones que modifican el estado de la base de datos y:

- **A**tomicity: Se considera como una sola operación, es decir, se realizan todos los cambios o no se realiza ninguno.
- **C**onsistency: El estado de la base de datos es consistente antes y después de ejecutarse la transacción, <u>pudiendo no serlo durante la operación</u>
- **I**solation: El estado intermedio de una transacción <u>no es visible por el resto de las transacciones: se aisla</u>.
- **D**urability: Luego de ejecutada la transacción, <u>los cambios de estado son persistentes y no pueden ser deshechos</u>, incluso, en el caso de fallos del sistema.

> Esto es conocido como las propiedades **ACID**.

## Operaciones que modifican el estado

### Insertar

1) Debemos comprobar que todas las metarreglas se cumplan para la tupla que vamos a insertar.

### Eliminar

1) No tenemos que comprobar las metarreglas en la tupla que vamos a eliminar pues ya está insertada.
2) La relación debe de avisar al resto de relaciones que un valor de llave primaria se va a eliminar.
3) Las relaciones que referencian a la tupla eliminada tienen tres opciones:
	1) Detener la eliminación.
	2) Hacer el valor de la llave foránea.
	3) Eliminar las tuplas que utilicen dicho valor de llave foránea.
### Actualizar

Esta operación puede interpretarse como el proceso de insertar una tupla y eliminar una tupla.

1) Debemos hacer las comprobaciones pertinentes a la inserción de la tupla modificada.
2) Si el valor de la llave primaria se modifica debemos avisar al resto de las relaciones para que se actualice el valor de la llave foránea.
3) Realizar una transacción de dos operaciones:
	1) Eliminar la tupla original.
	2) Insertar la tupla modificada.
## Operaciones para responder consultas

### Álgebra relacional

- Este es el lenguaje procedimental para el manejo y construcción de relaciones
- Compuesta por operandos (variables y relaciones) y operadores (extensión de la Teoría de Conjuntos).
- Las operaciones del álgebra relacional manipulan y producen relaciones.
#### Asignación

Se utiliza para destinar a una variable de relación el valor que se crea a partir de la aplicación de cualesquiera de las operaciones sobre las relaciones existentes.

#### Renombrar

Operación que no afecta el conjunto de tuplas presentes en la relación sino que modifica el **esquema de la relación**. En específico cambiar el nombre tanto de los atributos como de la relación.

#### Operaciones de Teoría de Conjuntos

##### Condiciones
1) Dos relaciones $R$ y $S$, no necesariamente distintas.
2) $R$ y $S$ **tienen el mismo esquema,** exceptuando, quizás, el nombre.

##### Operaciones de Conjuntos
###### Unión
$R \cup S$: es una relación con el mismo esquema, a excepción del nombre, cuyo cuerpo consiste en las tuplas que pertenecen a la relación $R$ o a la relación $S$ o ambas. Las tuplas duplicadas se eliminan.
###### Intersección
$R \cap S$: es una relación con el mismo esquema, a excepción del nombre, cuyo cuerpo consiste en las tuplas que pertenecen tanto a la relación $R$ como a la relación $S$.
###### Diferencia
$R - S$: es una relación con el mismo esquema, a excepción del nombre, cuyo cuerpo consiste en las tuplas que pertenecen a la relación $R$ y no a la relación $S$.

**Ejemplo:**

Relación $R$:

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 2                     | 3              |
| 3                     | 4              |
| 4                     | 4              |

Relación $S$:

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 2                     | 4              |
| 5                     | 7              |
| 6                     | 1              |

**Unión $(R \cup S)$**:

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 2                     | 3              |
| 3                     | 4              |
| 4                     | 4              |
| 5                     | 7              |
| 6                     | 1              |

> Notemos que para valores iguales de las llaves primarias se toma el del operando a la izquierda. En el caso $\set{(\text{A}:2),(\text{B}:3)}$ de $R$ y $\set{(\text{A}:2),(\text{B}:4)}$ de $S$, esta unión resulta en $\set{(\text{A}:2),(\text{B}:3)}$

**Intersección $(R \cap S)$**:

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 2                     | 3              |

> Aquí sucede lo mismo con las tuplas $\set{(\text{A}:2),(\text{B}:3)}$ de $R$ y $\set{(\text{A}:2),(\text{B}:4)}$ de $S$, cuya intersección resulta en $\set{(\text{A}:2),(\text{B}:3)}$.  



## Operaciones que remueven parte de una relación

### Restricción o Selección (R $\sigma$ F)

$R \, \sigma \, F$ produce una nueva relación con el mismo esquema que $R$, a excepción del nombre, cuyo cuerpo es un subconjunto del cuerpo de $R$. Es decir, las tuplas en la relación resultante son aquellas tuplas de $R$ que satisfacen la condición F, expresada mediante una fórmula bien formada.

**Ejemplo:**

Relación $R:$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 1                     | 2              | 5              |
| 2                     | 2              | 7              |
| 3                     | 4              | 7              |
| 4                     | 4              | 7              |

Relación $R \, \sigma \, (B = 4 \land C = 7):$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 3                     | 4              | 7              |
| 4                     | 4              | 7              |

Relación $R \, \sigma \, (B + C > 7):$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 2                     | 2              | 7              |
| 3                     | 4              | 7              |
| 4                     | 4              | 7              |

Relación $R \, \sigma \, (B = 2):$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 1                     | 2              | 5              |
| 2                     | 2              | 7              |

### Proyección $\pi_{A_1,A_2,\dots,A_n}(R)$

$\pi_{A_1,A_2,\dots,A_n}(R)$ produce una relación cuyo esquema solo contiene los atributos $A_1,A_2,...,A_n$ de $R$. El cuerpo de la relación consiste en todas las tuplas $\set{(A_1:a_1),(A_2:a_2),\dots,(A_n:a_n)}$ tal que existe una tupla en $R$ cuyo valor asociado al atributo $A_i$ es $a_i$ para todo $i = 1,\dots,n$. 

**Ejemplo:**

Relación $R:$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 1                     | 2              | 5              |
| 2                     | 2              | 7              |
| 3                     | 4              | 7              |
| 4                     | 4              | 7              |

Relación $\pi_{A,B}(R):$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 2                     | 2              |
| 3                     | 4              |
| 4                     | 4              |

Relación $\pi_B(R):$

| B:$\mathbb{N}$ |
| -------------- |
| 2              |
| 4              |

Relación $\pi_{B,C}(R):$

| B:$\mathbb{N}$ | C:$\mathbb{N}$ |
| -------------- | -------------- |
| 2              | 5              |
| 2              | 7              |
| 4              | 7              |

### Producto cartesiano $R \times S$: 

Es una nueva relación cuyo encabezado es la unión de los encabezados de la relación $R$ y la relación $S$. La llave primaria de la nueva relación es la unión de las llaves primarias de $R$ y $S$. Y las llaves foráneas de $R$ y $S$ son también llaves foráneas en $R \times S$. El cuerpo consiste en el conjunto resultante de unir cada tupla de $R$ con cada una de las tuplas de $S$.

**Ejemplo:**

Relación $R:$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 3                     | 4              |

Relación $S:$

| <u>B</u>:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 2                     | 5              | 6              |
| 4                     | 7              | 8              |
| 9                     | 10             | 11             |

Relación $R \times S:$

| <u>A</u>:$\mathbb{N}$ | R.B:$\mathbb{N}$ | S.B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | ---------------- | ---------------- | -------------- | -------------- |
| 1                     | 2                | 2                | 5              | 6              |
| 1                     | 2                | 4                | 7              | 8              |
| 1                     | 2                | 9                | 10             | 11             |
| 3                     | 4                | 2                | 5              | 6              |
| 3                     | 4                | 4                | 7              | 8              |
| 3                     | 4                | 9                | 10             | 11             |

## Operaciones que combinan relaciones

### Natural Join $R \Join S$ 

Sean $R$ y $S$ dos relaciones, no necesariamente distintas, distinguimos los siguientes conjuntos de atributos:

- El conjunto $R_1,\dots,R_m$ son atributos de $R$ y no de $S$.
- El conjunto $S_1,\dots,S_n$ son atributos de $S$ y no de $R$.
- El conjunto $A_1,\dots,A_k$ son atributos comunes de $R$ y $S$, es decir, atributos con el mismo nombre y mismo dominio asociado en ambas relaciones.

La operación $R \Join S$ se define como:

$$
\pi_{R_1,\dots,R_m,S_1,\dots,S_n,R.A_1,\dots,R.A_k} ((R \times S) \, \sigma \, (R.A_1= S.A_1 \land \dots \land R.A_k = S.A_k))
$$

**Ejemplo:**

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ |
| --------------------- | -------------- |
| 1                     | 2              |
| 3                     | 4              |

Relación $S:$

| <u>B</u>:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- |
| 2                     | 5              | 6              |
| 4                     | 7              | 8              |
| 9                     | 10             | 11             |

Relación $R \times S:$

| <u>A</u>:$\mathbb{N}$ | R.B:$\mathbb{N}$ | S.B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | ---------------- | ---------------- | -------------- | -------------- |
| 1                     | 2                | 2                | 5              | 6              |
| 1                     | 2                | 4                | 7              | 8              |
| 1                     | 2                | 9                | 10             | 11             |
| 3                     | 4                | 2                | 5              | 6              |
| 3                     | 4                | 4                | 7              | 8              |
| 3                     | 4                | 9                | 10             | 11             |

$F: R.B = S.B$

| <u>A</u>:$\mathbb{N}$ | R.B:$\mathbb{N}$ | S.B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | ---------------- | ---------------- | -------------- | -------------- |
| ==1==                 | ==2==            | ==2==            | ==5==          | ==6==          |
| 1                     | 2                | 4                | 7              | 8              |
| 1                     | 2                | 9                | 10             | 11             |
| 3                     | 4                | 2                | 5              | 6              |
| ==3==                 | ==4==            | ==4==            | ==7==          | ==8==          |
| 3                     | 4                | 9                | 10             | 11             |

Relación $(R \times S) \, \sigma \, F:$

| <u>A</u>:$\mathbb{N}$ | R.B:$\mathbb{N}$ | S.B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | ---------------- | ---------------- | -------------- | -------------- |
| 1                     | 2                | 2                | 5              | 6              |
| 3                     | 4                | 4                | 7              | 8              |

Relación $\pi_{A,R.B,C,D}((R \times S) \, \sigma \, F):$ 

| <u>A</u>:$\mathbb{N}$ | R.B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | ---------------- | -------------- | -------------- |
| 1                     | 2                | 5              | 6              |
| 3                     | 4                | 7              | 8              |

Relación $R \Join S:$

| <u>A</u>:$\mathbb{N}$ | B:$\mathbb{N}$ | C:$\mathbb{N}$ | D:$\mathbb{N}$ |
| --------------------- | -------------- | -------------- | -------------- |
| 1                     | 2              | 5              | 6              |
| 3                     | 4              | 7              | 8              |

> Natural Join a fin de cuentas lo que hace es aplicar un producto cartesiano entre dos relaciones y de este proyectar las tuplas cuyas cabeceras tengan igual valor.  
### Theta Join ($\theta$-Join)

Sean $R$ y $S$ dos relaciones, no necesariamente distintas, definimos el $\theta$-Join de $R$ y $S$ como:

$$
(R \times S) \, \sigma \, F : F = \theta
$$

donde $\theta$ es una condición, expresada mediante una fórmula bien formada.