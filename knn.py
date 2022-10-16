from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import Perceptron
import pickle

data = pd.read_csv('data.csv')
X = data.iloc[:, :14]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
#KNN
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train)
pickle.dump(neigh, open('KNN_Model.pkl', 'wb'))
print(type(X_test))
y_pred = neigh.predict(X_test)

print("For KNN, Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))

#Perceptron
clf = Perceptron(tol=1e-3, random_state=0)
clf.fit(X_train, y_train)
pickle.dump(clf, open('Perceptron.pkl', 'wb'))
y_pred = clf.predict(X_test)

print("For Perceptron, Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))