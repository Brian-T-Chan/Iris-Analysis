
# Plotting sepal length vs width across the three Iris species.

import pandas as pd
import matplotlib.pyplot as plt

# Getting the data.
df = pd.read_csv('iris.csv')

# Obtaining the data for each of the three species.
setosa = df[df['variety'] == 'Setosa']
versicolor = df[df['variety'] == 'Versicolor']
virginica = df[df['variety'] == 'Virginica']

# Plotting the data.
plt.scatter(setosa['sepal.length'], setosa['sepal.width'])
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'])
plt.scatter(virginica['sepal.length'], virginica['sepal.width'])

plt.xlabel('sepal length in cm')
plt.ylabel('sepal width in cm')
plt.title('sepal length vs width across three species')

plt.legend(['Setosa', 'Versicolor', 'Virginica'])

plt.savefig('graph.png')
