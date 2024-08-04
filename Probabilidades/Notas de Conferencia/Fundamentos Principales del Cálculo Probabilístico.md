
# Tema: Convergencia de sucesiones de variables aleatorias. Ley de los grandes Números. Teorema Central del Límite.

## Convergencia de Sucesiones de Variables Aleatorias

**Modos de Convergencia:**

- Casi segura: $X_n \to_{n \to \infty}^{c.s} X$ ssi $P({\omega \in \Omega : Xn(\omega) \to_{n \to \infty} X(\omega)}) = 1.$

- En probabilidad: $X_n \to_{n \to \infty}^p X$ ssi $\forall \varepsilon > 0, \lim_{n \to \infty} P(|X_n - X| > \varepsilon) = 0.$ 

## Leyes de los Grandes Números

### Ley Fuerte de los Grandes Números (LFGN):

$$
\frac{1}{n} \sum_{i=1}^{n}X_i - \sum_{i=1}^{n}\frac{1}{n}E[X_i] \to^{c.s} 0
$$
> Para valores suficientemente grandes $n$, la sucesión tiende a su valor esperado.
### Ley Débil de los Grandes Números:

$$
\frac{1}{n} \sum_{i=1}^{n}X_i - \sum_{i=1}^{n}\frac{1}{n}E[X_i] \to^{p} 0
$$
> Para valores suficientemente grandes $n$, la sucesión tiende a su valor esperado en probabilidad.

## Teoremas

- **Khinchin:** $\{X_n\}$ sucesión de variables independientes e igualmente distribuidas (iid) tales que $E[X_i] = \mu < +\infty, \text{ } i=1,2,... \implies X_n$ cumple **LFGN**.

- **Chebyshev:** $\{X_n\}$ sucesión de variables aleatorias independientes tales que $E[X_i] = \mu < +\infty, \forall i$ y $V(X_i) \leq M \implies X_n$ cumple **LDGN**.

- **Markov:** $\{X_n\}$ sucesión de variables aleatorias, $\frac{1}{n^2}V(\sum_{i=1}^{n} X_i) \to_{n \to \infty} 0 \implies X_n$ cumple **LDGN**.

- **Kolmogorov:** $\{X_n\}$ sucesión de variables aleatorias, $E[X_i] = \mu_i < +\infty, V(X_i) = \sigma^2_i \forall i, \sum_{i=1}^{\infty} \frac{\sigma_i^2}{i^2} < +\infty \implies X_n$ cumple **LFGN.**

## Teorema Central del Límite

### Moivre-Laplace

Sea $\{X_n\}$ sucesión de variables aleatorias de Bernoulli iid, $E[X_k] = p$ y $V(X_k) = p(1-p)$

$$
\implies \frac{\sum_{k=1}^n X_k - np}{\sqrt{np(1-p)}} \to^D Z \sim N(0,1)
$$
### Linderbeg-Lévy

Sea $\{X_n\}$ sucesión de variables aleatorias tal que $E[X_k] = \mu_k < +\infty$ y $V(\sum_{k=1}^{n}X_k) < +\infty$

$$
\implies \frac{\sum_{k=1}^n X_k - \sum_{k=1}^n \mu_k}{\sqrt{V(\sum_{k=1}^n X_k)}} \to^D Z \sim N(0,1)
$$

Si son iid, entonces el valor esperado siempre es el mismo, por lo que sumaríamos $n$ veces ese valor:

$$
\implies \frac{\sum_{k=1}^n X_k - n\mu}{\sqrt{n}\sigma} \to^D Z \sim N(0,1)
$$

