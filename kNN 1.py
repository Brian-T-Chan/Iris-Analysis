
# Make a prediction on the type of iris flower being viewed using kNN.

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

# Getting the data.
df = pd.read_csv("iris.csv")

# Getting the features and labels.
X = df.iloc[:,:-1].to_numpy()
y = df.iloc[:,-1].to_numpy()

# Numerically encode target labels.
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, train_size=0.7)

# Create and train the kNN classifier with k = 5
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# Make the prediction by decoding target labels.
prediction = le.inverse_transform(classifier.predict(X_test))
print(prediction)

