import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures
import warnings
import seaborn as sns
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib as mpl

warnings.filterwarnings(action='ignore')

data = pd.read_csv("/Users/zhoujie/Desktop/test_merge/merged.csv")
X_data = data.drop(['target_word'],axis=1)
print(X_data.head())
y_data = np.ravel(data[['target_word']])
X_train,X_test,y_train,y_test = train_test_split(X_data,y_data,test_size=0.2,random_state=0)

ss = StandardScaler()
ss.fit(X_train, X_test)
X_train_std = ss.transform(X_train)
X_test_std = ss.transform(X_test)
print(X_train_std.shape)
print(X_test_std.shape)


lr = LogisticRegression()
scores = cross_val_score(lr, X_train_std, y_train, cv=10, scoring='neg_mean_squared_error')
# print(scores.mean())
lr.fit(X_train_std, y_train)
print(lr.score(X_train_std, y_train))
print(lr.score(X_test_std, y_test))


for i in range(1, 9):
    pf = PolynomialFeatures(degree=i, interaction_only = True)
    X_train_std_pf = pf.fit_transform(X_train_std)
    X_test_std_pf = pf.transform(X_test_std)
    score = cross_val_score(lr, X_train_std_pf, y_train, cv=10, scoring='neg_mean_squared_error')
    print(scores.mean())
    lr.fit(X_train_std_pf, y_train)
    print(lr.score(X_train_std_pf, y_train))
    print(lr.score(X_test_std_pf, y_test))
    Y_scores = lr.predict_proba(X_test_std_pf)
    # fpr, tpr, thresholds = roc_curve(y_test, Y_scores[:, 1])
    # sns.lineplot([0, 1], [0, 1])
    # sns.lineplot(fpr, tpr)
    # plt.show()
    # 计算AUC值
    auc = roc_auc_score(y_test, Y_scores[:, 1])
    print("AUC:", auc)

pf = PolynomialFeatures(degree=2, interaction_only = True)
X_train_std_pf = pf.fit_transform(X_train_std)
X_test_std_pf = pf.transform(X_test_std)
lr.fit(X_train_std_pf, y_train)
print(lr.score(X_train_std_pf, y_train))
print(lr.score(X_test_std_pf, y_test))
y_ev_pred = lr.predict(X_test_std_pf)
print(y_ev_pred)

# mpl.rcParams['font.sans-serif'] = [u'simHei']
# mpl.rcParams['axes.unicode_minus'] = False
# t = np.arange(len(y_test))  # 样本编号
# fig = plt.figure(facecolor='w')
# fig.subplots()
# plt.plot(t, y_test, 'r-', lw=2, label=u'Real')
# plt.plot(t, y_ev_pred, 'b-', lw=2, label=u'Prediction')
# plt.legend(loc='best')
# plt.title('Announce/Declare', fontsize=18)
# plt.xlabel('Index', fontsize=15)
# plt.ylabel('Prediction', fontsize=15)
# plt.grid()
# plt.show()


sns.pairplot(data, hue='target_word')
plt.show()

