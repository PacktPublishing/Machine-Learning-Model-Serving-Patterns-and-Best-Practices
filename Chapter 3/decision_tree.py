from sklearn import tree
import matplotlib.pyplot as plt
X = [[0, 0, 2], [1, 1, 3], [3, 1, 3]]
Y = [0, 1, 2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[3, 1, 6]]))
print(clf.predict([[1, 1, 6]]))
print(clf.decision_path([[3, 1, 6], [1, 1, 6]]))
tree.plot_tree(clf)
plt.show()
