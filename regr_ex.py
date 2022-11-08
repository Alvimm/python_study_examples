import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1))
y = np.array([6, 12, 14, 23, 27, 32])

model = LinearRegression().fit(x, y)

# Predict a response and print it
y_pred = model.predict(x)
print('Data test:', y, sep='\n')
print('Data predict:', y_pred, sep='\n')

plt.scatter(x, y, c='blue')
plt.plot(x, y_pred, c='red')
plt.legend(['Predict', 'Real'])
plt.show()
