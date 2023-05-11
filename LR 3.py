
import pandas as pd

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Getting the data.
df = pd.read_csv("iris.csv")

# Get the sepal lengths and petal widths of all the Irises
# and their corresponding labels (Setosha, Versicolor, and Virginica).
X = df[['sepal.length', 'petal.width']]
y = df['variety']

# Numerically encode target labels.
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, train_size=0.7)

# Create and train the Logistic Regression classifier.
clf = LogisticRegression(multi_class='multinomial')
clf.fit(X_train, y_train)

# Make predictions.
y_pred = clf.predict(X_test)

# Determine accuracy of Logistic Regression classifier.
accuracy = accuracy_score(y_test, y_pred)

# Display predictions by decoding target labels and the accuracy.
print("\nPredictions: ", le.inverse_transform(y_pred))
print("\nAccuracy: ", accuracy)


