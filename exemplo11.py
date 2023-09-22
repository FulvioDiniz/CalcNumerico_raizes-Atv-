import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

# Dados de exemplo
x = np.array([4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1])
y = np.array([126, 121, 116, 118, 114, 118, 132, 141])

# Funções para as transformações
def exponential_transform(x, a, b, c):
    return a * np.exp(b * x) + c

def power_transform(x, a, b, c):
    return a * np.power(x, b) + c

def saturation_transform(x, a, b, c):
    return a / (1 + np.exp(-b * (x - c)))

# Modelos de regressão linear
linear_model = LinearRegression()
linear_model.fit(x.reshape(-1, 1), y)

# Aplicar transformações e ajustar modelos
params_exponential, _ = curve_fit(exponential_transform, x, y, maxfev=10000)  # Aumentamos maxfev
params_power, _ = curve_fit(power_transform, x, y)
params_saturation, _ = curve_fit(saturation_transform, x, y)

# Resto do código (gráficos, resultados) permanece o mesmo


# Gerar pontos para os gráficos
x_range = np.linspace(min(x), max(x), 100)
y_linear = linear_model.predict(x_range.reshape(-1, 1))
y_exponential = exponential_transform(x_range, *params_exponential)
y_power = power_transform(x_range, *params_power)
y_saturation = saturation_transform(x_range, *params_saturation)

# Exibir resultados
print("Regressão Linear:")
print(f"Coeficiente angular (a1): {linear_model.coef_[0]:.2f}")
print(f"Coeficiente linear (a0): {linear_model.intercept_:.2f}")
print("\nTransformação Exponencial:")
print(f"Coeficientes (a, b, c): {params_exponential}")
print("\nTransformação Potência:")
print(f"Coeficientes (a, b, c): {params_power}")
print("\nTransformação Saturação:")
print(f"Coeficientes (a, b, c): {params_saturation}")

# Plot dos gráficos
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x_range, y_linear, color='red', label='Regressão Linear')
plt.xlabel('Chuvas diárias (em 0,01 cm)')
plt.ylabel('Partículas removidas (Mg/m3)')
plt.legend()

plt.subplot(2, 2, 2)
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x_range, y_exponential, color='green', label='Transformação Exponencial')
plt.yscale('log')
plt.xlabel('Chuvas diárias (em 0,01 cm)')
plt.ylabel('Partículas removidas (Mg/m3)')
plt.legend()

plt.subplot(2, 2, 3)
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x_range, y_power, color='purple', label='Transformação Potência')
plt.yscale('log')
plt.xlabel('Chuvas diárias (em 0,01 cm)')
plt.ylabel('Partículas removidas (Mg/m3)')
plt.legend()

plt.subplot(2, 2, 4)
plt.scatter(x, y, color='blue', label='Dados Originais')
plt.plot(x_range, y_saturation, color='orange', label='Transformação Saturação')
plt.xlabel('Chuvas diárias (em 0,01 cm)')
plt.ylabel('Partículas removidas (Mg/m3)')
plt.legend()

plt.tight_layout()
plt.show()
