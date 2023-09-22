import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([4.3, 4.5, 5.9, 5.6, 6.1, 5.2, 3.8, 2.1]).reshape(-1, 1)
y = np.array([126, 121, 116, 118, 114, 118, 132, 141])

model = LinearRegression()
model.fit(x, y)

a0 = model.intercept_
a1 = model.coef_[0]
r2 = model.score(x, y)

y_pred = model.predict(x)

plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, y_pred, color='red', label='Predicted')
plt.xlabel('Chuvas diárias (em 0,01 cm)')
plt.ylabel('Partículas removidas (Mg/m3)')
plt.legend()
plt.show()
print("Feito por Fulvio Diniz Santos")
print(f'a0: {a0}')
print(f'a1: {a1}')
print(f'r2: {r2}')
