# Tema: Variable Aleatoria Discreta. Simulación. Varianza.

## Simulación de Variables Aleatorias Discretas

En el algoritmo general para simular variables aleatorias discretas se propone generar $U$ al azar en el intervalo $(0,1)$ y devolveremos:

$$
X = \begin{cases}
x_1, \text{ si } U \leq P_1 \\
x_2, \text{ si } U \leq P_1 + P_2 \\
. \\
. \\
. \\
x_j, \text{ si } \sum_{i}^{j-1} P_i < U \leq \sum_{i}^{j}P_i\\
. \\
. \\
. \\
\end{cases}
$$

Para el caso en el que $X \sim Geo(p)$ se puede calcular una expresión exacta para las sumas, pues:
$$
\sum_{i=1}^{j-1}P_i = \sum_{i=1}^{j-1}P(X = x_i) 
$$
$$
= P(X \leq j-1)
$$
> Recordemos que justamente esto es lo que plantea la **Función de Distribución**.

$$
= 1 - P(X > j-1)
$$
> Por axioma de Kolmogorov. Notemos que $(X > j - 1)$ representa que en los $j-1$ primeros experimentos no haya ocurrido ningún éxito.

$$
= 1 - (1-p)^{j-1}
$$
Ahora, para encontrar el valor de $j$ usando $U$ :
$$
X = min \{j:(1-p)^j \leq U\} 
$$

$$
= min(j: j \text{ }(1-p) \leq lnU)
$$
$$
= min\{j : j \geq \frac{ln(U)}{ln(1-p)}\}
$$
$$
= [\frac{ln(U)}{ln(1-p)}] + 1
$$
## Varianza:

### Proposición 1:

**Sea $X$ una v.a.d que toma valores $a_1,a_2,...,an,...$ y $f$ una función real, entonces:**
$$
E[f(X)] = \sum_{i=1}^\infty f(a_i)P(X = a_i)
$$
**si la serie converge absolutamente.**

**Demostración:** Definamos una variable aleatoria $Y = f(X)$. Esto significa que $f(x_i) = y_i, \forall i$, en otras palabras, cada posible valor que pueda tomar la variable aleatoria $Y$ sería el resultado de pasar por la función $f$ un valor de la variable aleatoria $X$.
Podría darse el caso que para la función $f$ definida existieran valores $x_i,x_j$ con $i \neq j$ tales que $f(x_i) = f(x_j) = y_k$, es decir, que la función $f$ no fuera inyectiva. Para estos casos tendremos que $P(Y=y_j) = \sum_{x_i:f(x_i)=y_j}$ , o sea, la probabilidad de ese $y_j$ sería la sumatoria de todas las probabilidades de aquellos valores  $x_i$ tales que $f(x_i) = y_j$, como bien se indica.

Quedando claro todo esto es sencillo plantear que:
$$
E[f(X)] = \sum_if(x_i)P(X=x_i)
$$
$$
E[f(X)] = \sum_j \sum_i f(x_i)P(X = x_i)
$$
$$
= \sum_{j} \sum_{x_i:f(x_i)=y_j}f(x_i)P(X=x_i)
$$
> Agrupamos los casos en los que $f(x_i)=y_i$ que es de lo que se encarga la sumatoria más interna. 

$$
= \sum_{j} \sum_{x_i:f(x_i)=y_j}y_iP(X=x_i)
$$
> Sustituimos por $y_i$

$$
= \sum_{j} y_j\sum_{x_i:f(x_i)=y_j}P(X=x_i)
$$
> Extraemos $y_i$ como factor común

$$
= \sum_{j} y_j P(Y=y_j) = E[Y]. \text{ } \blacksquare
$$
> Sustituimos $\sum_{x_i:f(x_i)=y_j}$ por $P(Y=y_j)$ 



El concepto de valor esperado proporciona una medida de tendencia central de la v.a estudiada, sin embargo no es suficiente información para muchos estudios. La varianza es un concepto relacionado a la dispersión que presentan los valores que toma la v.a respecto al valor esperado.

### Definición 1: 

Sea $X$ una v.a tal que $E[X] = \mu < \infty$, definimos varianza de $X$ y se denota $V(X)$ a la expresión:

$$
V(X) = E[(X-\mu)^2]
$$
$$
= E[X^2] - \mu^2
$$

**<u>Demostración</u>:**
$$
E[(X-\mu)^2] = E[X^2 - 2X\mu + \mu^2]
$$
> Expandimos la expresión

$$
= E[X^2] - E[2X\mu] + E[\mu^2]
$$
> Por linealidad del Valor Esperado

$$
= E[X^2] -2\mu E[X] + E[\mu^2]
$$
> Recordemos que $E[X] = \mu$

$$
= E[X^2] -2\mu^2 + \mu^2
$$
$$
= E[X^2] - \mu^2.\text{ } \blacksquare
$$

### Proposición 2:

 **Sean $X$ una v.a con $E[X] <  \infty$ y $a,b \in R$, entonces:**

$$
V(aX + b) = a^2V(X)
$$
**Demostración**

Sea $\mu = E[X]$, entonces: 

$$
E[aX+b] = aE[X] + b
$$
$$
= \underline{a\mu + b}
$$

Ahora:
$$
V(aX + b) = E[(aX + b - E[aX + b])^2]
$$

$$
= E[(aX + b - (a\mu + b))^2]
$$
> Sustituyendo la igualdad obtenida

$$
= E[(aX+ \cancel{b} - a\mu - \cancel{b})^2]
$$

$$
= E[(aX - a\mu)^2]
$$

$$
= E[(a(X-\mu))^2]
$$
> Extraemos $a$ como factor común

$$
= E[a^2 (X - \mu)^2]
$$

$$
= a^2E[(X-\mu)^2]
$$
> Linealidad del Valor Esperado

$$
= a^2 V(X)

$$
### Proposición 3:

**Sean $X$ e $Y$ v.a independientes y con valores esperados finitos, entonces:**

$$
V(X+Y) = V(X) + V(Y)
$$
**<u>Demostración</u>**

Sean $\mu_1 = E[X], \mu_2 = E[Y]$, entonces: 

$$
V(X + Y) = E[(X + Y - E[X + Y])^2]
$$
$$
= E[(X + Y - (E[X] + E[Y]))^2]
$$
> Por linealidad del Valor Esperado

$$
= E[(X+Y-(\mu_1 + \mu_2))^2]
$$

> Sustituimos $E[X]$ y $E[Y]$ por $\mu_1$ y $\mu_2$ respectivamente

$$
= E[((X - \mu_1) + (Y - \mu_2))^2]
$$
> Agrpamos términos convenientemente

$$
= E[(X - \mu_1)^2 + 2(X - \mu_1)(Y - \mu_2) + (Y - \mu_2)^2]
$$

> Expandimos el cuadrado

$$
= E[(X-\mu_1)^2] + 2E[(X - \mu_1)(Y - \mu_2)] + E[(Y - \mu_2)^2]
$$

> Por linealidad del Valor Esperado

$$
= E[(X-\mu_1)^2] + 2E[X-\mu_1] E[Y-\mu_2] + E[(Y-\mu_2)^2]
$$
> Por independencia de las variables aleatorias $X$ e $Y$ 

$$
= E[(X-\mu_1)^2] + 2\cancel{E[X-\mu_1]}^0 \cancel{E[Y-\mu_2]}^0 + E[(Y-\mu_2)^2]
$$

> Notemos que $E[Z- E[Z]]$ = $E[Z] - E[E[Z]] = E[Z] - E[Z] = 0$

$$
= E[(X-\mu_1)^2] + E[(Y-\mu_2)^2]
$$

$$
= V(X) + V(Y). \text{ } \blacksquare 
$$
## Desviación Estándar o Típica

Sea X una v.a tal que $E[X] < \infty$, esta se denota por $\sigma$ y se define por:

$$
\sigma(X) = \sqrt{V(X)}
$$
> Este concepto puede interpretarse como la distancia promedio a la que se encuentran los valores de la v.a respecto al valor esperado.

## Varianza de las diferentes DIstribuciones

### Bernoulli

Sea $X \sim Ber(p)$, entonces:

$$
V(X) = p(1-p)
$$
**<u>Demostración</u>**

Anteriormente se demostró que $E[X] = p$, si $X \sim Ber(p)$, por tanto:  

$$V(X) = E[X^2] - (E[X])^2 = p - p^2 = p(1-p)$$

### Binomial

Sea $X \sim Bin(n,p)$, entonces:

$$
V(X) = np(1-p)
$$
**<u>Demostración</u>**

Se definen las v.a $X_i \sim Ber(p)$, $i=1,...,n$ independientes tal que $X = X_1 + X_2 + ... + X_n$ tenemos que:

$$
V(X) = V(X_1 + X_2 + ... + X_n)  
$$

$$
= V(X_1) + V(X_2) + ... + V(X_n)
$$

> Por la [Proposición 3](#proposición-3).

 $$
 = \underbrace{p(1-p) + p(1-p) + ... + p(1-p)}_\text{n veces}
 $$
 > Pues cada $X_i \sim Ber(p)$, con $1 \leq i \leq n$ y ya vimos que $V(X \sim Ber(p)) = p(1-p)$ 
 
 $$
 = np(1-p). \text { } \blacksquare
 $$

### Geométrica

Sea $X \sim Geo(p)$, entonces:

$$
V(X) = \frac{1-p}{p^2}
$$

**<u>Demostración</u>** 

Anteriormente se demostró que $E[X] = \frac{1}{p}$, por lo que:

$$
\begin{equation}
V(X) = E[X^2] - (E[X])^2 = E[X^2] - \frac{1}{p}
\end{equation}
$$
Ahora determinemos el valor de $E[X^2]$:

$$
\begin{equation}
E[X^2] = \sum_{k=1}^\infty k^2p(1-p)^{k-1}
\end{equation}
$$

$$
\begin{equation}
= p \sum_{k=1}^\infty k^2(1-p)^{k-1} 
\end{equation}
$$
> Extraemos $p$ como factor común de la sumatoria

$$
\begin{equation}
= p \sum_{k=1}^\infty k(k + 1 - 1)(1-p)^{k-1}
\end{equation}
$$
> $k(k+1-1) = k$

$$
\begin{equation}
= p
\left[ 
	\sum_{k=1}^\infty k(k+1)(1-p)^{k-1} - \sum_{k=1}^\infty k(1-p)^{k-1} 
\right]
\end{equation}
$$

> Separamos la sumatoria en dos 

$$
\begin{equation}
= p
\left[ 
	\sum_{k=1}^\infty k(k+1)(1-p)^{k-1} - \cancel{\sum_{k=1}^\infty k(1-p)^{k-1}}^\frac{1}{p^2} 
\right]
\end{equation}
$$
> El valor del segundo sumando ya lo habíamos calculado anteriormente

Ahora:

$$
\begin{equation}
\frac{d^2(\left[ \sum_{k=-1}^\infty (1-p)^{k+1} \right])}{dp^2} = \sum_{k=1}^\infty (k+1)k(1-p)^{k-1}
\end{equation}
$$

Donde

$$
\begin{equation}
\sum_{k=-1}^\infty (1-p)^{k+1} = \frac{1}{1-(1-p)} = \frac{1}{p}
\end{equation}
$$

Por tanto

$$
\begin{equation}
\frac{d^2(\left[ \sum_{k=-1}^\infty (1-p)^{k+1} \right])}{dp^2} = \frac{d^2(\frac{1}{p})}{dp^2} = \frac{2}{p^3}
\end{equation}
$$

Sustituyendo en $(6)$

$$
\begin{equation}
= p
\left( \frac{2}{p^3} - \frac{1}{p^2} \right)
\end{equation}
$$

$$
\begin{equation}
= \frac{1-p}{p^2}. \text{ } \blacksquare
\end{equation}
$$