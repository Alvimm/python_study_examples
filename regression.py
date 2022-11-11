import matplotlib.pyplot as plt
import pandas
from sklearn.linear_model import LinearRegression

# Preprocessing
# Collection and Integration
file = pandas.read_csv('dengue_data.csv')

years = file[['years']]
cases = file[['cases']]

# Mineração
regr = LinearRegression()
regr.fit(X=years, y=cases)

future_year = [[2018]]
cases_2018 = regr.predict(future_year)

print('Predicted cases for 2018 ->', int(cases_2018))

# Post processing
plt.scatter(years, cases, color='black')
plt.scatter(future_year, cases_2018, color='red')
plt.plot(years, regr.predict(years), color='blue')

plt.xlabel('Years')
plt.ylabel('Dengue cases')
plt.xticks([2018])
plt.yticks([int(cases_2018)])

plt.show()
