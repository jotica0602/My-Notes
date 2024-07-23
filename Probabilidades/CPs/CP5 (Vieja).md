Alejandro Echevarría Brunet.

# CP\#5: Variable Aleatoria Discreta

## Ejercicios de Programación

### Ejercicio 1:

Implemente un algoritmo para simular una variable aleatoria con la distribución indicada:

a) $X \sim Bin(n,p)$

b) $X \sim Geo(p)$

#### Solución:

a) De la conferencia [[Variable Aleatoria Discreta 2#Simulación de Variables Aleatorias Discretas]] tenemos que para simular una v.a.d el criterio general es:

1) Generar $U \sim U(0,1)$
2) Devolver $x_j$ si: 

$$\sum_{i=1}^{j-1}P(X = x_i) < U \leq \sum_{i=1}^{j} P(X = x_i)$$ 

b) Para simular variables aleatorias geométricas podemos utilizar una fórmula cerrada que se obtiene apoyándonos en el criterio de la Transformada Inversa tratado superficialmente en [[Acerca de la Simulación de Variables Aleatorias#Método de la Transformada Inversa]].

Primeramente hallemos $F_X(x)$ para $X \sim Geo(p)$:

$$
F_X(x_j) = P(X \leq x_j) = \sum_{i=1}^{j}P(X = x_i) = \sum_{i=1}^{j} p(1-p)^{xi-1} = p \sum_{i=1}^{j} (1-p)^{xi-1}
$$

$$
= p \times \frac{1-(1-p)^{x_i}}{1-(1-p)}
$$

> Notemos que estamos en presencia de una suma geométrica, por lo que podemos calcular su valor

$$
= p \times \frac{1-(1-p)^{x_i}}{\cancel{1}-\cancel{1}+p}
$$

$$
= \cancel{p}^1 \times \frac{1-(1-p)^{x_i}}{\cancel{p}^1}
$$

$$
= \boxed{1 - (1-p)^{x_i}}
$$

Ahora hallemos la inversa de $F_X(x)$. Sea $U = F_X(x)$:

$$
U = 1-(1-p)^{x_i}
$$

$$
U-1 = -(1-p)^{x_i}
$$

$$
1 - U = (1-p)^{x_i}
$$

$$
\log{(1 - U)} = \log{(1-p)^{x_i}}
$$

$$
\log{(1 - U)} = x_i\log{(1-p)}
$$

$$
\frac{\log{(1 - U)}}{\log{(1-p)}} = x_i
$$

$$
\boxed{\left\lceil \frac{\log{(1 - U)}}{\log{(1-p)}} \right\rceil = x_i}
$$

> El cálculo logarítmico podría resultar en números no enteros y $X$ es una variable aleatoria discreta, por lo que necesitamos encontrar el entero $x_i$ más pequeño que satisfaga la igualdad, para ello usamos la función techo

```python
import numpy as np
import math

# Simular X ~ Bin(n,p)
def simulate_binom(n,p):
	cummulative = 0
	u = np.random.uniform(0,1)
	for k in range(n+1):
		cummulative += math.comb(n,k) * p**(n-k) * (1-p)**k
		if u <= cummulative:
		return k

# Simular X ~ Geo(p)
def simulate_geo(p):
    u = np.random.uniform(0,1)
    x = int(np.ceil(np.log(1 - u) / np.log(1 - p)))
    return x
```

## Ejercicios Prácticos:

### Ejercicio 2:
Un jugador tiene una probabilidad de $0.5$ de ganar una determinada partida cada vez. Analice qué es más probable: ganar $3$ partidas de $4$, $3$ de $5$ ó $3$ de $8$.

#### Solución:

Dividamos el problema en partes más pequeñas:

Tenemos una probabilidad $p$ de ganar una partida. Cada partida tiene dos posibilidades **victoria** o **derrota**, por lo que podemos considerar cada partida como un experimento de **Bernoulli**. Queremos saber de un número $n$ de partidas cuál es la probabilidad de ganar $k$ de ellas, por lo que $X \sim Bin(n,p)$.

**Probabilidad de Ganar 3 de 4:**

$$
\binom{4}{3}\left(\frac{1}{2}\right)\left(1-\frac{1}{2}\right)^3 = \frac{1}{4}
$$

**Probabilidad de Ganar 3 de 5:**

$$
\binom{5}{3}\left(\frac{1}{2}\right)^2 \left(1-\frac{1}{2}\right)^3 = \frac{10}{32}
$$

**Probabilidad de Ganar 3 de 8:**
$$
\binom{8}{3}\left(\frac{1}{2}\right)^5\left(1-\frac{1}{2}\right)^3 = \frac{56}{256}
$$

$\therefore$ Es más probable ganar 3 partidas de 5.

### Ejercicio 3:
Una compañía aseguradora paga por día de hospitalización $\$100$, durante los tres primeros días y $\$50$ los siguientes. Considerando que los días de hospitalización $X$ es una variable aleatoria discreta con función de probabilidad:

$$
P(X = k)
\begin{cases}
\frac{6 - k}{15}, \text{ para } k = 1,2,3,4,5 \\
0, \text{ en otro caso.}
\end{cases}
$$

Determine el valor esperado de pago por hospitalización por parte de la compañía.

#### Solución:

El hecho de que se pague por día una cantidad $n$ de dinero significa que se le está aplicando una función $f$ a nuestra variable aleatoria, donde 

$$
f(X) = 
\begin{cases}
100, \text{ si } X = 1 \\
100 + f(X-1), \text{ si } 2 \leq X \leq 3 \\
50 + f(X-1), \text{ si } X > 3	
\end{cases}
$$

$$
E[f(X)] = \sum_{i=1}^{k}f(X=x_i)P(X = x_i) = 100 \times \frac{5}{15} + 200 \times \frac{4}{15} + 300 \times \frac{3}{15} + 350 \times \frac{2}{15} + 400 \times \frac{1}{15} = \$220
$$

### Ejercicio 4:
Considere el siguiente juego donde a una persona se le proponen dos preguntas para responder. La pregunta **A** puede ser respondida correctamente con probabilidad $0.8$, y en en tal caso la persona obtendría un premio de $\$100$ mientras que la pregunta **B** tiene una probabilidad de $0.5$ de ser respondida correctamente y un premio de $\$200$. Si la persona responde correctamente la primera pregunta seleccionada gana el premio correspondiente y tiene derecho a responder la segunda pregunta. Diga cuál pregunta debe responder la persona primero para maximizar la ganancia esperada.

#### Solución:

Analicemos nuestros datos:
Tenemos dos preguntas **A** y **B** con probabilidades $p_1 = 0.8$ y $p_2 = 0.5$ de ser respondidas respectivamente. En ambos casos solo pueden ocurrir dos sucesos, responder correcta o incorrectamente la pregunta, los cuales además son independientes.

Nuestro problema consiste en determinar cuál pregunta deberíamos responder primero y cuál después para maximizar la ganancia obtenida.

Sea $X$ la variable aleatoria que define que hallamos elegido responder primero la pregunta **A** y luego la **B**, entonces:
$$
X =
\begin{cases}
	x_1: \text{Responder incorrectamente la pregunta A},\\ 
	x_2: \text{Responder correctamente la pregunta A e incorrectamente la pregunta B}, \\
	x_3: \text{Responder correctamente ambas preguntas.} 
\end{cases}
$$

Además, nos definen la función:

$$
f(X) = 
\begin{cases}
0, \text{ si }X = x_1 \\
100, \text{ si }X = x_2 \\
300, \text { si } X = x_3
\end{cases}
$$

Hallemos el valor esperado de $X$:
$$
E[f(X)] = \sum_{i=1}^{3} f(x_i) P(X = x_i)
$$

$$
= f(x_1) \times P(X = x_1) + f(x_2) \times P(X = x_2) + f(x_3) \times P(X = x_3)
$$

$$
= 0 \times 0.2 + 100 \times 0.8 \times 0.5 + 300 \times 0.8 \times 0.5 
$$

$$ 
= 160
$$

Sea $Y$ la variable aleatoria que define que hallamos elegido responder primero la pregunta **B** y luego la **A**, entonces:
$$
Y =
\begin{cases}
	y_1: \text{Responder incorrectamente la pregunta B},\\ 
	y_2: \text{Responder correctamente la pregunta B e incorrectamente la pregunta A}, \\
	y_3: \text{Responder correctamente ambas preguntas.} 
\end{cases}
$$

Además, nos definen la función:

$$
g(Y) = 
\begin{cases}
0, \text{ si } Y = y_1 \\
100, \text{ si } Y = y_2 \\
300, \text { si } Y = y_3
\end{cases}
$$

Hallemos el valor esperado de $Y$:
$$
E[g(Y)] = \sum_{i=1}^{3} g(y_i) P(Y = y_i)
$$

$$
= g(y_1) \times P(Y = y_1) + g(y_2) \times P(Y = y_2) + g(y_3) \times P(Y = y_3)
$$

$$
= 0 \times 0.5 + 200 \times 0.5 \times 0.2 + 300 \times 0.8 \times 0.5 
$$

$$ 
= 140
$$

Como podemos observar $E[X] > E[Y]$, por lo que para maximizar la ganancia deberíamos comenzar respondiendo la pregunta **A**.

## Ejercicios Teóricos:

### Ejercicio 5:

Halle la varianza de una v.a $X \sim Poisson(\lambda)$.

#### Solución:

$$
V(X) = E[X^2] - (E[X])^2
$$

$$
= \sum_{k=1}^{\infty} k^2 P(X = k) - \left(\cancel{\sum_{k=1}^{\infty} k P(X = k)}^\lambda \right) ^ 2
$$

$$
= \sum_{k=1}^{\infty} k^2 P(X = k) - \lambda^2
$$

> Pues en la [clase práctica](CP4%20(Vieja).md#ejercicio-7:) anterior demostramos que si $X \sim Poisson(\lambda) \implies E[X] = \lambda$. 

Trabajemos con el sumando izquierdo:

$$
\sum_{k=1}^{\infty} k^2 P(X = k) = \sum_{k=1}^{\infty} k^2 \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum_{k=1}^{\infty} k^2 \frac{\lambda^k}{k!} 
$$

> Extraemos $e^{-\lambda}$ como factor común de la sumatoria

$$
e^{-\lambda} \sum_{k=1}^{\infty} k^2 \frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=1}^{\infty} k \times k \frac{\lambda^k}{k \times (k-1)!}  
$$

> $k^2 = k \times k$ y $k! = k \times (k-1)!$, por lo que podemos simplificar términos 

$$
= e^{-\lambda} \sum_{k=1}^{\infty} k \frac{\lambda^k}{(k-1)!} = e^{-\lambda} \sum_{k=1}^{\infty} (k-1+1) \frac{\lambda^k}{(k-1)!}
$$

> Reescribimos $k$ como $(k-1+1)$

$$
e^{-\lambda} \left( \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} \right)
$$

> Separamos la sumatoria en dos sumatorias

$$
= e^{-\lambda} \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!}
$$

> Distribuimos $e^{-\lambda}$ con respecto a la suma

$$
= e^{-\lambda} \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1} \lambda }{(k-1)!}
$$

> En la sumatoria de la derecha tenemos que $ \lambda^k = \lambda^{k-1} \lambda$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + e^{-\lambda} \lambda \cancel{\sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}}^{e^{\lambda}}
$$

> Extraemos $\lambda$ como factor común y nuevamente tenemos que la sumatoria de la derecha es igual a $e^{\lambda}$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + e^{-\lambda} \lambda e^{\lambda}
$$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} (k-1) \frac{\lambda^k}{(k-1)!} + \lambda
$$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} \cancel{(k-1)}^1 \frac{\lambda^k}{\cancel{(k-1)}^1(k-2)!} + \lambda
$$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-2)!} + \lambda
$$

$$
= e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-2}\lambda^2}{(k-2)!} + \lambda
$$

$$
= e^{-\lambda} \lambda^2 \cancel{\sum_{k=1}^{\infty} \frac{\lambda^{k-2}}{(k-2)!}}^{e^{\lambda}} + \lambda
$$

> El procedimiento hasta aquí es análogo a los anteriores

$$
= e^{-\lambda} \lambda^2 e^{\lambda} + \lambda = \lambda^2 + \lambda
$$

Volviendo a la ecuación principal:

$$
\lambda^2 + \lambda - \lambda^2 = \lambda. \text{ } \blacksquare 
$$

### Ejercicio 6 (Ausencia de Memoria):

Sea $X$ una v.a con distribución geométrica, pruebe que:

$$
P(X - n = k | X > n) = P(X = k), \text{ } k = 1,2,\dots
$$

#### Solución:

$$
P(X-n = k | X > n) = P(X = k + n | X > n)
$$

$$
P(X = k + n | X > n) = \frac{P(X = k + n \cap X > n)}{P(X>n)}
$$

$$
= \frac{P(X = k + n)}{P(X > n)}
$$

> - Por definición de v.a.d geométrica, los valores de su dominio son enteros positivos, por tanto $k,n \in \mathbb{Z}^+$, por lo que si $X = n + k$ y $X > n \implies (X = k + n \cap X > n) = (X = k + n)$.
> - Para $P(X > n)$ podemos encontrar también una expresión:
> $$ P(X > n) = 1 - P(X \leq n) = 1 - \sum_{i=1}^{n} p(1-p)^{i-1}
$$
>
> $$ = 1 - p \sum_{i=1}^{n} (1 - p)^{i-1} = 1 - \left( p \times \frac{1-(1-p)^n}{1-(1-p)} \right) = 1 - \left( p \times \frac{1 - (1 - p)^n}{p} \right)$$ 
> - Recordemos que podemos aplicar la fórmula para sumas geométricas finitas.
> 
> $$
= 1 - \left( 1-(1-p)^n \right).
$$
> 
> $$
= \boxed{(1-p)^n}
$$

$$
= \frac{p(1-p)^{k+n-1}}{(1-p)^n}
$$

$$
= p(1-p)^{k-1} = P(X = k). \blacksquare 
$$

### Ejercicio 7:

Sea $X$ una variable aleatoria que toma valores no negativos, pruebe que:

$$
E[X] = \sum_{i=1}^{\infty} P(X \geq i)
$$

#### Solución:

$$
\sum_{i=1}^{\infty}P(X \geq i)
$$

> Muchas veces solo debemos observar qué ocurre con los datos que tenemos.

$$
= P(X \geq 1) + P(X \geq 2) + \dots + P(X \geq j) + \dots
$$

> En este caso podemos notar que para cada valor $P(X \geq i)$, éste contendrá valores en su propia sumatoria que a su vez pertenecen a la sumatoria de $P(X = i+1)$. 

$$
= (P(X = 1) + P(X = 2) + ...) + (P(X = 2) + P(X = 3) + \dots ) + \dots + (P(X = j) + P(X = j + 1) + \dots)
$$

$$
P(X = 1) + 2P(X=2) + 3P(X=3) + \dots + jP(X = j) + \dots
$$

> Por lo que si abrimos las sumas y agrupamos llegamos a la ya conocida expresión.

$$
= \sum_{i=1}^{\infty} i P(X = i) = E[X]
$$