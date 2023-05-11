
# Plotting petal length vs width across the three Iris species.

import pandas as pd
import matplotlib.pyplot as plt

# Getting the data.
df = pd.read_csv('iris.csv')

# Obtaining the data for each of the three species.
setosa = df[df['variety'] == 'Setosa']
versicolor = df[df['variety'] == 'Versicolor']
virginica = df[df['variety'] == 'Virginica']

# Plotting the data.
plt.scatter(setosa['petal.length'], setosa['petal.width'])
plt.scatter(versicolor['petal.length'], versicolor['petal.width'])
plt.scatter(virginica['petal.length'], virginica['petal.width'])

plt.xlabel('petal length in cm')
plt.ylabel('petal width in cm')
plt.title('petal length vs width across three species')

plt.legend(['Setosa', 'Versicolor', 'Virginica'])

plt.show()
