from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
import pickle
import sys

X, y = load_iris(return_X_y=True)
print("Original data dimensions:", X.shape)
phase_one_model = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)
score = phase_one_model.score(X, y)
print("Accuracy of the phase two model:", score)
p = pickle.dumps(phase_one_model)
print("Size of the phase two model in bytes:", sys.getsizeof(p))


X_new = SelectKBest(chi2, k=1).fit_transform(X, y)
print("Data dimensions after feature reduction:", X_new.shape)
phase_two_model = LogisticRegression(random_state=0, max_iter=1000).fit(X_new, y)
score = phase_two_model.score(X_new, y)
print("Accuracy of the phase one model: ", score)
p = pickle.dumps(phase_two_model)
print("Size of the phase one model in bytes:", sys.getsizeof(p))
