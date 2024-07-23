 # Tema: Simulación de Variables Aleatorias Continuas

## Introducción

Como habíamos visto anteriormente en [Acerca de la Simulación de Variables Aleatorias](Acerca%20de%20la%20Simulación%20de%20Variables%20Aleatorias), existen varios métodos o algoritmos para realizar esta tarea, explicamos brevemente en qué consistían los algoritmos para simular **Variables Aleatorias Discretas** y dimos una serie de pasos a seguir para la simulación de **Variables Aleatorias Continuas**. Ahora profundizaremos un poco más en el marco teórico de este último tema.

## Método de la Transformada Inversa

Sean $U \sim U(0,1)$ y $F$ una función de distribución continua y estrictamente creciente, entonces la variable aleatoria:

$$
X = F^{-1}(U)
$$
tiene Función de Distribución $F$.

**Demostración:** Sea $F_X$ la función de distribución de $X = F^{-1}(U)$, entonces:

$$
F_X(x) = P(X \leq x)
$$
> Por definición de función de distribución

$$
= P(F^{-1}(U) \leq x)
$$
> Sustituimos $X$ por su equivalente $F^{-1}(U)$

$$
= P[F(F^{-1}(U) \leq F(x))]
$$
> Como $F$ es estrictamente creciente y continua si $x \leq y \implies F(x) \leq F(y)$

$$
= P(U \leq F(x)).
$$

> Como $F$ y $F^{-1}$ son mutuamente inversas, entonces $F(F^{-1}(U)) = U$

$\blacksquare$
### Simulación de una variable aleatoria con Distribución Exponencial

Sea $X \sim Exp(\lambda)$, su función de distribución es:
$$
F(x) = 
\begin{cases}
1-e^{-\lambda x}, \text{ } x > 0\\
0, \text{ } x \leq 0
\end{cases}
$$
Si $u = 1-e^{-\lambda x}$, hallemos su función inversa:
$$
u - 1 = -e^{-\lambda x} 
$$

$$
1 - u = e^{-\lambda x}
$$

$$
ln(1-u) = -\lambda x
$$

$$
x = - \frac{1}{\lambda}ln(1-u)
$$
Por lo que, para simular un valor de $X$ se puede usar la fórmula anterior.

#### Algoritmo:

```python
import random
import math

def simulate_exp(lambda_value):
	u = random.random()
	return -math.log(u,math.e) / lambda_value
```

## Método de los Rechazos

Muchas veces la función $f_X$ que estamos estudiando puede resultar bastante compleja y hallar la transformada inversa $F^{-1}_X$ puede resultar bastante tedioso.

Si quisiéramos simular una v.a $X$ con función de densidad $f$ y conocemos cómo simular $Y$ con función de densidad $g$. Como $f$ y $g$ son funciones de densidad, entonces sus gráficas se cortan porque sino el área bajo cada curva no pudiera ser 1.

**Demostración:** Supongamos que $\nexists x,y \in R: f(x) = g(y)$, entonces, sin pérdida de generalidad se cumple que $f(x) < g(y)$, por tanto, el área bajo la curva $g(x)$ será mayor que el área bajo la curva $f(x)$, pero por propiedad de la variable aleatoria continua sabemos que $\int_{-\infty}^{+\infty}f(x)dx = \int_{-\infty}^{+\infty}g(x)dx = 1$, lo cual es una contradicción.
$\therefore \exists x,y \in R: f(x) = g(y) \text{ } \blacksquare.$

Si hallamos un valor $c$ y una función $g(x)$ que nos permitan acotar $f(x)$:
$$
f(x) \leq cg(x), \text{ o sea, } \frac{f(x)}{g(x)} \leq c
$$
Entonces podríamos simular puntos del plano que estén bajo la curva $cg(x)$ y tomar los que se encuentren por debajo de $f(x)$.
### Algoritmo

1) Generar $Y \sim g$.
2) Generar $U\ \sim U(0,1)$.
3) Si $U \leq U(0,1)$ devolvemos $X = Y$.
4) En caso contrario volvemos al paso 1.

### Ejemplo

Simule una variable aleatoria $Z \sim N(0,1)$ utilizando el método de rechazos.

**Solución:** Como $Z \sim N(0,1)$, la función de densidad es la estándar, por tanto es par. Para simplificar el procedimiento hagamos la transformación $X = |Z|$.

Recordemos que la función de densidad de la Distribución Normal es:
$$
f_Z(z) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x - \mu)^2}{2}},
$$
pero como $\mu = 0$ y $\sigma = 1,$ entonces:
$$
f_Z(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}.
$$
Como $X = |Z|,$ hallemos $f_X(x)$:
$$
f_X(x) = f_Z(z) + f_Z(-z)
$$

$$
f_X(x) = 2f_Z(z)
$$

$$
f_X(x) = \frac{2}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}
$$
> Pues al ser $f_Z(z)$ par, $f_Z(z) = f_Z(-z)$, lo cual intuitivamente tiene sentido, pues si cada valor negativo se vuelve positivo, se duplica la posibilidad de obtener la probabilidad de obtener ese valor.

Usemos $g(x) = e^{-x}$ como función auxiliar, donde $g$ es la función de densidad de $Y \sim Exp(1)$.

Ahora hallemos el valor de $c$:
$$
h(x) = \frac{f(x)}{g(x)} = \frac{\frac{2}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}}{e^{-x}}
$$

$$
= \frac{2}{\sqrt{2\pi}}e^{-\frac{x^2}{2} + x}
$$
Primero hallemos el valor máximo que alcanza el exponente de $e$:

Derivamos:
$$
\frac{d}{dx}\left({-\frac{x^2}{2} + x}\right) = -x + 1
$$
Hallamos raíces:
$$
-x + 1 = 0, \text{ } x = 1
$$
Como la segunda derivada siempre es negativa, este valor es un máximo, por tanto:

$$
h(x) \leq h(1), \text{ } \forall x \in R
$$

$$
\frac{2}{\sqrt{2\pi}}e^{-\frac{x^2}{2} + x} \leq \frac{2}{\sqrt{2\pi}}e^{-\frac{1^2}{2} + 1} =  \frac{2}{\sqrt{2\pi}}e^{\frac{1}{2}} = \sqrt{\frac{2}{\pi}
}e^{\frac{1}{2}},
$$
o sea:

$$
\frac{2}{\sqrt{2\pi}}e^{-\frac{x^2}{2} + x} \leq \sqrt{\frac{2}{\pi}
}e^{\frac{1}{2}}, \text{ } \forall x.
$$

Por tanto, $c = \sqrt{\frac{2e}{\pi}}$, ahora redefinamos $h(x)$:

$$
h(x) = \frac{f(x)}{cg(x)} = \frac{\cancel{\frac{2}{\sqrt{2\pi}}}^1e^{-\frac{x^2}{2} + x}}{\cancel{\sqrt{\frac{2}{\pi}}^1
}e^{\frac{1}{2}}}
$$
> Los términos con raíces cuadradas son equivalentes, por eso podemos simplificarlos

$$
= \frac{e^{-\frac{x^2}{2}+x}}{e^{\frac{1}{2}}}
$$

$$
= e^{-\frac{x^2}{2} + x - \frac{1}{2}}
$$
$$
= e^{\frac{-x^2 + 2x - 1}{2}}
$$
$$
\boxed{= e^{-\frac{(x-1)^2}{2}}}
$$
Ahora que tenemos bien definida $h(x)$, solo queda proponer el algoritmo:

#### Algoritmo

1) Generar $Y \sim Exp(1)$.
2) Generar $X \sim U(0,1)$.
3) Si $X \leq e^{-\frac{(Y-1)^2}{2}}$ devolvemos $X = Y$ .
4) En caso contrario volvemos al paso 1.

**Código en Python**
```python
import random
import math
def simulate_normal():
	while True:
		x = random.random()
		y = random.expovariate(1)
		if x <= math.e**((-(y-1)**2)/2)
			return y
```