
# Plotting four histograms for petal lengths, petal widths,
# sepal lengths, and sepal widths.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
fig, ax = plt.subplots(2, 2)

ax[0, 0].hist(df['petal.length'], ec='black')
ax[0, 0].set_title("Petal Length in cm")

ax[0, 1].hist(df['petal.width'], ec='black')
ax[0, 1].set_title("Petal Width in cm")

ax[1, 0].hist(df['sepal.length'], ec='black')
ax[1, 0].set_title("Sepal Length in cm")

ax[1, 1].hist(df['sepal.width'], ec='black')
ax[1, 1].set_title("Sepal Width in cm")

fig.tight_layout(pad=1.5)

plt.show()


