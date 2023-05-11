
# Plotting the accuracy of the kNN classifier with varying values of k.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

# Getting the data.
df = pd.read_csv("iris.csv")

# Getting the features and labels.
X = df.iloc[:,:-1].to_numpy()
y = df.iloc[:,-1].to_numpy()

# Numerically encode target labels.
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8)

results = []

# Train and predict accuracies of kNN classifiers for k ranging from 1 to 50.
for k in range(1, 51):

    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    results.append(accuracy_score(y_test, y_pred))

# Plot the results.
plt.plot(range(1, 51), results, marker = 'o')

plt.xlabel('k')
plt.ylabel('accuracy')
plt.title('accuracy vs k')

plt.savefig('graph.png')

