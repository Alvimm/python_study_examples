import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

file = pd.read_csv('expenses_data.csv')


day = file[['day']]
alimentation = file[['alimentation']]
clothing = file[['clothing']]
transport = file[['transport']]

x = np.array(file).reshape((-1, 1))
# y = np.array(file[clothing]).reshape((-1, 1))
# z = np.array(file[transport]).reshape((-1, 1))
regr = LinearRegression().fit(X=day, y=alimentation)

# regr
# regr.fit(X=day, y=clothing)
# regr.fit(X=day, y=transport)


plt.scatter(day, alimentation, color='red')

# ***************************** TRANSFORMAR EM CLASSE,FUNCIONANDO !!!*******************************

# day = file[['day']]
# alimentation = file[['alimentation']]
# clothing = file[['clothing']]
# transport = file[['transport']]

# plt.plot(day, alimentation, color='blue')
# plt.plot(day, clothing, color='yellow')
# plt.plot(day, transport, color='black')
# plt.legend(['Alimentation', 'Clothing', 'Transport'])
# plt.xlabel('Day')
# plt.ylabel('Expenses in BRL')
# plt.title('Expense graphs')


plt.show()
