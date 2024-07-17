# Tema: Vectores Aleatorios Continuos

## Vector Aleatorio Continuo
### Definición 1

El vector $X  = (X_1,X_2,...,X_n)$ es un vector **aleatorio continuo si $X_i$ es una variable aleatoria** continua con $i = 1,2,...,n$ y su **Función de Distribución Conjunta** se puede escribir de la siguiente forma:

$$
F(x_1,x_2,...,x_n) = P(X_1 \leq x1,X_2 \leq x2,...,X_n \leq xn) = \int_{-\infty}^{x_1}\int_{-\infty}^{x_2}...\int_{-\infty}^{x_n}f(x)dt_ndt_{n-1}...dt_1
$$
Donde la función $f(t_1,t_2,...,t_n)$ es **una función no negativa llamada función de densidad conjunta**.

Solo estudiaremos los vectores aleatorios del tipo $(X,Y)$, cuya función de distribución conjunta se puede escribir para la forma de **vectores aleatorios de dos dimensiones:**

$$
F_{(X,Y)}(x,y) = P(X \leq x, Y \leq y) = \int_{-\infty}^y\int_{-\infty}^{x}f(u,v)dudv
$$

### Propiedades de los Vectores Aleatorios

Sea $(X,Y)$ un vector aleatorio con $F_{(X,Y)}$ función de distribución conjunta se cumplen las siguientes propiedades:

1) $F_{(X,Y)}$ es no decreciente en cada una de las variables.
2) $F_{(X,Y)}$ continua por la derecha en cada variable
3) $f(x,y) = \frac{\partial^2}{\partial x \partial y}F_{(X,Y)}(x,y)$ 
4)  Límites al infinito: 
$$
F_{(X,Y)}(-\infty,y) = lim_{x \to -\infty}F_{(X,Y)}(x,y) = 0$$
$$
F_{(X,Y)}(x,-\infty) = lim_{y \to -\infty}F_{(X,Y)}(x,y) = 0$$
$$
F_{(X,Y)}(+\infty,+\infty) = \lim_\limits{x \to +\infty, \text{ }y \to +\infty}F_{(X,Y)}(x,y) = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)dxdy = 1$$
5) $P(a < X \leq b, c < Y \leq d) = F_{(X,Y)}(b,d) - F_{(X,Y)}(a,d) - F_{(X,Y)}(b,c) + F_{(X,Y)}(a,c)$
6) $P(X = x, Y = y) = 0$
7) Probabilidad sobre un conjunto B:
	$$\iint_\limits{(x,y) \in B} f(x,y)dxdy $$
#### Ejemplo 1

Sea $(X,Y)$ un vector aleatorio con función de densidad conjunta:

$$
f(x,y) = 
\begin{cases}
2e^{-x}e^{-2y}, \text{ } x > 0,\text{ }y> 0 \\
0, \text{ en otro caso.}
\end{cases}
$$
Halle $P(X > 1, Y < 1)$ y $P(X < Y)$.

**Hallando $P(X>1,Y<1)$:**
$$
P(X > 1, Y < 1) = \iint_\limits{(X>1, Y<1)} f(x,y)dxdy
$$

$$
= \int_{1}^{+\infty}\int_{0}^{1} 2e^{-x}e^{-2y} dydx = \int_{1}^{+\infty}e^{-x}\left(\int_{0}^{1}2e^{-2y}dy\right)dx
$$

$$
= \int_{1}^{+\infty}-e^{-x}\Big(e^{-2y}\Big|_{0}^{1}\Big)dx = \int_{1}^{+\infty}e^{-x}\left(1 -e^{-2} \right) dx
$$

$$
= \left(1-e^{-2}\right)\int_{1}^{+\infty}e^{-x}dx =-\left(1-e^{-2}\right)\left(\cancel{\lim_\limits{x \to +\infty}e^{-x}}^0-e^{-1} \right)
$$

$$
= \boxed{(1-e^{-2})e^{-1}}.
$$
**Hallando $P(X<Y)$:**
$$
P(X<Y) = \int_\limits{0}^{+\infty}\int_\limits{0}^yf(x,y)dxdy
$$

$$
= \int_\limits{0}^{+\infty}\int_\limits{0}^y 2e^{-x}e^{-2y} dxdy = \int_\limits{0}^{+\infty} 2e^{-2y}\left(\int_\limits{0}^y e^{-x}dx\right)dy
$$

$$
= \int_\limits{0}^{+\infty} 2e^{-2y}\left(\int_\limits{0}^y e^{-x}dx\right)dy = \int_\limits{0}^{+\infty} 2e^{-2y}\left(-e^{-x}\Big|_0^y \right)dy = \int_\limits{0}^{+\infty} 2e^{-2y}\left( 1 - e^{-y}\right) dy  
$$

$$
= \int_\limits{0}^{+\infty}2e^{-2y} -2e^{-3y}dy = \int_\limits{0}^{+\infty}2e^{-2y}dy - \int_\limits{0}^{+\infty}2e^{-3y}dy 
$$

$$
= -\int_\limits{0}^{+\infty}-2e^{-2y}dy + \frac{2}{3}\int_\limits{0}^{+\infty}-3e^{-3y}dy = -\left(e^{-2y}\Big|_0^{+\infty}\right) + \frac{2}{3} \left(e^{-3y}\Big|_0^{+\infty}\right)
$$
$$
= -\left( \cancel{\lim_\limits{x \to +\infty}e^{-2y}}^0 - e^{-2\times0} \right) + \frac{2}{3} \left(\cancel{\lim_\limits{x \to +\infty}e^{-3y}}^0 - e^{-3 \times 0} \right) = 1 - \frac{2}{3}
$$

$$
= \boxed{\frac{1}{3}}.
$$

### Definición 2 (Función de Densidad Marginal)

Sea $(X,Y)$ un vector aleatorio con
función de densidad conjunta $f(x, y)$, entonces las funciones de densidades marginales se
obtienen a partir de las siguientes expresiones:

$$
f_X(x) = \int_{-\infty}^{+\infty}f(x,y)dy
$$
$$
f_Y(y) = \int_{-\infty}^{+\infty}f(x,y)dx
$$
### Definición 3 (Función de Distribución Marginal)

Sea $(X,Y)$ un vector aleatorio con función de densidad conjunta $f(x,y)$, entonces la funciones de distribución marginal para cada componente se obtienen a partir de las siguientes expresiones:

$$
F_X(x) = \lim_\limits{y\to+\infty}F(x,y) = F_{(X,Y)}(x,+\infty) = \int_{-\infty}^{x}\int_{-\infty}^{+\infty}f(u,y)dydu
$$
$$
F_Y(y) = \lim_\limits{x\to+\infty}F(x,y) = F_{(X,Y)}(+\infty,y) = \int_{-\infty}^{y}\int_{-\infty}^{+\infty}f(x,v)dxdv
$$

### Definición 4

Sea $(X,Y)$ vector aleatorio con función de densidad conjunta $f(x,y)$ y función de distribución conjunta $F(x,y)$, se dice que $X$ e $Y$ son independientes si y solo si:

$$
F_{(X,Y)}(x,y) = F_X(x)F_Y(y), \text{ } \forall x,y \in \mathbb{R}
$$
O de forma equivalente, si y solo si:

$$
f_{(X,Y)}(x,y) = f_X(x)f_Y(y), \text{ } \forall x,y \in \mathbb{R}
$$
### Definición 5 (Valor Esperado)

Sea un vector aleatorio $(X,Y)$ se define:

$$
E[g(X,Y)] = \iint_\limits{\mathbb{R}^2}g(x,y)f(x,y)dxdy
$$
### Definición 6 (Covarianza)

Sea un vector aleatorio $(X,Y)$ se define la covarianza como:

$$
Cov(X,Y) = E[(X,Y)] - E[X]E[Y]
$$

### Definición 7 (Correlación)

Sea un vector aleatorio $(X,Y)$ se define la correlación como:

$$
\rho_{(X,Y)} = \frac{Cov(X,Y)}{\sqrt{V(X)V(Y)}}
$$

### Definición 8 (Distribución Condicional)

Sea $(X,Y)$ vector aleatorio definido en $(\Omega^2, \mathcal{F}, P)$ espacio de probabilidad, sea $f(x,y)$ densidad conjunta y $f_Y$ la función de densidad marginal de $Y$. Sea $Y \in \Omega: f_Y(y) \neq 0$. Entonces la distribución condicional de $X$ dado $Y = y$ es:

$$
F_{(X|Y=y)}(x) = P(X \leq x | Y = y) = \int_\limits{-\infty}^x f(u|y)du, \text{ } \forall x \in \mathbb{R},
$$

donde $f(x|y) = \frac{f(x,y)}{f_Y(y)}.$ 