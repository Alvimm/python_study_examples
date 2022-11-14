import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ***************************** ENTRADA DE DADOS*******************************
file = pd.read_csv('expenses_data.csv')
day = file['day'].values
alimentation = file['alimentation'].values
clothing = file['clothing'].values
transport = file['transport'].values

# ***************************** SÉRIES TEMPORAIS*******************************

# plt.plot(day, alimentation, '-o', color='green', linewidth=3,
#          markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
# plt.plot(day, clothing, '-o', color='yellow', linewidth=3,
#          markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
# plt.plot(day, transport, '-o', color='black', linewidth=3,
#          markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
# plt.legend(['Alimentation', 'Clothing', 'Transport'])
# plt.xlabel('Day')
# plt.ylabel('Expenses in BRL')
# plt.title('Expense graphs')


class Time_series():
    def show_graphs(self, x, y, z):
        plt.plot(day, x, '-o', color='green', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
        plt.plot(day, y, '-o', color='yellow', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
        plt.plot(day, z, '-o', color='black', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)
        plt.legend(['Alimentation', 'Clothing', 'Transport'])
        plt.xlabel('Day')
        plt.ylabel('Expenses in BRL')
        plt.title('Expense graphs')
        plt.show()


# test = Time_series()
# test.show_graphs(alimentation, clothing, transport)


# ***************************** REGRESSÃO LINEAR !!!*******************************
# ***************************************** ALIMENTATION ********************************
regr = LinearRegression()
day = day.reshape(-1, 1)
regr.fit(day, alimentation)
angular_coef = regr.coef_[0]
linear_coef = regr.intercept_
line = angular_coef * day + linear_coef


class Linear_regr():
    def show_linear_regr(self, name):
        plt.plot(day, line, label='Linear regression', c='blue')
        plt.plot(day, name, '-o', label='alimentation - original', linewidth=3,
                 markerfacecolor='black', markeredgecolor='black', markeredgewidth=4, c='red')
        plt.xlabel('Day')
        plt.ylabel(f'{name} expenses in BRL')
        plt.legend()
        plt.show()


test = Linear_regr()
test.show_linear_regr(alimentation)
test.show_linear_regr(clothing)
test.show_linear_regr(transport)

# plt.plot(day, line, label='Linear regression', c='blue')
# plt.plot(day, alimentation, '-o',
#          label='alimentation - original', linewidth=3, markerfacecolor='black', markeredgecolor='black', markeredgewidth=4, c='red')
# plt.xlabel('Day')
# plt.ylabel('Alimentation expenses in BRL')
# plt.legend()


# ***************************************** CLOTHING ********************************
# regr = LinearRegression()
# day = day.reshape(-1, 1)
# regr.fit(day, clothing)
# angular_coef = regr.coef_[0]
# linear_coef = regr.intercept_
# line = angular_coef * day + linear_coef

# plt.plot(day, line, label='Linear regression', c='blue')
# plt.plot(day, clothing, '-o',
#          label='clothing - original', linewidth=3, markerfacecolor='black', markeredgecolor='black', markeredgewidth=4, c='red')
# plt.xlabel('Day')
# plt.ylabel('Clothing expenses in BRL')
# plt.legend()


# # ***************************************** TRANSPORT ********************************
# regr = LinearRegression()
# day = day.reshape(-1, 1)
# regr.fit(day, transport)
# angular_coef = regr.coef_[0]
# linear_coef = regr.intercept_
# line = angular_coef * day + linear_coef

# plt.plot(day, line, label='Linear regression', c='blue')
# plt.plot(day, transport, '-o',
#          label='transport - original', linewidth=3, markerfacecolor='black', markeredgecolor='black', markeredgewidth=4, c='red')
# plt.xlabel('Day')
# plt.ylabel('Transport expenses in BRL')
# plt.legend()


# plt.show()
