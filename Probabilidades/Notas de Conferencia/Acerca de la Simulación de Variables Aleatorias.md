## ¿ Qué es Simular una Variable Aleatoria ?

**Simular una variable Aleatoria** significa usar una computadora para generar valores que siguen la misma distribución de probabilidad que la variable. Esto se puede hacer utilizando diversos algoritmos, entre ellos, uno de los métodos más comunes es el método de la **transformada inversa**.

## Método de la Transformada Inversa

Se basa en la relación entre una variable aleatoria $X$ y su función de distribución acumulada  $F_X(x)$ (ver las notas de [Variable Aleatoria Discreta](Variable%20Aleatoria%20Discreta%201)).

El método implica los siguientes pasos:

1) Generar un número aleatorio uniforme $U$ entre $0$ y $1$.
2) Encontrar el valor $x$ tal que $F_X(x) = U$.
3) Asignar este valor $x$ como la muestra de la variable aleatoria.
### Pasos Detallados:
#### 1) Generar un Número Aleatorio Uniforme:

Generamos un número aleatorio $U$ que está [uniformemente distribuido](#distribución-uniforme) entre $0$ y $1$. Esto se puede hacer fácilmente en la mayoría de los lenguajes de programación.

#### 2) Calcular la Función de Distribución Acumulada Inversa:

##### En Distribuciones Continuas:
Para encontrar el valor $x$ correspondiente a $U$, necesitamos la función de distribución acumulada inversa $F_X^{−1}(u)$. Para una variable aleatoria $X$, si $U$ es uniformemente distribuido en $[0, 1]$, entonces $X=F_X^{−1}(U)$ tiene la distribución deseada.

##### En Distribuciones Discretas:
En este caso $F_X^{-1}(u)$ es un poco diferente. Aquí usamos una tabla de probabilidades acumuladas para encontrar el intervalo en el que $U$ cae y asignar el valor correspondiente.
#### 3) Asignar el Valor de la Variable Aleatoria:

Finalmente, el valor $x$ que encontramos se considera una muestra de la variable aleatoria $X$.

# Distribución uniforme

Decimos que un número esta uniformemente distribuido si cada valor dentro de un intervalo especificado tiene la misma probabilidad de ser seleccionado.