# Tema: Variable Aleatoria Discreta. Función de Probabilidad. Valor Esperado.

## Espacio Muestral
Conjunto de todos los resultados posibles de un experimento aleatorio. Por ejemplo, si lanzamos un dado, su espacio muestral $\Omega$ es:
$$\Omega = \{1,2,3,4,5,6\}$$

## Variable Aleatoria Discreta (v.a.d) 

**Definición 1:** Es una función que asigna un número real a cada resultado en el espacio muestral de un experimento aleatorio.

$$X:\Omega \rightarrow R $$
### Nota:
> **El espacio muestral $\Omega$ puede ser cualquiera, $X$ lo que hará es mapear cada resultado de $\omega \in \Omega$ para poderlo ''cuantificar''**

>**En experimentos cuyo conjunto de resultados es discreto, siempre puede tomarse como espacio muestral este conjunto, y como v.a $X$, la función identidad, es decir, $X(\omega) = \omega$.**

### Ejemplos:
- Si tomamos los 2 resultados a obtener al lanzar una moneda, nuestro espacio muestral sería:

    $\Omega = \{Cara, Escudo\}$ donde $X$ cuantificaría los resultados de la siguiente forma:

    $X(Cara) = 0$

    $X(Escudo) = 1$ 

    Es decir:
$$X = 
    \begin{cases}
    0, \text{ si es Cruz} \\
    1, \text{ si es Cara}
    \end{cases}\\
$$ 
- Si tomamos los 6 posibles resultados a obtener al lanzar un dado, nuestro espacio muestral ($\Omega$) sería:

$$\Omega = \{1,2,3,4,5,6\}$$

$$X
    \begin{cases}
    1, \text{ si sale la cara con 1}\\
    2, \text{ si sale la cara con 2}\\
    3, \text{ si sale la cara con 3}\\
    4, \text{ si sale la cara con 4}\\
    5, \text{ si sale la cara con 5}\\
    6, \text{ si sale la cara con 6}\\
    \end{cases}
$$



## Tipos de Variables Aleatorias

- **Discretas**: Toman un <u>conjunto finito o numerable de valores</u>.
- **Continuas**: Pueden tomar <u>cualquier valor dentro de un intervalo continuo</u>. 

## Definiciones

### Definición 2:
**Sea $X$ una v.a.d que toma valores $a_1,a_2,...,$ se define su Función de Probabilidad o  Función de Masa de Probabilidad como:**
$$P_X(a_i) = P(X = a_i) \text{, }$$
**para $i=1,2$**

**Notemos que**

$$\sum_{i=1}^{\infty}{P_x(a_i)} = \sum_{i=1}^{\infty}{P(X=a_i)} = 1.$$ 

**para cualquier v.a.d y la demostración se obtiene de los [Axiomas de Kolmogorov](Axiomas%20de%20Kolmogorov.md).**

#### Ejemplo 1:
Si $X$ indica la ocurrencia del suceso <u>sale cara</u> al lanzar una moneda y se sabe que la probabilidad de que salga cara es $\frac{1}{4}$, entonces, ¿cuál es la función de probabilidad de $X$?

##### Respuesta:
$\Omega = \{Cara, Escudo\}$

$$X= 
    \begin{cases}
    0, \text{ si es Cruz} \\
    1, \text{ si es Cara}
    \end{cases}
$$

$$P(X)=
    \begin{cases}
    \frac{3}{4}, \text{ si X = 0}\\
    \frac{1}{4}, \text{ si X = 1}
    \end{cases}
$$

ó alternativamente:

$\\P_X(X=0) = \frac{3}{4}$

$P_X(X= 1) = \frac{1}{4}$

### Definición 3: 

**Sea $X$ una v.a.d, se define su Función de Distribución:**

$$
F_X(x) = P(X \leq x) = \sum_{x_i \leq x} P(X = x_i).
$$

#### Nota
> La función de distribución nos da la probabilidad de que $X$ tome valores menores o iguales que el $x$ fijado.

#### Ejemplo 2: 
En el [Ejemplo 1](#ejemplo-1), se obtiene que la función de distribución es la siguiente:

Para $x < 0$ tendremos que $F_X(x) = 0$, pues no existen valores en $\Omega$ menores que 0.

Para $0 \leq x < 1$:

Como los eventos son <u>discretos</u> y en este intervalo solo se puede tomar el valor 0, $$F_X(x) = \sum_{i \leq 0} P(X = i) = P(X = 0) = \frac{3}{4}$$

Nuevamente, como los eventos son <u>discretos</u>, para cualquier valor de x mayor o igual que 1, $F_X(x)$ incluye ambas probabilidades, $P(X = 0)$ y $P(X=1)$, por lo que:
$$
F_X(x) = P(X = 0) + P(X=1) = 1
$$
Notemos que tiene sentido, pues la suma de todas las probabilidades del espacio muestral por [Definición 2](#definición-2) es 1.

Finalmente la función de distribución $F_X(x)$ queda determinada de la siguiente forma:
$$
F(x) = \begin{cases}
        0, \text{ si } x < 0\\
        \frac{3}{4}, \text{ si } 0 \leq x < 1\\
        1, \text{ si } x \geq 1
       \end{cases}
$$

### Definición 4 (Bernoulli):
**Sea $p \in (0,1)$, se dice que $X$ tiene distribución de Bernoulli con
parámetro $p$ y se denota $X \sim Ber(p)$ si su función de probabilidad es:**
$$
P(X)=\begin{cases}
1-p, \text{ si } X = 0\\
p, \text{ si } X = 1
\end{cases}
$$
> - Esta v.a se usa para indicar la ocurrencia de un suceso de interés, un éxito en el experimento, por ejemplo: <u>sale cara al lanzar una moneda</u>.
> - Se dice que un experimento es de Bernoulli si los posibles resultados son éxito o fracaso.**

### Definición 5 (Binomial):
**Sean $p \in (0,1)$ y $n \in N$, se dice que $X$ tiene Distribución Binomial con parámetros $n$ y $p$, y se denota $X \sim Bin(n,p)$ si:**
$$P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$$
para $k = 0,1,2,...,n$.

> - La v.a binomial <u>representa la cantidad de éxitos obtenidos en</u> $n$ <u>experimentos de Bernoulli independientes</u>.
> - Si se define $X_i \sim Ber(p)$ independientes, entonces: $X = X_1 + X_2 + ... + X_n$

### Definición 4 (Geométrica):

**Sea $p \in (0,1)$, se dice que $X$ tiene Distribución Geométrica con parámetro $p$ y se denota $X \sim Geo(p)$ si:**

$$
P(X = k) = p(1-p)^{k-1}
$$

**para $k = 1,2,...$**

> - En este enfoque se asume que se realizan infinitas pruebas de Bernoulli independientes y que $X$ <u>representa el número del experimento en el que por primera vez se obutvo éxito</u>.

### Definición 5 (Binomial Negativa):
**Sean $p \in (0,1)$ y $r \in N$, se dice que $X$ tiene Distribución Binomial Negativa con parámetros $r$ y $p$, y se denota $X \sim BN(r,p)$ si:**
$$
P(X = k) = \binom{k - 1}{r - 1}p^r(1-p)^{k-r}
$$

para $k = r, r+1, r+2, ...$

> - La v.a $X$ <u>representa el número del experimento en el que se obtuvo por primera vez el r-ésimo éxito</u>.
> - $X$ se puede representar como la suma de $r$ v.a Geométricas independientes.

### Definición 8 (Poisson):
**Sea $\lambda > 0$, se dice que  $X$ tiene distribución Poisson con parámetro $\lambda$ y lo denotamos por $X \sim Poisson(\lambda)$ si:**

$$
P(X = k) = \frac{\lambda^ke^{-\lambda}}{k!},
$$

> Un ejemplo común en la literatura es que el número de clientes que llegan a un servidor
durante un tiempo determinado tiene distribución de Poisson.

**para** $k = 0,1,2,...$

## Valor Esperado o Esperanza Matemática:

**Sea $X$ una v.a.d que toma valores $a_1,a_2,...,$ entonces el valor esperado o esperanza matemática de $X$ se denota por $EX$ y es:**
$$
EX = \sum_{i=1}^{\infty}{a_iP(X = a_i)},
$$
**si esta serie converge absolutamente.**

**Si denotáramos $P(X = ai)$, entonces:**
$$
EX = \sum_{i=1}^{\infty}a_ip_i
$$

> - El valor esperado es un promedio ponderado  de los valores de la v.a de acuerdo al peso que le da la función de probabilidad a estos valores.$\\$
> - Intuitivamente lo que se plantea es que para una gran cantidad de experimentos realizados, la media aritmética de los valores observados de la v.a se aproxima a su valor esperado.


### Nota
> La siguiente [Observación](#observación) y la posterior [Proposición 1](#proposición%201) fueron tomadas del libro y comienzan en la página 165.
### Observación:
Intuitivamente podríamos decir que el valor esperado de una variable aleatoria podría obtenerse como la suma ponderada de $X(s)$ multiplicado por la probabilidad de esos $s$, $\forall s \in S$. Donde $S$ es el conjunto de todos los sucesos, es decir, nuestro espacio muestral, de ahí surge la siguiente proposición.
### Proposición 1
Sea $X$ una <u>variable aleatoria</u>,  el valor de $E[X] = \sum_{s \in S}X(s)p(s)$

**Demostración:**
Supongamos que los distintos valores de $X$ son $x_i$, $i \geq 1$. Para cada $i$, sea $S_i$ el evento para el cual $X$ es igual a $x_i$, es decir

$S_i = \{s: X(s) = x_i\}$

> - En palabras más humanas, $S_i$ es un subconjunto del espacio muestral, en el cual se cumple que para todo elemento que pertenezca a él, su resultado al aplicarle la función $X$ es $x_i$
> - Si tomamos como S el conjunto de los posibles valores a obtener al lanzar un dado:$\\$
>
>   $S = \{1,2,3,4,5,6\}$, donde: $\\$
> $S_1 = \{1\}, \\ S_2 = \{2\}, \\.\\.\\.  \\ S_6 = \{6\}$ $\\$ 
> Observemos que $X(S_1 = \{1\}) = 1$ y así para cada $i$. 
> En este ejemplo particular $|S_i| = 1$, pero podría darse el caso de que ésta sea mayor. 

**Ahora:**

$$
\begin{equation}
    E[X] = \sum_{i}x_iP(X=x_i),
\end{equation}
$$

$$
\begin{equation}
    =\sum_{i}x_i P(S_i)
\end{equation}
$$

> $P(X = x_i) = P(S_i)$ por como está definido $S_i$


$$
\begin{equation}
    =\sum_{i}x_i\sum_{s \in S_i}p(s),
\end{equation}
$$

> pues $P(S_i)$ es la suma de las probabilidades de todos los eventos $s \in S_i$

$$
\begin{equation}
    =\sum_{i}\sum_{s \in S_i}x_ip(s)
\end{equation}
$$

> aplicamos distributividad de $x_i$ con respecto a $\sum_{s \in S_i}p(s)$

$$
\begin{equation}
    =\sum_{i}\sum_{s \in S_i}X(s)p(s)
\end{equation}
$$

> recordemos que $x_i = X(s)$

$$
\begin{equation}
    =\sum_{s \in S}X(s)p(s)
\end{equation}
$$

> La equivalencia del paso anterior con el actual se da porque $\sum_{i}\sum_{s \in S_i}$ indica implícitamente iterar por todo el conjunto $S$.

$\blacksquare$ 

### Corolario (Linealidad del Valor Esperado)

**Sean $X_1,X_2,...,X_n$ variables aleatorias, $E[\sum_{i=1}^{n}\alpha_iX_i] = \alpha_1E[X_1] + \alpha_2E[X_2] + ... + \alpha_nE[X_n]$**

**Demostración:**

Sea $Z = \alpha_1 X_1 + \alpha_2 X_2 + ... + \alpha_n X_n$ = $\sum_{i=1}^{n}\alpha_i X_i$,

entonces: 
$$
\begin{equation}
    E[Z] = \sum_{s \in S}Z(s)p(s),
\end{equation}
$$
> Por la [Proposición](#proposición-1) anterior
$$
\begin{equation}
    = \sum_{s \in S}(\alpha_1 X_1(s) + \alpha_2 X_2(s) + ... + \alpha_n X_n(s))p(s),
\end{equation}
$$

> Sustituyendo $Z$

$$
\begin{equation}
    = \sum_{s \in S}\alpha_1 X_1(s)p(s) + \alpha_2 X_2(s)p(s) + ... + \alpha_n X_n(s)p(s),
\end{equation}
$$

> Distribuimos $p(s)$

$$
\begin{equation}
    = \sum_{s \in S}\alpha_1 X_1(s)p(s) + \sum_{s \in S}\alpha_2 X_2(s)p(s) + ... + \sum_{s \in S}\alpha_n X_n(s)p(s),
\end{equation}
$$

> Separamos en sumas independientes

$$
\begin{equation}
    = \alpha_1\sum_{s \in S} X_1(s)p(s) + \alpha_2\sum_{s \in S} X_2(s)p(s) + ... + \alpha_n\sum_{s \in S} X_n(s)p(s),
\end{equation}
$$

> Extraemos como factor común cada $\alpha_i$

$$
\begin{equation}
    = \alpha_1E[X_1] + \alpha_2E[X_2] + ... + \alpha_n\ E[X_n],
\end{equation}
$$

> Por la [Proposición](#proposición-1) anterior.

$\blacksquare$

### Proposición 2

**Sea $a$ un valor constante, entonces:**

$$
E[a] = a
$$
**Demostración:**

Sea X una v.a que siempre toma el valor constante $a$, entonces P(X = a) = 1, por tanto:
$$
E[X] = a \times P(X = a) = a \times 1 = a. \text{ } \blacksquare
$$

### Independencia de Variables Aleatorias:

**Dos variables aleatorias $X$ e $Y$ independientes cumplen que: 

$$
P(X = x_i, Y = y_j) = P(X = x_i)P(Y = y_j), \text{ } \forall i,j
$$
**Nota:**

> $P(X = x_i, Y = y_j)$ es la probabilidad conjunta de que $X = x_i$ e $Y = y_i$.

#### Proposición 3:

**Sean $X$ e $Y$ dos variables aleatorias independientes, entonces:

$$
E[X+Y] = E[X] + E[Y]
$$
**Demostración:**


Ahora:
$$
E[X + Y] = \sum_{x,y} (x + y) P(X = x, Y = y)
$$
$$
= \sum_{x,y} xP(X=x,Y=y) + yP(X=x,Y=y)
$$
> Aplicamos distributiva
$$
= \sum_{x,y} xP(X=x,Y=y) + \sum_{x,y} yP(X=x,Y=y)
$$
> Si la serie converge absolutamente podemos separar la sumatoria 

$$
= \underbrace{\sum_{x} xP(X = x)\sum_y P(Y=y)}_1 + \underbrace{\sum_{y} yP(Y= y_i)\sum_xP(X= x)}_2
$$
> Para el sumando $1$ iteraremos primero por $y$ y luego por $x$ y para el sumando $2$ iteraremos por $x$ y luego por $y$.

$$
= \sum_x xP(X=x) + \sum yP(Y = y)
$$
> Tengamos en cuenta que el reordenamiento anterior nos permite aplicar la propiedad $\sum_i P_i = 1$, por lo que $\sum_y P(Y = y) = 1$ e ídem para $x$.

$$
= E[X] + E[Y]. \text { } \blacksquare
$$
#### Proposición 4

**Sean $X$ e $Y$ dos variables aleatorias independientes, entonces:**

$$
E[XY] = E[X]E[Y]
$$
**Demostración:**

$$
E[XY] = \sum_{x,y}xyP(X=x,Y=y)
$$

$$
= \sum_{x,y}xyP(X = x)P(Y = y)
$$
> Por independencia de las variables aleatorias

$$
= \sum_{x,y}xP(X=x)yP(Y=y)
$$
> Primero iteraremos por $y$ y luego por $x$

$$
= \sum_{x}xP(X=x)\sum_{y}yP(Y=y)
$$

$$
= E[X]E[Y]. \text{ } \blacksquare
$$



## Valores Esperados de las Diferentes Distribuciones

### Valor Esperado de la Distribución de Bernoulli:
Sea $X \sim Ber(p)$, entonces:
$$
E[X] = p
$$

**Demostración:**
$$
E[X] = 0\times(1-p) + 1\times p = p
$$

$\blacksquare$

### Valor Esperado de la Distribución Binomial:

Sea $X \sim Bin(n,p)$ y se definen las variables aleatorias $X_i \sim Ber(p)$ independientes, $i=1,2,...,n$, tal que $X = X_1 + X_2 + ... + X_n$, entonces:

$$
E[X] = np
$$

**Demostración:**
$$
E[X] = E[X_1 + X_2 + ... + X_n] = E[X_1] + E[X_2] + ... + E[X_n]
$$

> por [linealidad del valor esperado](#corolario-linealidad-del-valor-esperado)

$$
= \underbrace{\cancel{E[X_1]}^{p} + \cancel{E[X_2]}^{p} + ... + \cancel{E[X_n]}^{p}}_{\text{n veces}} = np
$$

> cada $E[X_i]$ es el valor esperado de una distribución de Bernoulli, cuyo valor es $p$ y se está sumando $n$ veces. 

$\blacksquare$

### Valor Esperado de la Distribución Geométrica:
Sea $X \sim Geo(p)$, $p \in (0,1)$, entonces:

$$
E[X] = \frac{1}{p} 
$$

**Demostración:**

$$
E[X] = \sum_{k=1}^{\infty}kp(1-p)^{k-1}
\text{, }(1)$$

$$
= p\sum_{k=1}^{\infty}k(1-p)^{k-1} \text{ }(2)
$$

> sacamos $p$ factor común

**Ahora recordemos del Análisis Mátematico que:**

$$
\sum_{k=0}^{\infty}(1-p)^k = \lim_{k\rightarrow+\infty} \frac{1 - (1-p)^{k+1}}{1-(1-p)} \text{, }(3)
$$

> pero como $|p| < 1$ en el infinito $(1-p)^{k+1}$ tiende a $0$

$$
\lim_{k\rightarrow+\infty} \frac{1 - \cancel{(1-p)^{k+1}}^0}{1-(1-p)} = \frac{1}{p} \text{, }(4)
$$

**Además, observemos que:**

$$
\frac{d(\sum_{k=0}^{\infty}(1-p)^k)}{dp} = -\sum_{k=0}^{\infty}k(1-p)^{k-1} \text{, }(5)
$$

$$
\frac{d(\frac{1}{p})}{dp} = -\sum_{k=0}^{\infty}k(1-p)^{k-1} \text{, }(6)
$$

$$
 -\frac{1}{p^2} = -\sum_{k=0}^{\infty}k(1-p)^{k-1} \text{ }(7)
$$

> multiplicando $(7)$ por $-1$ en obtenemos:

$$
\frac{1}{p^2} = \sum_{k=0}^{\infty}k(1-p)^{k-1} \text{ }(8)
$$

**Sustituyendo $(8)$ en $(2)$:**

$$
p\sum_{k=1}^{\infty}k(1-p)^{k-1} = p * \frac{1}{p^2} = \frac{1}{p}. \text{ }(9)
$$

$\blacksquare$