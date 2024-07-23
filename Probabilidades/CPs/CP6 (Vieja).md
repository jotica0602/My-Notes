Alejandro Echevarría Brunet

# CP\#6: Variable Aleatoria Continua

## Ejercicios Prácticos

### Ejercicio 1:

Una variable aleatoria tiene la siguiente función de distribución:

$$
F_X(x) = 
\begin{cases}
0, & \text{ si } x < 0\\
\frac{1}{20} (x+4)^2 - \frac{a}{5}, &\text{ si } 0 \leq x \leq 2\\
1, & \text{ si } x > 2\\    
\end{cases}
$$

a) Determine la función de densidad de X.
b) Halle el valor de $a$.
c) Halle $E[X]$. 

#### Solución:

a) Utilizando la propiedad 2 de [[Variable Aleatoria Continua#Propiedades de la Variable Aleatoria Continua]] tenemos que:

$$
\frac{dF}{dx}(x) = f_X(x)
$$

$$
f_X(x) = 
\begin{cases}
\frac{1}{10}(x+4), &\text{ si } 0 \leq x \leq 2 \\
0, &\text{ en otro caso.}
\end{cases}
$$

b) De [[Variable Aleatoria Continua#Propiedades de la Variable Aleatoria Continua]], por la propiedad 6 tenemos que $F_X(x)$ es una función continua, por lo que:

$$
\lim_{x \to 2^-} F_X(x) = \lim_{x \to 2^+} F_X(x)
$$

O sea:
$$
\lim_{x \to 2^-} F_X(x) = 1
$$

$$
\frac{1}{20} (2+4)^2 - \frac{a}{5} = 1
$$

$$
\boxed{a = 4}
$$

c) 
$$
E[X] = \int_{-\infty}^{+\infty} x f_X(x)
$$

$$
= \int_{0}^{2} x \frac{1}{10}(x+4) = \int_{0}^{2} \frac{1}{10} x^2 + \int_{0}^{2} \frac{1}{10}4x 
$$

$$
= \frac{x^3}{30}\Big|_0^2 + \frac{4x^2}{20}\Big|_0^2 = \boxed{\frac{16}{15}}
$$

### Ejercicio 2:

Un ómnibus llega a una parada específica en intervalos de $15$ minutos empezando a las $7:00$ a.m, o sea, llega a las 7:00, 7:15, 7:30, 7:45, ... . Se conoce que el tiempo en que un pasajero llega a la parada tiene distribución uniforme entre 7:00 y 7:30.

a) Determine la probabilidad de que el pasajero espere menos de 5 minutos por el ómnibus.
b) Halle la probabilidad de que el pasajero espere más de 10 minutos por el ómnibus.
c) Calcule el valor esperado del tiempo de espera.

#### Solución:

a) Sea $X$ la variable aleatoria que define el tiempo de llegada del pasajero, entonces:

$$
f_X(x) = 
\begin{cases}
\frac{1}{30}, & \text{ si } 0 \leq x \leq 30 \\
0, & \text{ en otro caso.}
\end{cases}
$$

Para que el pasajero espere menos de 5 minutos por el ómnibus, éste debería llegar en el intervalo $(10,15]$ ó en el intervalo $(25,30]$:

$$
P(10 < X \leq 15) + P(25 < X \leq 30) = F_X(15) - F_X(10) + F_X(30) - F_X(25)
$$

> Por propiedad 6 de [[Variable Aleatoria Continua#Propiedades de la Variable Aleatoria Continua]], que para $X \sim U(a,b) = \frac{x - a}{b - a}$. En este caso $a = 0$ y $b = 15$

$$
\frac{15}{30} - \frac{10}{30} + \frac{30}{30} - \frac{25}{30} = \boxed{\frac{1}{3}}
$$

b) La probabilidad de que el pasajero espere más de 10 minutos por el ómnibus significa que éste llegue en el intervalo $[0,5)$ ó en el intervalo $[15,20)$:

$$
P(0 \leq X < 5) + P(15 \leq X < 20) = F_X(5) - F_X(0) + F_X(20) - F_X(15)
$$

$$
= \frac{5}{30} - \frac{0}{30} + \frac{20}{30} - \frac{15}{30} = \boxed{\frac{1}{3}}
$$

c) sea $g(x)$ la función que define el tiempo de espera, ésta está definida de la siguiente forma:

$$
g(x) = 
\begin{cases}
    15 - x, & \text{ si } 0 \leq x \leq 15 \\
    30 - x, & \text{ si } 15 < x \leq 30 \\
    0, & \text{ en otro caso.}
\end{cases}
$$

$$
E[g(X)] = \int_{0}^{15}g(x)f(x)dx + \int_{15}^{30}g(x)f(x)dx
$$

$$
= \int_{0}^{15} (15 - x)\frac{1}{30} dx + \int_{15}^{30}(30-x)\frac{1}{30}dx
$$

$$
= \int_{0}^{15} \frac{15}{30}dx - \int_{0}^{15}\frac{x}{30} dx + \int_{15}^{30} \frac{30}{30} dx - \int_{15}^{30}\frac{x}{30} dx
$$

$$
= \frac{15}{30}x\Big|_{0}^{15} - \frac{x^2}{60}\Big|_{0}^{15} + \frac{30}{30}x\Big|_{15}^{30} - \frac{x^2}{60}\Big|_{15}^{30}
$$

$$
= \frac{225}{30} - \frac{225}{60} + 30 - 15 - \frac{900}{60} + \frac{225}{60} = \boxed{\frac{15}{2}}
$$

### Ejercicio 3:
El tiempo en horas que se requiere para reparar una máquina es una v.a que sigue una distribución exponencial con parámetro $\lambda = \frac{1}{2}$.

a) Determine la probabilidad de que el tiempo de reparación exceda las 2 horas.
b) Halla la probabilidad de que la reparación dure al menos 10 horas dado que se conoce que la duración excede las 9 horas.

#### Solución:
Sea $X$ la variable aleatoria que define el proceso de reparación, la función de densidad de la distribución exponencial está dada por:

$$
f_X(x) = 
\begin{cases}
\lambda e^{-\lambda x}, & \text{ si } 0 \leq x \\
0, & \text{en otro caso.}    
\end{cases}
$$

a) 
$$
\text{ } P(X > 2) = 1 - P(X \leq 2) = 1 - \int_{0}^{2} \lambda e^{-\lambda x}dx = 1 - (-e^{-\lambda x})\Big|_{0}^{2}
$$

$$
= 1 - (-e^{-2\lambda} + 1) = e^{-2\lambda}
$$

$$
= \boxed{e^{-1}}
$$


b) $P(X > 10 | X > 9) = P(X - 9 > 1 | X > 9)= P(X > 1)$ debido a la [[CP6 (Vieja)#Ejercicio 9 (Ausencia de Memoria de la Distribución Exponencial)]]] 

$$
P(X > 1) = 1 - P(X \leq 1) = 1 - (-e^{-\lambda x})\Big|_{0}^{1}
$$

$$
= 1 - (-e^{-\lambda} + 1) = e^{-\lambda} = \boxed{e^{-\frac{1}{2}}}
$$

> Pues recordemos en ambos resultados finales que $\lambda = \frac{1}{2}$.

### Ejercicio 4:

Sea $X \sim N(12,4)$.

a) Calcule $P(X > 13)$.
b) Calcule $P(10 < x < 11)$
c) Halle el valor de $c$ para el cual $P(X > c) = 0.1$

#### Solución:

Para las próximas soluciones necesitaremos estandarizar nuestra variable aleatoria $X$. Sea $Z \sim N(0,1)$. 

$$
Z = \frac{X - 12}{2}
$$

a) 
$$
\text{ } P(X > 13) = 1 - P(X \leq 13)
$$

$$
1 - P \left( Z \leq \frac{13-12}{2} \right) = 1 - P \left( Z \leq \frac{1}{2} \right) = 1 - \varPhi \left( \frac{1}{2} \right) = 1 - 0.6915
$$

$$
= \boxed{0.3085}
$$

b) 

$$
P(10 < X < 11) = P \left ( \frac{10 - 12}{2} < Z < \frac{11 - 12}{2} \right) 
$$

$$
= P \left( -1 < Z < -\frac{1}{2} \right) = \varPhi \left ( -\frac{1}{2} \right) - \varPhi(-1)  
$$

$$
= 1-\varPhi \left( \frac{1}{2}\right) - (1 - \varPhi(1))
$$

$$
= -\varPhi \left( \frac{1}{2}\right) + \varPhi(1)
$$

$$
= -0.6915 + 0.8413 
$$

$$
= \boxed{0.1498}
$$

c) 

$$
P(X > c) = 0.1 \iff P \left( Z > \frac{c - 12}{2} \right) = 0.1
$$

$$
\implies 1 - P \left( Z \leq \frac{c - 12}{2} \right) = 0.1
$$

$$
\implies 1 - \varPhi \left( \frac{c - 12}{2} \right) = 0.1
$$

$$
\implies \varPhi \left( \frac{c - 12}{2} \right) = 0.9
$$

$$
\implies  \frac{c - 12}{2} = \varPhi^{-1}(0.9)
$$

$$
\implies  \frac{c - 12}{2} = 1.29
$$

$$
\implies  \boxed{c = 14.58}
$$

### Ejercicio 5:

Sea $X \sim N(5,\sigma^2)$ y se conoce que $P(X > 9) = 0.2$. Calcule el valor aproximado de $V(X)$

#### Solución:

Sea $Z \sim N(0,1)$:

$$
Z = \frac{X - 5}{\sigma}
$$

Ahora:

$$
P(X > 9) = 0.2 \iff P \left(Z > \frac{9-5}{\sigma} \right) \iff 1 - P \left(Z \leq \frac{4}{\sigma} \right) = 0.2
$$

$$
\implies P \left(Z \leq \frac{4}{\sigma} \right) = 0.8
$$

$$
\implies \varPhi \left(\frac{4}{\sigma} \right) = 0.8
$$

$$
\implies \frac{4}{\sigma} = \varPhi^{-1}(0.8)
$$

$$
\implies \frac{4}{\sigma} = 0.84 
$$

$$
\implies \boxed{\sigma = 4.76}
$$

## Ejercicios Teóricos:

### Ejercicio 6:

Halle la varianza de $X$, si $X \sim Exp(\lambda)$.

#### Solución:

$$
V(X) = E[X^2] - (E[X])^2
$$

$$
V(X) = \int_{0}^{+\infty}x^{2}f(x)dx - \int_{0}^{+\infty}xf(x)dx 
$$

Trabajemos primeramente con $E[X^2]$

$$
= \int_{0}^{+\infty}x^{2}f(x)dx = \int_{0}^{+\infty} x^2 \lambda e^{-\lambda x} dx
$$

Aplicando el método de integración por partes, sean: 
$
u = x^2 \\ 
dv = \lambda e^{-\lambda x}dx \\
du = 2xdx \\
v = -e^{-\lambda x}
$

$$
uv - \int_{0}^{+\infty}vdu
$$

$$
= -x^2e^{-\lambda x} - \int_{0}^{+\infty}-e^{-\lambda x}2xdx
$$

$$
= -x^2e^{-\lambda x} +2\int_{0}^{+\infty}e^{-\lambda x} x dx
$$

Volviendo a aplicar el método de integración por partes, sean:
$
u = x \\
dv = e^{-\lambda x} \\
du = dx \\ 
v = -\frac{1}{\lambda} e^{-\lambda x}
$

$$
= -x^2e^{-\lambda x} + 2 \left( uv - \int_{0}^{+\infty}vdu \right) 
$$

$$
= -x^2e^{-\lambda x} + 2 \left( -\frac{1}{\lambda} xe^{-\lambda x} - \int_{0}^{+\infty}  -\frac{1}{\lambda} e^{-\lambda x} dx \right)
$$

$$
= -x^2e^{-\lambda x} -\frac{2}{\lambda} xe^{-\lambda x} + \frac{2}{\lambda} \int_{0}^{+\infty} e^{-\lambda x} dx
$$

$$
= -x^2e^{-\lambda x} -\frac{2}{\lambda} xe^{-\lambda x} - \frac{2}{\lambda^2}\int_{0}^{+\infty} -\lambda e^{-\lambda x} dx
$$

$$
= \left( -x^2e^{-\lambda x} -\frac{2}{\lambda} xe^{-\lambda x} - \frac{2}{\lambda^2} e^{-\lambda x} \right)\bigg|_{0}^{+\infty}
$$

$$
= \lim_{x \to +\infty} \left( -x^2e^{-\lambda x} -\frac{2}{\lambda} xe^{-\lambda x} - \frac{2}{\lambda^2} e^{-\lambda x} \right) - (-0^2e^{-\lambda 0} -\frac{2}{\lambda} 0e^{-\lambda 0} - \frac{2}{\lambda^2} e^{-\lambda 0})
$$

$$
= \cancel{\lim_{x \to +\infty} \left( -x^2e^{-\lambda x} \right)}^{0, x \to +\infty} + \cancel{\lim_{x \to +\infty} \left( -\frac{2}{\lambda} xe^{-\lambda x} \right)}^{0, x \to +\infty} +  \cancel{\lim_{x \to +\infty} \left( - \frac{2}{\lambda^2} e^{-\lambda x} \right)}^{0, x \to +\infty} + \frac{2}{\lambda^2}
$$

$$
= \boxed{\frac{2}{\lambda^2}}
$$

Ahora trabajemos con $E[X]$:

$$
E[X] = \int_{0}^{+\infty}xf(x)dx = \int_{0}^{+\infty}x\lambda e^{-\lambda x} dx 
$$

Aplicando el método de integración por partes, sean:
$
u = x \\
du = dx \\
dv = \lambda e^{-\lambda x} dx \\
v = -e^{-\lambda x}
$

$$
= uv - \int_{0}^{+\infty}vdu
$$

$$
= -xe^{-\lambda x} - \int_{0}^{+\infty} - e^{-\lambda x}dx
$$

$$
-xe^{-\lambda x} - \frac{1}{\lambda} \int_{0}^{+\infty} - \lambda e^{-\lambda x}
$$

$$
= \left( -xe^{-\lambda x} - \frac{1}{\lambda} e^{-\lambda x} \right) \bigg|_{0}^{+\infty}
$$

$$
= \lim_{x \to +\infty}\left( -xe^{-\lambda x} - \frac{1}{\lambda} e^{-\lambda x} \right) - \left( -0e^{-\lambda 0} - \frac{1}{\lambda} e^{-\lambda 0} \right)
$$

$$
\lim_{x \to +\infty}\left( -xe^{-\lambda x} - \frac{1}{\lambda} e^{-\lambda x} \right) + \frac{1}{\lambda}
$$

$$
\cancel{\lim_{x \to +\infty}\left( -xe^{-\lambda x} \right)}^{0, x \to +\infty} + \cancel{\lim_{x \to +\infty}\left( -\frac{1}{\lambda} e^{-\lambda x} \right)}^{0, x \to +\infty} + \frac{1}{\lambda}
$$

$$
= \boxed{\frac{1}{\lambda}}
$$

Volviendo a la ecuación principal:

$$
V(X) = E[X^2] - (E[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \boxed{\frac{1}{\lambda^2}}
$$


### Ejercicio 7:

Dada una variable aleatoria $U \sim U(a,b)$, calcula la probabilidad de que tome valores entre $\frac{(a+b)}{4}$ y $\frac{(a+b)}{2}$.

#### Solución:

Sea $f_X(x)$ la función de densidad de nuestra variable aleatoria uniforme definida por:

$$
f_X(x) =
\begin{cases}
\frac{1}{b-a}, & \text{ si } a \leq x \leq b \\
0, & \text{ en otro caso. }
\end{cases}
$$

Entonces $F_X(x)$ se define como:

$$
F_X(x) = 
\begin{cases}
0, & \text{ si } x < a \\
\frac{x - a}{b - a}, &\text{ si } a \leq x \leq b \\ 
1, & \text{ si } x > b
\end{cases}
$$

Ahora:

$$
P \left( \frac{(a+b)}{4} \leq X \leq \frac{(a+b)}{2} \right) = F_X \left( \frac{(a+b)}{2}\right) - F_X \left( \frac{(a+b)}{4}\right)
$$

$$
= \frac{\frac{(a+b)}{2} - a}{b-a} - \frac{\frac{(a+b)}{4} - a}{b-a} = \frac{\frac{(a+b)}{2} - a - \frac{(a+b)}{4} + a}{b-a} = \frac{\frac{2(a+b) - (a+b)}{4}}{b-a} = \frac{\frac{(a+b)}{4}}{b-a}  
$$

$$
= \boxed{\frac{a+b}{4(b-a)}}
$$

### Ejercicio 8:

Sea la variable aleatoria $X \sim N(\mu,\sigma^2)$, halle la probabilidad de que $X$ se encuentre en los siguientes intervalos:

a) $[\mu - \sigma, \mu + \sigma]$
b) $[\mu - 2\sigma, \mu + 2\sigma]$
c) $[\mu - 3\sigma, \mu + 3\sigma]$

#### Solución:

a) El procedimiento es similar para cada inciso por lo que solo haremos el primero:

Sea $Z \sim N(0,1)$:

$$
Z = \frac{X - \mu}{\sigma}
$$

$$
P(\mu - \sigma \leq X \leq \mu + \sigma) \iff P \left( \frac{(\mu - \sigma) - \mu}{\sigma} \leq Z \leq \frac{(\mu + \sigma) - \mu}{\sigma} \right)
$$

$$
= P(-1 \leq Z \leq 1) = \varPhi(1) - \varPhi(-1)
$$

$$
= \varPhi(1) - (1- \varPhi(1)) = 2\varPhi(1) - 1 = 2 \times 0.8413 - 1
$$

$$
= 1.6826 - 1 = \boxed{0.6826}
$$

### Ejercicio 9 (Ausencia de Memoria de la Distribución Exponencial):

Sea $X \sim Exp(\lambda)$, pruebe que:

$$
P(X - t > x | X > t) = P(X > x) \text{ } x,t \geq 0
$$

#### Solución:

Primeramente hallemos $P(X > x)$:

$$
P(X > x) = 1 - P(X \leq x) = 1 - \int_{0}^{x}f(u)du
$$

$$
= 1 - \int_{0}^{x} \lambda e^{-\lambda u} du
$$

$$
1 - (-e^{-\lambda u})\bigg|_{0}^{x} = 1 - (-e^{-\lambda x} + 1) = \boxed{e^{-\lambda x}}
$$

Ahora hallemos $P(X - t > x | X > t)$:

$$
P(X - t > x | X > t) = P(X > x + t | X > t)
$$

$$
P(X > x + t | X > t) = \frac{P(X > x + t \cap X > t)}{P(X > t)}
$$

> Como $x$ y $t$ son valores no negativos, si $X > x + t \implies X > t$, en otras palabras: 
> Si $(X > x + t) \subset (X > t) \implies (X > x + t) \cap (X > t) = (X > x + t)$ 

$$
= \frac{P(X > x + t)}{P(X > t)} = \frac{1 - P(X \leq x + t)}{1 - P(X \leq t)} = \frac{1 - \int_{0}^{x+t}f(u)du}{1 - \int_{0}^{t}f(u)du}
$$

$$
= \frac{1 - \int_{0}^{x+t} \lambda e^{-\lambda u} du}{1 -\int_{0}^{t} \lambda e^{-\lambda u}du} = \frac{1 - (-e^{-\lambda u})\bigg|_{0}^{x+t}}{1 - (-e^{-\lambda u})\bigg|_{0}^{t}} = \frac{1 - (-e^{-\lambda (x+t)} + 1)}{1 - (-e^{-\lambda (t)} + 1)}
$$

$$
= \frac{e^{-\lambda(x + t)}}{e^{-\lambda t}} = \boxed{e^{-\lambda x} = P(X > x)}. \ \blacksquare
$$

### Ejercicio 10:

Cuál es la probabilidad de que las raíces dela ecuación $4x^2 + 4Yx + Y + 2 = 0$ sean ambas reales si $Y \sim U(0,5)$.

#### Solución:

Para que una ecuación cuadrática tenga soluciones reales, su discriminante debe ser mayor o igual que 0.

Hallemos el discriminante:

$$
D = b^2 - 4ac \geq 0
$$

$$
D = (4Y)^2 - 4(4)(Y+2) = 16Y^2 - 16Y -32 \geq 0
$$

$$
Y^2 - Y - 2 \geq 0
$$

$$
(Y-2)(Y+1) \geq 0
$$

De donde:
$$
Y \geq 2 \land Y \geq -1
$$

Como $Y \sim U(0,5)$, es imposible que $Y$ tome el valor $-1$, por lo que solo nos resta hallar la probabilidad de que $Y$ tome valores en el intervalo $[2,5]$.

$$
P(2 \leq Y \leq 5) = F_Y(5) - F_Y(2) = \frac{5}{5} - \frac{2}{5} = \boxed{\frac{3}{5}}
$$