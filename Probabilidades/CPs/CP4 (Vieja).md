## Ejercicios de Programación
### Ejercicio 1: (ver [Notas de Simulación de Variables Aleatorias](../Notas%20de%20Conferencia/Acerca%20de%20la%20Simulación%20de%20Variables%20Aleatorias))

Desarrolle un algoritmo eficiente para simular una v.a X con función de probabilidad:

| x          | 1    | 2    | 3    | 4    |
| ---------- | ---- | ---- | ---- | ---- |
| $P(X=x_i)$ | 0.15 | 0.20 | 0.35 | 0.30 |

```python
import random
def simulate(x:list[int], px:list[int]) -> int:
	u = random.random()
	sum = 0
	for i in range(len(x)):
		sum += px[i]
		if u < sum:
			return px[i]
		
```


## Ejercicios Prácticos:

### Ejercicio 3:

Una moneda es lanzada tres veces. Considere la variable aleatoria definida como el número de caras obtenidas en los tres lanzamientos. Determine:
- a) Las funciones de probabilidad y de distribución. 
- b) El valor esperado.

a) Suponiendo que la moneda sea justa (las probabilidades de obtener cara serían $1/2$) y que se quiere determinar la cantidad de caras o **éxitos** obtenidos en $3$ experimentos independientes de Bernoulli, pues los posibles resultados de cada lanzamiento serían **éxito** o **fracaso**, podemos decir que nuestra variable aleatoria $X$ tiene una Distribución Binomial (ver las notas de la conferencia [Variable Aleatoria Discreta 1](../Notas%20de%20Conferencia/Variable%20Aleatoria%20Discreta%201.md)), o sea $X \sim Bin(n,p)$, donde $n = 3$, $p = \frac{1}{2}$.

De aquí los resultados posibles serían:
- Ninguna Cara de 3 lanzamientos ($k=0$).
- Una Cara de 3 lanzamientos ($k=1$).
- Dos Caras de 3 lanzamientos ($k=2$).
- Tres Caras de 3 lanzamientos ($k=3$).

Recordemos que si $X \sim Bin(n,p)$, su función de probabilidad la podemos obtener ploteando los distintos valores de $k$ y el correspondiente valor de $n$ en la fórmula:
$$
P(X = k) = \binom{n}{k}p^{n-k}(1-p)^k
$$
Para $k = 0$:
$$
\binom{3}{0}\frac{1}{2}^{3-0}(1-\frac{1}{2})^0 = \frac{1}{8} 
$$
Para $k = 1$:
$$
\binom{3}{1}\frac{1}{2}^{3-1}(1-\frac{1}{2})^1 = \frac{3}{4} \times \frac{1}{2} = \frac{3}{8} 
$$
Para $k = 2$:
$$
\binom{3}{2}\frac{1}{2}^{3-2}(1-\frac{1}{2})^2 = \frac{3}{2} \times \frac{1}{4} = \frac{3}{8} 
$$
Para $k = 3$:
$$
\binom{3}{3}\frac{1}{2}^{3-3}(1-\frac{1}{2})^3 = \frac{1}{8} 
$$

Para calcular la Función de Distribución es muy sencillo. Recordemos que:
$$
F_X(x) = P(X\leq x) = \sum_{x_i \leq x}P(x_i)
$$
Ahora:

Para $x = 0$:
$$
F_X(x) = P(X \leq 0) = P(0) = \frac{1}{8}
$$
Para $x = 1$:
$$
F_X(x) = P(X \leq 1) = P(0) + P(1) = \frac{1}{8} + \frac{3}{8}  = \frac{4}{8}
$$
Para $x = 2$:
$$
F_X(x) = P(X \leq 2) = P(0) + P(1) + P(2) = \frac{1}{8} + \frac{3}{8} + \frac{3}{8}= \frac{7}{8}
$$
Para $x = 3$:
$$
F_X(x) = P(X \leq 3) = P(0) + P(1) + P(2) = \frac{1}{8} + \frac{3}{8} + \frac{3}{8} + \frac{1}{8}= 1
$$
b) Recordemos que el valor esperado se obtiene de la siguiente forma:
$$
E[X] = \sum_{i=1}^{\infty}x_iP(X=x_i) 
$$
Para nuestro caso $X = \{0,1,2,3\}$, por tanto:
$$
E[X] = 0 \times P(0) + 1 \times P(1) + 2 \times P(2) + 3 \times P(3)
$$
$$
= 0 \times \frac{1}{8} + 1 \times \frac{3}{8} + 2 \times \frac{3}{8} + 3 \times \frac{1}{8} = \frac{12}{8}
$$
### Ejercicio 4:

Suponga que 2 equipos juegan una serie de partidas **hasta que uno obtiene $i$ victorias**.
Se asume que el equipo A gana una partida con probabilidad $p$ e independientemente
de los juegos anteriores. Determine el valor esperado del número de juegos realizados
si:

- a) $i = 2$
- b) $i = 3$

2.1 - Demuestre que en ambos casos el valor esperado se maximiza cuando $p=\frac{1}{2}$.

Para calcular ambos valores esperados primeramente debemos hallar las probabilidades de obtener el resultado deseado (**obtener por primera vez $i$ victorias** por un equipo o el otro) en un determinado número de partidas. Para ello podemos hacer uso de la Distribución Binomial Negativa:
$$
P(X = k) = \underbrace{\binom{k-1}{r-1}p^r(1-p)^{k-r}}_{\text{Equipo A}} + \underbrace{\binom{k-1}{r-1}(1-p)^rp^{k-r}}_{\text{Equipo B}} 
$$
Donde $k$ es el número de intentos y $r$, el número de victorias (éxitos deseados).

Para a) $r = i = 2$:
$$
P(X = k) = \underbrace{\binom{k-1}{2-1}p^2(1-p)^{k-2}}_{\text{Equipo A}} + \underbrace{\binom{k-1}{2-1}(1-p)^2p^{k-2}}_{\text{Equipo B}} 
$$
Para b) $r=i=3$:
$$
P(X = k) = \underbrace{\binom{k-1}{3-1}p^3(1-p)^{k-3}}_{\text{Equipo A}} + \underbrace{\binom{k-1}{3-1}(1-p)^3p^{k-3}}_{\text{Equipo B}} 
$$

Antes de darle solución al problema, hagamos un análisis su naturaleza:

> Para que un equipo pueda ganar $i=2$ partidos de una serie de partidos jugados, deben jugarse mínimo $k = 2$ partidos (pues para $k=1$ partidos, la probabilidad de que un equipo u otro gane es $0$) y máximo $k=3$ partidos, considerando la posibilidad de empate. 

Por tanto:

$$
	E[X] = \sum_{i=2}^{3}x_iP(X=x_i) 
$$
$$
= 2 \times P(X=2) + 3 \times P(X=3)
$$

$$
= 2 \times (\binom{2-1}{2-1}p^2(1-p)^{2-2} + \binom{2-1}{2-1}(1-p)^2p^{2-2}) +3 \times (\binom{3-1}{2-1}p^2(1-p)^{3-2} + \binom{3-1}{2-1}(1-p)^2p^{3-2})
$$
$$
= 2 \times (\binom{1}{1}p^2(1-p)^{0} + \binom{1}{1}(1-p)^2p^{0}) +3 \times (\binom{2}{1}p^2(1-p)^{1} + \binom{2}{1}(1-p)^2p^{1})
$$

$$
= 2 \times (p^2 + (1-p)^2) +3 \times (2p^2(1-p) + 2p(1-p)^2)
$$
$$
= 2p^2 + 2(1-p)^2 + 6p^2(1-p) + 6p(1-p)^2
$$
$$
= 2p^2 + 2(1-2p+p^2) + 6p^2-6p^3+6p(1-2p+p^2)
$$
$$
= 2p^2 + 2 - 4p + 2p^2 + 6p^2 - 6p^3 + 6p -12p^2 + 6p^3
$$
$$
 = -2p^2 + 2p + 2 
$$
Analicemos el planteamiento **2.1**:
$$
\frac{d(E[X])}{dp} = -4p + 2
$$

$$
-4p + 2 = 0 \implies p = \frac{1}{2}
$$
Analicemos si p es un máximo:
$$
\frac{(d^2(E[X]))}{d^2p} = -4
$$


$\therefore p = \frac{1}{2}$ es un máximo. $\blacksquare$ 

Para el caso del inciso b) el análisis es idéntico, solamente debemos tener en cuenta que para $k=\{1,2\}$ las probabilidades de ganar $3$ juegos serían $0$, por lo que nuestras referencias serían $k=\{3,4,5\}$ juegos.

## Ejercicios Teóricos:
### Ejercicio 5:

Compruebe que $\sum pi = 1$  si $p_i = P (X = a_i)$, donde $a_i$ son los valores admisibles
para cada una de las distribuciones siguientes:

- a) $X \sim Bin(n,p)$
- b) $X \sim Geo(p)$
- c) $X \sim Poisson(\lambda)$

a) Si $X \sim Bin(n,p)$ tendremos que:

$$
\sum_{k=1}^{\infty}P(X=a_k) = \sum_{k=0}^{n}\binom{n}{k}p^{n-k}(1-p)^k
$$
que esto no es más que el desarrollo del binomio de Newton, es decir:
$$
(p+(1-p))^n = \sum_{k=0}^{n}\binom{n}{k}p^{n-k}(1-p)^k
$$
De donde:
$$
(p+(1-p))^n = 1^n = 1. 
$$

$\blacksquare$

b) Si $X \sim Geo(p)$ tendremos que:

$$
\sum_{i=1}^{\infty}P(X=a_i) = \sum_{i=1}^{\infty}p(1-p)^{i-1} 
$$

$$
= p \sum_{i=1}^{\infty}(1-p)^{i-1}
$$

$$
= p \times \frac{1}{1-(1-p)} = p \times \frac{1}{p} = 1.
$$
> Usamos la fórmula para calcular el resultado de una serie geométrica teniendo que $|p| < 1$

$\blacksquare$

c) Si $X \sim Poisson(\lambda)$ tendremos que:

$$
\sum_{i=1}^{\infty}P(X = a_i) = \sum_{i=1}^{\infty}\frac{\lambda^i e^{-\lambda}}{i!}
$$

$$
= e^{-\lambda} \sum_{i=1}^{\infty}\frac{\lambda^i}{i!} 
$$
> Recordemos que $\sum_{n=1}^{\infty} \frac{x^n}{n!} = e^{x}$ 
$$
= e^{-\lambda} e^{\lambda} = 1.
$$

$\blacksquare$

### Ejercicio 7:

Si $X \sim Poisson(\lambda)$, demuestre que $E[X] = \lambda$.

**Solución:**
$$
E[X] = \sum_{i=1}^{\infty}a_iP(X=a_i) = \sum_{i=1}^{\infty}i\frac{\lambda^ ie^{-\lambda}}{i!} 
$$

$$
= e^{-\lambda}\sum_{i=1}^{\infty}\cancel{i}\frac{\lambda^ i}{\cancel{i}(i-1)!}
$$
> Extraemos  $e^{-\lambda}$ como factor común y reescribimos $i!$ como $i(i-1)!$ 
$$
= e^{-\lambda}\sum_{i=1}^{\infty}\frac{\lambda^{i-1}\lambda}{(i-1)!}
$$
> Reescribimos $\lambda^i$ como $\lambda^{i-1} \lambda$ 
$$
= \lambda e^{-\lambda}\sum_{i=1}^{\infty}\frac{\lambda^{i-1}}{(i-1)!}
$$
> Extraemos $\lambda$ como factor común de la sumatoria
$$
= \lambda e^{-\lambda} e^{\lambda} = \lambda.
$$
> Aplicamos la propiedad utilizada en el ejercicio anterior.

$\blacksquare$

