import sklearn

from sklearn import tree  # 引入tree模型


# 决策树分类
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()  # 引入模型
clf = clf.fit(X, Y)  # 训练模型


