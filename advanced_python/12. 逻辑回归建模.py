from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go
from sklearn.decomposition import PCA
from plotly.offline import iplot
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import warnings
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
#数据读入
filename='/Users/zhoujie/Desktop/test_merge/merged.csv'
data = pd.read_csv(filename)
print(data.isnull().sum()/len(data)*100)
print(data.var())


# print(data.head())
####这个是announce/declare数量分布饼图
labels = data.groupby('target_word').size().index
values = data.groupby('target_word').size()
trace = go.Pie(labels=labels, values=values)
layout = go.Layout(width=350, height=350)
fig = go.Figure(data=[trace], layout=layout)
iplot(fig)

#####特征分布bar图
# groups = data.groupby(by = "target_word")
# means, sds = groups.mean(), groups.std()
# means.plot(yerr = sds, kind = 'bar', figsize = (9, 5), table = True)
# plt.show()

#数据准备
X_data = data.drop(['target_word'],axis=1)
print(X_data.head())
y_data = np.ravel(data[['target_word']])
print(X_data.corr())
#
# ###划分数据集
#
X_train,X_test,y_train,y_test = train_test_split(X_data,y_data,test_size=0.2,random_state=0)
# print(X_train)
# print(X_test.shape)
# print(y_train)
#
# ### 建模
lr = LogisticRegression(penalty='l2')
# lr.fit(X_train,y_train)
# lr.predict(X_test)
rfe = RFE(lr, n_features_to_select=10)
rfe = rfe.fit(X_data, data.target_word)
rfe.ranking_

####feature importance ranking   feature排序：NER%<sent_type<NER<ADV<Adj<Adv%<number_token<Adj%<genre<mean_len_token<sent_score
model = RandomForestRegressor(random_state=1, max_depth=10)
df=pd.get_dummies(X_data)
model.fit(df,data.target_word)
features = df.columns
importances = model.feature_importances_
indices = np.argsort(importances[0:10])  # top 10 features
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()



#输出模型系数
# print('训练模型自变量参数为：',lr.coef_)
# print('训练模型截距为：',lr.intercept_)
# #模型评价
# print('模型的平均正确率为：',lr.score(X_test,y_test))

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()#实例化逻辑回归模型
model.fit(X_train, y_train)#训练模型
predictions = model.predict(X_test)#在测试集上预测
# print(classification_report(y_test, predictions))#输出模型的精度指标表


y_hat = lr.predict(X_test)
probability = lr.predict_proba(X_test)

# 产生序号，用于可视化的横坐标。
# index = np.arange(len(X_test))
# pro_0 = probability[:, 0]
# pro_1 = probability[:, 1]
# tick_label = np.where(y_test == y_hat, "O", "X")
# plt.figure(figsize=(15, 5))
# # 绘制堆叠图
# plt.bar(index, height=pro_0, color="g", label="Announce")
# # bottom=x，表示从x的值开始堆叠上去。
# # tick_label 设置标签刻度的文本内容。
# plt.bar(index, height=pro_1, color='r', bottom=pro_0, label="Declare", tick_label=tick_label)
# plt.legend(loc="best", bbox_to_anchor=(1, 1))
# plt.xlabel("Index")
# plt.ylabel("Probability")
# plt.title("Logistic Regression")
# plt.show()

import seaborn as sns
from sklearn.metrics import roc_curve, roc_auc_score#调用ROC,AUC函数
Y_scores = lr.predict_proba(X_test)#返回测试集上预测值属于某标签的概率
#计算参数，绘制ROC曲线
# fpr, tpr, thresholds = roc_curve(y_test, Y_scores[:,1])
# sns.lineplot([0, 1], [0, 1])
# sns.lineplot(fpr, tpr)
# plt.show()
#计算AUC值
auc = roc_auc_score(y_test,Y_scores[:,1])
print("AUC:",auc)
