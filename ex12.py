import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8])
y = np.array([110, 123, 119, 86, 62])
coef = np.polyfit(x, y, 2)
print(coef)
polynomial_model = np.poly1d(coef)
xp = np.linspace(0, 8, 100)
plt.scatter(x, y)
plt.plot(xp, polynomial_model(xp), c='r')
plt.show()
y_pred = polynomial_model(x)
r_squared = np.corrcoef(y, y_pred)[0, 1]**2
print("Feito por Andre e Fulvio")
print(r_squared)
