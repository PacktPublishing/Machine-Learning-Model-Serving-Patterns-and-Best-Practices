from sklearn import svm, datasets
from sklearn.model_selection import cross_val_score
X, y = datasets.load_iris(return_X_y=True)
clf = svm.SVC(random_state=0)
print(clf.fit(X,y))
score = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print(score)
