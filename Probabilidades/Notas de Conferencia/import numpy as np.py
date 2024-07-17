import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Función para simular valores normales
def simulate_normal():
    while True:
        x = random.random()
        y = random.expovariate(1)
        if x <= math.exp((-(y - 1) ** 2) / 2):
            return y

# Generar datos utilizando la función simulate_normal
num_samples = 10000
data = [simulate_normal() for _ in range(num_samples)]

# Mostrar los primeros 10 valores generados
print("Primeros 10 valores generados:")
print(data[:10])

# Graficar histograma para visualizar la distribución
plt.hist(data, bins=50, density=True, alpha=0.5, color='g', edgecolor='black', label='Histograma de datos')

# Graficar la función de densidad de probabilidad teórica
x = np.linspace(0, np.max(data), 1000)
pdf = np.exp((-(x - 1) ** 2) / 2) / (np.sqrt(2 * np.pi))
plt.plot(x, pdf, 'r-', lw=2, label='PDF teórica')

# Graficar la función e^{-(x-1)^2/2}
exp_function = np.exp((-(x - 1) ** 2) / 2)
plt.plot(x, exp_function, 'b-', lw=2, label='$e^{\\frac{-(x-1)^2}{2}}$')

plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución generada por simulate_normal')
plt.legend()
plt.show()
