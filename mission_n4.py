import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ***************************** ENTRADA DOS DADOS ***************************
file = pd.read_csv('expenses_data.csv')
day = file['day'].values
alimentation_exp = file['alimentation'].values
clothing_exp = file['clothing'].values
transport_exp = file['transport'].values

# ***************************** SÉRIES TEMPORAIS ****************************


class Time_series():
    def show_ts(self, x, y, z):
        plt.plot(day, x, '-o', color='green', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)  # noqa
        plt.plot(day, y, '-o', color='yellow', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)  # noqa
        plt.plot(day, z, '-o', color='black', linewidth=3,
                 markerfacecolor='blue', markeredgecolor='blue', markeredgewidth=4)  # noqa
        plt.legend(['Alimentation', 'Clothing', 'Transport'])
        plt.xlabel('Day')
        plt.ylabel('Expenses in BRL')
        plt.title('Expense graphs')
        plt.show()

# ***************************** REGRESSÃO LINEAR *****************************


class Linear_regr():
    def show_graphs(self, type, name_text, color):
        global day, regr, line
        day = np.array(day).reshape(-1, 1)
        regr = LinearRegression().fit(day, type)
        line = regr.coef_[0] * day + regr.intercept_
        plt.plot(day, line, label='Linear regression', c='blue')
        plt.plot(day, type, '-o', label=f'{name_text} - original', linewidth=3,
                 markerfacecolor='black', markeredgecolor='black', markeredgewidth=4, c=f'{color}')  # noqa
        plt.xlabel('Day')
        plt.ylabel(f'{name_text} expenses in BRL')
        plt.legend()
        plt.show()


# ******************** SAÍDA(APRESENTAÇÃO) DOS DADOS ************************
t_series = Time_series()
t_series.show_ts(alimentation_exp, clothing_exp, transport_exp)
l_regr = Linear_regr()
l_regr.show_graphs(alimentation_exp, 'Alimentation', 'green')
l_regr.show_graphs(clothing_exp, 'Clothing', 'yellow')
l_regr.show_graphs(transport_exp, 'Transport', 'black')
