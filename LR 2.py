
# Plotting sepal length against petal width for the three Iris species.

import pandas as pd
import matplotlib.pyplot as plt

# Getting the data.
df = pd.read_csv("iris.csv")

# Getting the features of each of the Iris flowers species.
setosa = df[df['variety']=='Setosa']
setosa = setosa.iloc[:,:-1]

versicolor = df[df['variety']=='Versicolor']
versicolor = versicolor.iloc[:,:-1]

virginica = df[df['variety']=='Virginica']
virginica = virginica.iloc[:,:-1]

# Plotting the desired features. Colors are used for each
# of the three Iris species.
plt.scatter(setosa['sepal.length'], setosa['petal.width'])
plt.scatter(versicolor['sepal.length'], versicolor['petal.width'])
plt.scatter(virginica['sepal.length'], virginica['petal.width'])

plt.xlabel('sepal length in cm')
plt.ylabel('petal width in cm')
plt.title('sepal length vs petal width across three species')

plt.legend(['Setosa', 'Versicolor', 'Virginica'])

plt.show()
