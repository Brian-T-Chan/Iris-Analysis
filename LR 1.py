
# Determine statistics for the features (sepal lengths, sepal widths, petal lengths, and petal widths) 
# of the three Iris flowers species.

import pandas as pd

# Getting the data.
df = pd.read_csv("iris.csv")

# Getting the features of each of the Iris flowers species.
setosa = df[df['variety']=='Setosa']
setosa = setosa.iloc[:,:-1]

versicolor = df[df['variety']=='Versicolor']
versicolor = versicolor.iloc[:,:-1]

virginica = df[df['variety']=='Virginica']
virginica = virginica.iloc[:,:-1]

# Determine the statistics.
print('Setosa:')
print(setosa.describe(), '\n')

print('Versicolor:')
print(versicolor.describe(), '\n')

print('Virginica:')
print(virginica.describe(), '\n')
