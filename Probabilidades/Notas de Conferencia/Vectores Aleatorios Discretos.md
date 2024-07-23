
# Tema: Vectores Aleatorios Discretos

## Introducción

Muchas veces es de interés considerar más de una variable aleatoria.

## Vector Aleatorio

### Definición 1
Al par $(X,Y)$ le llamaremos vector aleatorio si $X$ e $Y$ son variables aleatorias. Puede darse el caso que una variable sea continua y otra discreta, pero solo consideraremos el caso en que ambas variables sean continuas o ambas variables sean discretas.

### Ejemplo 1 
Se lanza un dado y una moneda de forma independiente, sea $X$ el resultado de la moneda (1 si sale cara y 0 si sale escudo) y $Y$ el resultado del dado, entonces $(X,Y)$ es un vector aleatorio discreto que toma los valores:
$$
\{(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)\}
$$

### Definición 2 (Función de Probabilidad Conjunta)

**La función que toma valores $\{(a_i,b_j)\}_{i,j \in \mathbb{N}}$ es:**
$$
P_{(X,Y)}(a_i,b_j) = P(X = a_i, Y = b_j), \text{ } \forall(a_i,b_j),
$$
**donde $P(X = a_i, Y = b_j)$ es la probabilidad de la intersección de los sucesos $X = a_i$ e $Y = b_j.$**

En el [Ejemplo 1](#ejemplo-1), la función de probabilidad conjunta es:

| X\Y | 1              | 2              | 3              | 4              | 5              | 6              |
| --- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 0   | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ |
| 1   | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ | $\frac{1}{12}$ |

### Ejemplo 2

Se extraen $3$ bolas de una urna que contiene $4$ bolas rojas y $2$ bolas negras, se definen las v.a $X$ e $Y$ que cuantifican la cantidad de bolas rojas y negras extraídas respectivamente.

En base a los valores que puede tomar el vector $(X,Y)$, la probabilidad conjunta resulta en:

| X\Y | 0                                                | 1                                               | 2                                               |
| --- | ------------------------------------------------ | ----------------------------------------------- | ----------------------------------------------- |
| 1   | 0                                                | 0                                               | $\frac{\binom{4}{1}\binom{2}{2}}{\binom{6}{3}}$ |
| 2   | 0                                                | $\frac{\binom{4}{2}\binom{2}{1}}{\binom{6}{3}}$ | 0                                               |
| 3   | $\frac{\binom{4}{3} \binom{2}{0}}{\binom{6}{3}}$ | 0                                               | 0                                               |
### Proposición 1

**Sea $(X,Y)$ un vector aleatorio con función de probabilidad conjunta $P_{(X,Y)}$ que toma valores $\{(a_i,b_j)\}_{i,j \in \mathbb{N}},$ entonces:**
$$
\sum_{i=1}^\infty\sum_{j=1}^\infty P_{(X,Y)}(a_i,b_j) = \sum_{j=1}^\infty\sum_{i=1}^\infty P_{(X,Y)}(a_i,b_j) = 1
$$
**Demostración:**
Por [Axioma 1 de Kolmogorov](Axiomas%20de%20Kolmogorov) tenemos que $P(\Omega) = 1$.
Notemos que cada par $(a_i,b_j)_{i,j \in \mathbb{N}}$, representa en sí mismo una partición del espacio muestral $\Omega$, por tanto son elementos disjuntos, lo cual nos permite reescribir $\Omega$ de la forma:

$$
\Omega = \bigcup_{i=1}^\infty A_i.
$$
Haciendo uso de lo planteado anteriormente:
$$
P(\Omega) = P\left(\bigcup_{i=1}^\infty A_i \right) = 1.
$$
Recordemos que por [Axioma 3 de Kolmogorov](Axiomas%20de%20Kolmogorov):
$$
P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i), \text{ si } A_i \cap A_j = \emptyset, \forall i,j \in \mathbb{N}, i \neq j, 
$$
lo cual se cumple en nuestro caso, por lo que:
$$
\sum_{i=1}^\infty P(A_i) = 1
$$
Como en este caso necesitamos sumar todos los pares $(a_i,b_j)$, entonces:
$$
\sum_{i=1}^\infty\sum_{j=1}^\infty P_{(X,Y)}(a_i,b_j) = 1.
$$
Como esta serie converge absolutamente y la probabilidad de cualquier suceso siempre es no negativa, entonces podemos conmutar los sumandos:
$$
\sum_{j=1}^\infty\sum_{i=1}^\infty P_{(X,Y)}(a_i,b_j) = 1.\text{ }\blacksquare
$$
### Definición 3

**La función de distribución conjunta del vector aleatorio discreto $(X,Y)$ es:**

$$
F_{(X,Y)}(x,y) = P(X \leq x, Y \leq y), \text{ } \forall(x,y) \in \mathbb{R}^2
$$
### Definición 4

**Las funciones de probabilidad marginal de las variables aleatorias $X$ e $Y$ son:**
$$
P_X(a_i) = \sum_{j=1}^\infty P_{(X,Y)}(a_i,b_j) = \sum_{j=1}^\infty P(X = a_i, Y = b_j), \text{ y }
$$
$$
P_Y(bj) = \sum_{i=1}^\infty P_{(X,Y)}(a_i,b_j) = \sum_{i=1}^\infty P(X = a_i, Y = b_j), \text{ } \forall i \in \mathbb{N}
$$
respectivamente.

En el [Ejemplo 1](#ejemplo-1), podemos comprobar que la función de probabilidad marginal para $X$ es:

| $a_i$        | 0             | 1             |
| ------------ | ------------- | ------------- |
| $P(X = a_i)$ | $\frac{1}{2}$ | $\frac{1}{2}$ |
(Fijamos cada fila de $X$ y sumamos todos los valores de las columnas de $Y$)
y para $Y$:

| $b_j$        | 1             | 2             | 3             | 4             | 5             | 6             |
| ------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| $P(X = b_j)$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ | $\frac{1}{6}$ |

### Definición 5

**Se dice que las v.a discretas $X$ e $Y$ son independientes si parat odos los valores admisibles $(a_i,b_j), \text{ } i,j \in \mathbb{N}$, se cumple la siguiente condición:**
$$
P(X = a_i, Y = b_j) = P(X = a_i)P(Y = b_j).
$$

En el [Ejemplo 1](#ejemplo-1) las v.a $X$ e $Y$ son independientes, mientras que en el [Ejemplo 2](#ejemplo-2) son dependientes y para demostrarlo basta con que no se cumpla para algún caso el planteamiento anterior para un par de valores específicos.

$$
P(X = 1, Y = 1) = 0
$$

$$
\neq P(X = 1)P(Y = 0) = \frac{\binom{4}{1}\binom{2}{2}}{\binom{6}{3}}\times\frac{\binom{4}{3}\binom{2}{0}}{\binom{6}{3}}
$$

### Proposición 2

**Sea $g: \mathbb{R}^2 \rightarrow \mathbb{R}$, la esperanza matemática o valor esperado de la v.a $g(X,Y)$ se calcula mediante la expresión:**

$$
E[g(X,Y)] = \sum_{i=1}^\infty\sum_{j=1}^\infty  g(a_i,b_j)P(X = a_i,b_j).
$$
### Proposición 3
**Sean $X$ e $Y$ variables aleatorias independientes, entonces $E[XY] = E[X]E[Y]$. La demostración de esta proposición ya se hizo en las propiedades del valor esperado en [Variable Aleatoria Discreta](Variable%20Aleatoria%20Discreta%201#proposición-4).

### Definición 6

La covarianza y el coeficiente de correlación lineal se calculan mediante las siguientes expresiones respectivamente:

$$
cov(X,Y) = E[XY] - E[X]E[Y]
$$
$$
\rho = \frac{cov(X,Y)}{\sqrt{V(X)V(Y)}}
$$
donde $-1 \leq \rho \leq 1$

#### Clasificación de la relación lineal entre dos variables aleatorias

- **Si $-1 \leq \rho \leq -0.7$ se dice que existe relación lineal inversa entre las v.a**
- **Si $-0.4 \leq \rho \leq 0.4$ se dice que no existe relación lineal.**
- **Si $0.7 \leq \rho \leq 1$ se dice que la relación lineal es directa.**

###  Proposición 4

**Sean $X$ e $Y$ variables aleatorias, entonces:**

- **$X$ e $Y$ v.a independientes $\implies cov(X,Y) =0$.**
- **$V(X+Y) = V(X) + V(Y) + 2cov(X,Y)$.**
- **$X$ e $Y$ v.a independientes $\implies V(X+Y) = V(X) + V(Y)$.**
### Definición 7

**Sea $b_j$ un valor de la v.a $Y$ fijo, se denomina distribución condicional de $X$ dado $Y = b_j$ a la variable aleatoria que toma valores $a_i$ con probabilidad:**
$$
P(X = a_i | Y = b_j) = \frac{P(X = a_i, Y = b_j)}{P(Y = b_j)}
$$
A esta variable aleatoria se le denota como $X|Y = b_j$. 