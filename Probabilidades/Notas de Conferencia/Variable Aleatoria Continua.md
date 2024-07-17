# Temas: Variable aleatoria continua. Función de Distribución. Valor Esperado y Varianza. Funciones de variable aleatoria.

## Variable Aleatoria Continua

Las variables aleatorias continuas son otro modo de cuantificar los resultados de los experimentos aleatorios, solo que en este caso los valores que toman estas variables se encuentran en un intervalo.

### Definición 1

**Sea $X: \Omega \rightarrow R$ una función que toma valores en un intervalo, se dice que X es una variable aleatoria continua si su Función de Distribución se puede representar como:** 

$$
F(x) = P(X \leq x) = \int_{-\infty}^x f(t)dt.
$$
**A la función $f$ se le denomina Función de Densidad o Densidad de Probabilidad (PDF) e identifica a la variable aleatoria (Ver [PMF y PDF](PMF%20y%20PDF))**

#### Nota
> Recordemos que en las variables aleatorias discretas, su función de distribución se definía como:
> $$
F(x) = P(X \leq x) = \sum_{i=1}^{\infty} P(X = x) $$
> De ahí que se plantee la definición de arriba, puesto que $X$ ahora toma valores continuos y la sumatoria se convierta en una integral.

### Propiedades de la Variable Aleatoria Continua

1)  $f(t) \geq 0, t \in R$.
2) $f(t) = \frac{dF}{dt}(t)$.
3) $\lim_{t \to \infty} F(t) = \int_{-\infty}^{+\infty} f(t)dt = 1$.
4) $P(X = x) = 0, x \in R$.
5) $F$ es una función continua.
6) $P(X \in B) = \int_B f(t) dt$, donde $B = (a,b]$. De lo cual se deduce que: 

$$
P(a < X \leq b) = F(b) - F(a) = \int_a^b f(t)dt.
$$
#### Nota
> De la Propiedad 6 notemos que como 
> $$F(b) = P(X \leq b) \text{ y }$$
> 
> $$F(a) = P(X \leq a),$$
> por definición de Función de Distribución, entonces:
> $$F(b) - F(a) = P(X \leq b) - P(X \leq a)$$ 

#### Ejemplo 1

Sea $X$ una variaible aleatoria con función de densidad (PDF):
$$
f(x) = 
\begin{cases}
1/2, \text { si } 1 \leq x < a \\
2, \text { si } a \leq x \leq 2 \\
0, \text { en otro caso}
\end{cases}
$$

Donde $a$ es una constante tal que $1 < a < 2$.

a) Determine el valor de a.


$$
\int_1^2 f(t)dt = 1
$$

> Por Propiedad $3$

$$
\int_1^a f(t)dt + \int_a^2f(t)dt = 1
$$

> Dividimos el intervalo

$$
\int_a^1 \frac{1}{2} dt + \int_a^2 2dt = 1
$$

$$
\frac{1}{2}t \Bigg|_1^a + 2t\Bigg|_a^2 = 1
$$

$$
\frac{1}{2} a - \frac{1}{2} + 4 - 2a = 1
$$

$$
a = \frac{5}{3}.
$$

b) Calcule $P(\frac{1}{3} < X < \frac{7}{4})$.

$$
P(\frac{1}{3} < X < \frac{7}{4}) = \int_{\frac{1}{3}}^{\frac{7}{4}} f(t) dt
$$

> Por Propiedad $6$

$$
= \int_{\frac{1}{3}}^1f(t)dt + \int_{1}^{\frac{5}{3}}f(t)dt + \int_{\frac{5}{3}}^{\frac{7}{4}}f(t)dt  
$$

> Dividimos los intervalos

$$
= \int_{1}^{\frac{5}{3}}f(t)dt + \int_{\frac{5}{3}}^{\frac{7}{4}}f(t)dt  
$$

> Como $\frac{1}{3} < 1$ y $x = 0$ si se encuentra en cualquier otro intervalo, entonces $\int_{\frac{1}{3}}^1f(t)dt = 0$ 

$$
= \int_{1}^{\frac{5}{3}}\frac{1}{2}dt + \int_{\frac{5}{3}}^{\frac{7}{4}}2dt  
$$

$$
= \frac{1}{2}t\Bigg|_1^{\frac{5}{3}} + 2t\Bigg|_\frac{5}{3}^{\frac{7}{4}}
$$

$$
= \left(\frac{1}{2}\times\frac{5}{3} - \frac{1}{2}\right) + \left(2\times\frac{7}{4} - 2 \times\frac{5}{3}\right)
$$

$$
= \frac{1}{2}.
$$

## Valor Esperado

La definición de Valor Esperado es análoga al caso discreto, lo que la serie se convierte en una integral dado que la variable aleatoria toma valores continuos.

### Definición 2

**Sea $X$ una variable aleatoria con función de densidad $f$, entonces definimos su valor esperado como:**

$$
E[X] = \int_{-\infty}^{+\infty}xf(x)dx
$$

**Si la integral converge absolutamente.**

### Definición 3

**Sean $X$ una variable aleatoria continua con función de densidad $f$ y $g$ un función real, entonces:**

$$
E[g(X)] = \int_{-\infty}^{+\infty} g(x)f(x)dx
$$

## Varianza

**Sea $X$ una v.a.c con $E[X] = \mu < \infty$ definimos la varianza de $X$ como:**

$$
V(X) = E[(X - \mu)^2] = E[X^2] - \mu.
$$

## Funciones de Variable Aleatoria Clásicas

### Función de Variable Aleatoria Uniforme

Se dice que $X$ tiene distribución Uniforme en el intervalo $(a,b)$ y se denota $X \sim U(a,b)$ si su función de densidad es:

#### Función de Densidad
$$
f(x) = \begin{cases}
    \frac{1}{b-a}, \text{ si } x \in (a,b) \\
    0, \text{ en otro caso}
\end{cases}
$$

> La v.a uniforme le da el mismo peso a todos los valores del intervalo $(a,b)$.

#### Función de Distribución 

$$
F(x) = 
\begin{cases}    
1, \text{ } x \geq b\\
\frac{x - a}{b - a}, \text{ } x \in (a,b) \\
0, \text{ } x \leq a
\end{cases}
$$

#### Nota
> Cuando simulamos y se nos plantea seleccionar un número $U$ al azar en el intervalo $(0,1)$ significa que $U \sim U(0,1)$.

#### Valor Esperado

$$
E[X] = \int_a^b t\frac{1}{b-a}dt = \frac{t^2}{2}\frac{1}{b-a}\Bigg|_a^b = \frac{a+b}{2}
$$

#### Varianza
$$
V(X) = \frac{(b-a)^2}{12}
$$

### Función de Variable Aleatoria Exponencial

Se dice que $X$ tiene distribución Exponencial con parámetro $\lambda > 0$ y se denota $X \sim Exp(\lambda)$.

#### Función de Densidad

$$
f(x) = \begin{cases}
    \lambda e^{-\lambda x}, \text{ } x > 0 \\
    0, \text{ } x \leq 0
\end{cases}
$$

#### Nota
> Estas v.a se utilizan comúnmente para los tiempos de vida. 

#### Función de Distribución

$$
F(x) = \begin{cases}
    1 - e^{-\lambda x}, \text{ } x > 0 \\
    0, \text{ } x \leq 0
\end{cases}
$$

#### Valor Esperado

$$
E[X] = \frac{1}{\lambda}
$$

#### Varianza

$$
V(X) = \frac{1}{\lambda^2}
$$

### Función de Variable Aleatoria Normal

Se dice que $X$ tiene distribución Normal o Gaussiana con parámetros $\mu$ y $\sigma^2$ y se denota $X \sim N(\mu,\sigma^2)$.

#### Función de Densidad

$$
f(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \text{ } x \in R
$$

#### Valor Esperado

$$
E[X] = \mu
$$

#### Varianza

$$
V(X) = \sigma^2
$$

#### Nota

> Las transformaciones lineales de una variable aleatoria con distribución normal sigue teniendo distribución normal. 
>
> Por lo que, si tenemos $X \sim N(\mu,\sigma^2)$ entonces, podemos encontrar una Variable Aleatoria $Z$ tal que: 
> $$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$
> A este de sustraer la media(Valor Esperado), en este caso y dividir por la desviación estándar (en este caso $\mu$ y $\sigma$ respectivamente) se le denomina "estandarizar una variable aleatoria". 
> 
> A la distribución $N(0,1)$ se le denomina Normal Estándar.
> 
> La Distribución Normal Estándar es simétrica.

#### Función de Distribución

No existe fórmula explícita para la función de distribución, y en el caso particular de la normal estándar, la función de distribución se denota por $\Phi(x)$ y está dada por:

$$
\Phi(x) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}dt
$$

##### Nota
> - Para los valores aproximados de esta función disponemos de tablas.
> - En esta función se cumple que: 
> $$\Phi(-x) = 1 - \Phi(x).$$

##### Ejemplo 2

Sea $X \sim N(1,9)$, halle $P(-2 \leq X \leq 2)$.

**Solución:**
$$
P(-2 \leq X \leq 2) = P(X \leq 2) - P(X \leq -2)
$$

> Por [Nota](#nota-1) de la Propiedad 6 de Variable Aleatoria Continua de Variable Aleatoria Continua.

Primero estandaricemos $X$, para ello:

$$
Z = \frac{X - 1}{3}, \text{ y para } X = \{2, -2\}
$$

$$
P(X \leq 2) - P(X \leq -2) = P\left(Z \leq \frac{2-1}{3}\right) - P\left(Z \leq \frac{-2 - 1}{3}\right) 
$$

> Sustituimos $X$ en las desigualdades

$$
= P\left(Z \leq \frac{1}{3}\right) - P\left(Z \leq -1\right) 
$$


$$
= \Phi\left(\frac{1}{3}\right) - \Phi(-1)
$$

> Por [Nota](#nota-1) de la Propiedad 6 de Variable Aleatoria Continua de Variable Aleatoria Continua en el sentido contrario.

$$
= \Phi\left(\frac{1}{3}\right) - \left(1 - \Phi(1)\right)
$$

> Por Propiedad de la Función de Distribución de la Función Normal Estándar.

## Funciones de Variable Aleatoria no Clásicas

### Situación
Muchas veces encontrar la distribución de una nueva variable aleatoria transformada a partir de una variable original puede ser extremadamente útil.

> - A la transformación que se le aplica a la variable aleatoria original $X$ la denotaremos por $\varphi$.
> - Una transformación de una varialbe aleatoria no es más que una función.
> - A la variable aleatoria original transformada le llamaremos $\varphi(X)$.

### ¿Cómo obtener la función de distribución de la Variable Aleatoria original transformada $\varphi(X)$?

Sea X v.a continua con Función de Densidad $f_X$ y Función de Distribución $F_X$, para hallar la distribución de $\varphi(X) = |X|$ (por conveniencia diremos que $Y = \varphi(X)$), hallamos primero su Función de Distribución:

$$
F_Y(y) = P(Y \leq y)
$$

$$
= P(|X| \leq y)
$$

$$
= P(-y \leq X \leq y)
$$

$$
= \boxed {F_X(y) - F_X(-y)}.
$$

Derivando en ambos miembros obtenemos la función de densidad de $Y$:

$$
f_Y(y) = f_X(y) + f_X(-y)
$$

### Obtención de Distribuciones para funciones ($\varphi$) estrictamente monótonas

Sea $X$ una variable aleatoria continua con función de densidad $f_X$ y supongamos que la función $\varphi(X)$ es estrictamente monótona y diferenciable, entonces la variable aleatoria $Y = \varphi(X)$ tiene función de densidad:

$$
f_Y(y) = \begin{cases}
    f_X(\varphi^{-1}(y))\left|\frac{d\varphi^{-1}}{dy}(y)\right|, \text{ si } y \in Dom(\varphi^{-1}) \\
    0, \text{ en otro caso }
\end{cases}
$$

#### Ejemplo 3
Sea $X \sim N(\mu,\sigma)$ se puede comprobar que $Z = \frac{X - \mu}{\sigma} \sim N(0,1)$ utilizando $\varphi(x) = \frac{x - \mu}{\sigma}$.

**Solución:**

Al ser $\varphi$ una funci'on lineal, cumple que es estrictamente creciente y diferenciable, y adem'as su funci'on inversa es:

$$
\varphi^{-1}(y) = \sigma y + \mu 
$$

y su derivada
$$
\frac{d\varphi^{-1}}{dy} = \sigma
$$

La función de densidad de $X$ es:

$$
f_X(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x - \mu)^2}{2\sigma^2 }}
$$

Evaluando $f_X$ en la derivada de $\varphi^{-1}$ tenemos:

$$
f_X\left(\varphi^{-1}(y)\right) \left|\frac{d\varphi^{-1}}{dy}\right| = \frac{1}{\sqrt{2\pi}\cancel{\sigma}}e^{-\frac{\left[(\sigma y + \mu) - \mu\right]^2}{2\sigma^2}} \times \cancel{|\sigma|}
$$

$$
= \frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}
$$

Por lo que:

$$
 \boxed{f_Y(y) = \frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}}
$$

Por tanto, $Z \sim N(0,1).$ $\blacksquare$

#### Resumiendo
**Si tenemos $X \sim M$ e $Y = \varphi(X)$ es estrictamente monótona, entonces seguimos los siguientes pasos:**

1) **Hallamos la función inversa $\varphi^{-1}(y)$.**
2) **Hallamos la derivada de la función inversa $\frac{d\varphi^{-1}}{dy}$.**
3) **Evaluamos la función de densidad de $M$.**
4) **Tendremos que $f_Y = f_M(\varphi^{-1}(y))\left|\frac{d\varphi^{-1}}{dy}(y)\right|$**