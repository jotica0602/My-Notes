Alejandro Echevarría Brunet

# CP\#8: Vectores Aleatorios Discretos

## Ejercicio 1:

Sea $(X,Y)$ un vector aleatorio discreto con función de probabilidad conjunta dada por:

| Y\X | 2   | 4   | 6   |
| --- | --- | --- | --- |
| 1   | 0.1 | a   | 0   |
| 3   | 0   | 0.2 | 0.2 |
| 5   | 0.3 | 0   | b   |

a) Determine los valores de $a$ y de $b$ si se conoce que $E[X] = 3.8$.
b) Halle la función de probabilidad marginal para cada variable.
c) Diga si $X$ e $Y$ son independientes.
d) Calcule $E[XY]$.

### Solución:

a) Por [[Vectores Aleatorios Discretos#Proposición 1]] tenemos que: 

$$
P(\Omega) = \sum_{i=1}^{\infty}\sum_{j=1}^{\infty}P_{(X,Y)}(x_i,y_j) = 1
$$

> La suma de las probabilidades de todos los elementos del espacio muestral es igual a 1.

$$
P(X = 2, Y = 1) + P(X = 2, Y = 3) + P(X = 2, Y = 5) + P(X = 4, Y = 1) + P(X = 4, Y = 3) + P(X = 4, Y = 5) + P(X = 6, Y = 1) + P(X = 6, Y = 3) + P(X = 6, Y = 5) = 1
$$

$$
\implies 0.1 + 0 + 0.3 + a + 0.2 + 0 + 0 + 0.2 + b = 1
$$

$$
a + b = 0.2
$$

Conociendo que $E[X] = 3.8$ y apoyándonos en la definición de $E[X]$:

$$
E[X] = \sum_{i = 1}^{\infty}x_i P(X = x_i)
$$

$$
E[X] = 2 * (0.1 + 0 + 0.3) + 4 * (a + 0.2 + 0) + 6 * (0 + 0.2 + b) = 3.8 
$$

> Recordemos que  $P(X = x_i) = \sum_{s:X(s) = x_i}^{}P(s)$.

$$
\implies 4a + 6b = 1
$$

Resolviendo el sistema de ecuaciones lineales:

$$
a  +  b = 0.2
$$

$$
4a + 6b = 1 
$$

Obtenemos que $a = b = 0.1$

b) Recordemos que la probabilidad marginal de cada variable componente que a su vez es una componente de un vector aleatorio de dos dimensiones está dada por:

$$
P(X = x_i) = \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} P(X = x_i, Y = y_j)
$$


Probabilidad Marginal de $X$ |-------| Probabilidad Marginal de $Y$


| $X = x_i$    | 2   | 4   | 6   | $Y = y_i$    | 1   | 3   | 5   |
| ------------ | --- | --- | --- | ------------ | --- | --- | --- |
| $P(X = x_i)$ | 0.4 | 0.3 | 0.3 | $P(Y = y_i)$ | 0.2 | 0.4 | 0.4 |

c) Para que las variables aleatorias de un vector aleatorio sean independientes debe cumplirse que 

$$
P(X = x_i, Y = y_j) = P(X = x_i)P(Y = y_j), \ \forall i,j \in \mathbb{N}
$$

Es fácil comprobar que para los valores $X = 2$ e $Y = 3$:

$$
P(X = 2, Y = 3) \neq P(X = 2)P(Y = 3),
$$

$$
0 \neq 0.16
$$

$\therefore$ No son independientes.

d) 

$$
E[XY] = \sum_{i=1}^{\infty}\sum_{j=1}^{\infty} x_i y_j P(X = x_i, Y = y_j)
$$

$$
= 2 * 1 * P(X = 2, Y = 1) + 2 * 3 * P(X = 2, Y = 3) + 2 * 5 * P(X = 2, Y = 5) + 4 * 1 * P(X = 4, Y = 1) + 4 * 3 * P(X = 4, Y = 3) + 4 * 5 * P(X = 4, Y = 5) + 6 * 1 * P(X = 6, Y = 1) + 6 * 3 * P(X = 6, Y = 3) + 6 * 5 * P(X = 6, Y = 5) 
$$

$$
= 2 * 1 * 0.1 + 2 * 3 * 0 + 2 * 5 * 0.3 + 4 * 1 * 0.1 + 4 * 3 * 0.2 + 4 * 5 * 0 + 6 * 1 * 0 + 6 * 3 * 0.2 + 6 * 5 * 0.1
$$

$$
= \boxed{12.6}
$$

## Ejercicio 2:

Cuatro amigos deciden enviar cada uno una carta a cualquiera de los otros 3 del grupo. Sea $X$ la variable aleatoria que define el número de cartas que recibe el primero de ellos e $Y$ la variable aleatoria que define el número de cartas que recibe el segundo de ellos. Complete en la tabla la función de probabilidad conjunta.

|Y\X|       0                       |       1       |       2       |       3       |
|---|-------------------------------|---------------|---------------|---------------|
|0  |$\frac{4}{81}$                 |               |               |               |
|1  |$\frac{10}{81}$|$\frac{17}{81}$|               |               |               |
|2  |$\frac{8}{81}$                 |               |               |               |
|3  |$\frac{2}{81}$                 |               |               |               |

a) Halle $P_Y$ y $F_Y$.
b) Halle $E[X|Y = 1]$.
c) Calcule $F_{X|Y>0}$.
d) Diga si $X$ e $Y$ son independientes.

### Solución:

> Observación: Una persona no puede enviarse una carta a sí misma, solo a los demás. 

Notemos que el orden $(X,Y)$, $(Y,X)$ no influye en nada, por lo que nuestra tabla es simétrica:

|Y\X|        0      |       1       |       2      |        3     |
|---|---------------|---------------|--------------|--------------|
|0  |$\frac{4}{81}$ |$\frac{10}{81}$|$\frac{8}{81}$|$\frac{2}{81}$|
|1  |$\frac{10}{81}$|$\frac{17}{81}$|              |              |
|2  |$\frac{8}{81}$ |               |              |              |
|3  |$\frac{2}{81}$ |               |              |              |


En los casos en los que un amigo reciba 3 cartas significa que todos le enviaron una a él y éste envió una a otra persona, por lo que los casos en que un amigo reciba 3 cartas y el otro 2 ó 3 son imposibles.

|Y\X|       0       |       1       |       2      |       3      |
|---|---------------|---------------|--------------|--------------|
|0  |$\frac{4}{81}$ |$\frac{10}{81}$|$\frac{8}{81}$|$\frac{2}{81}$|
|1  |$\frac{10}{81}$|$\frac{17}{81}$|              |              |
|2  |$\frac{8}{81}$ |               |              | 0            |
|3  |$\frac{2}{81}$ |               | 0            | 0            |


Preguntar esta parte

| Y\X | 0               | 1               | 2              | 3              |
| --- | --------------- | --------------- | -------------- | -------------- |
| 0   | $\frac{4}{81}$  | $\frac{10}{81}$ | $\frac{8}{81}$ | $\frac{2}{81}$ |
| 1   | $\frac{10}{81}$ | $\frac{17}{81}$ | $\frac{8}{81}$ | $\frac{1}{81}$ |
| 2   | $\frac{8}{81}$  | $\frac{8}{81}$  | $\frac{2}{81}$ | 0              |
| 3   | $\frac{2}{81}$  | $\frac{1}{81}$  | 0              | 0              |

a) Probabilidad Marginal de $Y$:

| $Y = y_i$  |       0       |       1       |       2       |       3      |
|----------|---------------|---------------|---------------|--------------|
|$P(Y = y_i)$|$\frac{24}{81}$|$\frac{36}{81}$|$\frac{18}{81}$|$\frac{3}{81}$|

Distribución Marginal de $Y$:

| $Y = y_i$  |       0       |       1       |       2       |       3      |
|------------|---------------|---------------|---------------|--------------|
|$F_Y(y)$    |$\frac{24}{81}$|$\frac{60}{81}$|$\frac{78}{81}$|      $1$     |

b) 

$$
E[X | Y = 1] = \sum_{i=0}^{3}x_i*P(X = x_i | Y = 1)
$$

$$
= \sum_{i=0}^{3} x_i * \frac{P(X = x_i, Y = 1)}{P(Y = 1)} = \frac{1}{P(Y = 1)}\sum_{i=0}^{3} x_i * P(X = x_i, Y = 1)
$$

$$
= \frac{1}{P(Y = 1)} \left( 0 * P (X = 0, Y = 1) + 1 * P(X = 1, Y = 1) + 2 * P(X = 2, Y = 1) + 3 * P(X = 3, Y = 1) \right)
$$

$$
= \frac{81}{36} * \left( 0 * \frac{10}{81} + 1 * \frac{17}{81} + 2 * \frac{8}{81} + 3 * \frac{1}{81} \right) = \boxed{1}
$$

c) 

$$
F_{X | Y > 0}(x) = P(X \leq x_j | Y > 0) = \sum_{i=0}^{j} \frac{P(X = x_i, Y > 0)}{P(Y > 0)} = \frac{1}{P(Y > 0)}\sum_{i=0}^{j}P(X = x_i, Y > 0)
$$

Ahora:

$$
P(Y > 0) = 1 - P(Y \leq 0) = 1 - \frac{24}{81} = \frac{57}{81}
$$


| $X = x_i$       |       0                             |       1                             |       2                             |       3      |
|-----------------|-------------------------------------|-------------------------------------|-------------------------------------|--------------|
|$F_{X\|Y>0}(x)$  |$\frac{\frac{20}{81}}{\frac{57}{81}}$|$\frac{\frac{46}{81}}{\frac{57}{81}}$|$\frac{\frac{56}{81}}{\frac{57}{81}}$|      $1$     |

d) Verifiquemos independencia:

$$
P(X = 3, Y = 2) \neq P(X = 3)P(Y = 2)
$$

$$
0 \neq \frac{3}{81} * \frac{18}{81}
$$

$\therefore$ No son independientes.

## Ejercicio 3:

Sea $(X,Y)$ un vector aleatorio discreto con función de probabilidad dada por:

|Y\X|       4                       |       6       |       8       |       10      |
|---|-------------------------------|---------------|---------------|---------------|
|0  | 0                             |       0.1     |      0.2      |      0.1      |
|1  | 0                             |       0       |      0        |      0.2      |
|2  | 0.2                           |       0.1     |      0        |       a       |

a) Halle el valor de $a$
b) Halle las funciones de probabilidad marginal para ambas variables. 
c) Halle la función de Distribución Conjunta.
d) Halle $V(Y)$. 
e) Halle $E[X|Y = 2]$.
f) Diga si $X$ e $Y$ son independientes.

### Solución:

a) Aplicando un razonamiento análogo a lo visto en el [Ejercicio 1](#solución) obtenemos que el valor de $a$ es $0.1$

b) Probabilidad Marginal de $X$ |----------------| Probabilidad Marginal de $Y$

| $X = x_i$    | 4   | 6   | 8   |   10   | $Y = y_i$  |  0   | 1   | 2   |
| ------------ | --- | --- | --- | ------ |     ---    | ---  | --- | --- |
| $P(X = x_i)$ | 0.2 | 0.2 | 0.2 |  0.4   |$P(Y = y_i)$| 0.4  | 0.2 | 0.4 | 

c) **Para hallar la Función de Distribución Conjunta recordemos que:**

$$
F_{(X,Y)}(x_n,y_k) = P(X \leq x_n, Y \leq y_k) = \sum_{i=1}^{n}\sum_{j=1}^{k}P(X = x_i, Y = y_j)
$$

> Esta expresión no es más que la suma de todos aquellos pares que cumplan que tanto su primera componente como la segunda sean menores o iguales que los que recibe la función como argumento

Utilizando la fórmula anterior comenzamos iterando por los valores de $Y$.

**Para $Y = 0$:**
- $X = 4:$

$$
F_{(X,Y)}(4,0) = P (X \leq 4, Y \leq 0) = 0
$$

- $X = 6:$

$$
F_{(X,Y)}(6,0) = P (X \leq 6, Y \leq 0) = P_{(X,Y)}(4,0) + P_{(X,Y)}(6,0) = 0.1
$$

> Aplicamos la idea planteada anteriormente: sumar las probabilidades de todos los pares (X,Y) tales que ambas componentes cumplieran al mismo tiempo ser menores o iguales que las componentes del par fijado.

- $X = 8:$

    $$
    F_{(X,Y)}(8,0) = P (X \leq 8, Y \leq 0) = P_{(X,Y)}(4,0) + P_{(X,Y)}(6,0) + P_{(X,Y)}(8,0) = 0.3
    $$

- $X = 10:$

Los pares $(X,Y)$ que cumplen $(X \leq 10, Y \leq 0)$ son $(4,0)$, $(6,0)$, $(8,0)$, $(10,0)$ y la suma de sus probabilidades es $0.4$

**Para Y = 1:**

- $X = 4$:

Los pares $(X,Y)$ que cumplen $(X \leq 4, Y \leq 1)$ son $(4,0)$, $(4,1)$ y la suma de sus probabilidades es $0$.

Omitamos algunos pasos y por cuestiones prácticas detengámonos por cuestiones prácticas en el caso:

$Y = 2, X = 8$.

Aquí los pares $(X,Y)$ que cumplen $(X \leq 8, Y \leq 2)$ son $(4,0)$, $(4,1)$, $(4,2)$, $(6,0)$, $(6,1)$, $(6,2)$, $(8,0)$, $(8,1)$, $(8,2)$, y la suma de sus probabilidades es $0.6$

**Continuando el procedimiento la tabla queda confeccionada de la siguiente forma:**

**Función de Distribución Conjunta**

|Y\X    | X < 4 | 4 | 6 | 8 | 10 |
|---    |-------|---|---|---|----|
|**Y<0**|   0   | 0 | 0 | 0 | 0  |
| **0** |   0   | 0 |0.1|0.3|0.4 |
| **1** |   0   | 0 |0.1|0.3|0.6 |
| **2** |   0   |0.2|0.4|0.6| 1  |


d) 

$$
V(Y) = E[Y^2] - (E[Y])^2
$$

$$
= \sum_{i=1}^{3} x_i^2 * P(Y = x_i) - \left( \sum_{i=1}^{3}x_i*P(Y = x_i) \right)^2
$$

$$
= 0^2 * 0.4 + 1^2 * 0.2 + 2^2 * 0.4 - (0 * 0.4 + 1 * 0.2 + 2 * 0.4)^2
$$

$$
= 1.8 - 1 = \boxed{0.8}
$$

e)

$$
E[X|Y = 2] = \sum_{i=1}^{4} x_i * P(X = x_i | Y = 2)
$$

$$
= \sum_{i=1}^{4} x_i * \frac{P(X = x_i, Y = 2)}{P(Y = 2)} = \frac{1}{P(Y = 2)} \sum_{i=1}^{4} P(X = x_i, Y = 2)
$$

$$
= \frac{1}{0.4} * (4 * 0.2 + 6 * 0.1 + 8 * 0 + 10 * 0.1) = \boxed{6}
$$


f) No son independientes:

$$
P(X = 4, Y = 1) \neq P(X = 4) P(Y = 1) 
$$

$$
0 \neq 0.04
$$

## Ejercicio 4:

Un experimento consiste en lanzar tres veces una moneda justa. Sea $X$ la variable aleatoria que representa el número de caras en las tres tiradas e Y la variable aleatoria que representa el valor absoluto de la diferencia entre el número de caras y escudos en las tres tiradas, determine:

a) La función de probabilidad conjunta del vector $(X,Y)$.
b) La media y desviación tı́pica de las distribuciones marginales de $X$ y $Y$ .
c) La covarianza y el coeficiente de correlación.

### Solución:


a) Observemos al acabar el experimento pueden suceder varios escenarios, estos son:

- Obtener 0 caras.
- Obtener 1 cara.
- Obtener 2 caras.
- Obtener 3 caras.

A cada suceso le asignaremos como valor $x_i$ el número asociado a la cantidad de caras obtenidas.
En dependencia de los resultados queda definida nuestra variable aleatoria $Y$.

- Para $0$ caras: $Y = | 0 - 3 | = 3$
- Para $1$ cara: $Y = | 1 - 2 | = 1$
- Para $2$ caras: $Y = | 2 - 1 | = 1$
- Para $3$ caras: $Y = | 3 - 0 | = 3$ 
  
De esta forma nuestro espacio muestral queda definido de la siguiente forma:

$$
\Omega = \set{(0,3), (1,1), (2,1), (3,3)}
$$

Notemos que cada tirada representa un experimento de Bernoulli, pues en cada una solo existen dos opciones éxito o fracaso y podemos decir además que cada uno es independiente.

Todo este análisis nos permite concluir que $X \sim Bin(n,p)$, pues realizamos $n = 3$ experimentos de Bernoulli independientes con probabilidad $p = \frac{1}{2}$, con queriendo conocer cuántos éxitos podemos obtener en cada uno.

Para determinar la probabilidad de obtener $k = 0,1,2,3$ aplicamos la función de probabilidad conocida para esta distribución:

$$
P(X = k) = \binom{n}{k}p^{n-k}(1-p)^k
$$

Para $k = 0$:

$$
P(X = 0) = \binom{3}{0}\frac{1}{2}^{3-0} \left(1-\frac{1}{2} \right)^0 = \frac{1}{8}
$$

Para $k = 1$:

$$
P(X = 1) = \binom{3}{1}\frac{1}{2}^{3-1} \left(1-\frac{1}{2} \right)^1 = \frac{3}{8}
$$

Para $k = 2$:

$$
P(X = 2) = \binom{3}{2}\frac{1}{2}^{3-2} \left(1-\frac{1}{2} \right)^2 = \frac{3}{8}
$$

Para $k = 3$:

$$
P(X = 3) = \binom{3}{3}\frac{1}{2}^{3-3} \left(1-\frac{1}{2} \right)^3 = \frac{1}{8}
$$

Por lo que la función de probabilidad conjunta queda determinada de la siguiente forma:

|Y\X|       0       |       1       |       2       |       3       |   
|---|---------------|---------------|---------------|---------------|
| 1 | 0             | $\frac{3}{8}$ | $\frac{3}{8}$ |       0       |
| 3 |$\frac{1}{8}$  |       0       |      0        | $\frac{1}{8}$ |


b) Función de Probabilidad Marginal de $X$:

| $X = x_i$     |       0       |       1       |       2       |       3       |   
|---------------|---------------|---------------|---------------|---------------|
| $P(X = x_i)$  | $\frac{1}{8}$ | $\frac{3}{8}$ | $\frac{3}{8}$ | $\frac{1}{8}$ |

Función de Probabilidad Marginal de $Y$:

| $Y = y_i$     |       1       |       3       |   
|---------------|---------------|---------------|
| $P(Y = y_i)$  | $\frac{6}{8}$ | $\frac{2}{8}$ |


**Varianza y Valor Esperado:**
Para $X$:

$$
V(X) = E[X^2] - (E[X])^2
$$

$$
E[X] = 0 * \frac{1}{8} + 1 * \frac{3}{8} + 2 * \frac{3}{8} + 3 * \frac{1}{8} = \boxed{\frac{12}{8}}
$$

$$
E[X^2] =0^2 * \frac{1}{8} + 1^2 * \frac{3}{8} + 2^2 * \frac{3}{8} + 3^2 * \frac{1}{8} = \boxed{\frac{24}{8}}
$$

$$
V(X) = \frac{24}{8} - \left( \frac{12}{8} \right)^2 = \frac{24}{8} - \frac{144}{64} = \boxed{\frac{48}{64}} 
$$

Para $Y$:
$$
V(Y) = E[Y^2] - (E[Y])^2
$$

$$
E[Y] = 1 * \frac{6}{8} + 3 * \frac{2}{8} = \boxed{\frac{12}{8}}
$$

$$
E[Y^2] = 1^2 * \frac{6}{8} + 3^2 * \frac{2}{8} = \boxed{\frac{24}{8}}
$$

$$
V(Y) = \frac{24}{8} - \left( \frac{12}{8} \right)^2 = \frac{24}{8} - \frac{144}{64} = \boxed{\frac{48}{64}}
$$

**Desviación Típica:**

$$
\sigma(X) = \sqrt{V(X)}  = \sqrt{\frac{48}{64}} = \frac{\sqrt{3}}{2} = \sigma(Y)
$$

**Covarianza:**

$$
Cov(X,Y) = E[XY] - E[X]E[Y]
$$

$$
E[XY] = 0 * 3 * \frac{1}{8} + 1*1*\frac{3}{8} + 2 * 1 * \frac{3}{8} + 3 * 3 * \frac{1}{8} = \frac{18}{8}
$$

$$
Cov(X,Y) = \frac{18}{8} - \frac{12}{8} * \frac{12}{8} = \frac{18}{8} - \frac{144}{64} = \boxed{0} 
$$

**Coeficiente de Correlación:**

$$
\rho = \frac{Cov(X,Y)}{\sqrt{V(X)V(Y)}} = 0
$$