# Steps
# 1-install mlxtend
# 2-import necessary libraries
# 3-display basic info
# 4-display histplot for Age and Estimeted salary
# 5-display boxplot for Age and Estimeted salary
# 6-diplay value counts and replace F and M with 0,1
# 7-create x and y, transform x
# 8-create LogisticRegression model, display y_pred and y_test
# 9-create and display confusion matrix
# 10-display TN, TP, FN, FP
# 11-display all types of score
# 12-display classiffication report


#pip install mlxtend


import sys
sys.version
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline


df = pd.read_csv("Social_Network_ads.csv")
df.shape
df.head()
df.info()
df.describe()
df.isna().sum()


histplot = sns.histplot(df['Age'], kde=True, bins=30, color='red', alpha=0.3)
for i in histplot.containers:
    histplot.bar_label(i)
plt.show()

histplot = sns.histplot(df['EstimatedSalary'],kde=True, bins=30, color="red", alpha=0.3)
for i in histplot.containers:
    histplot.bar_label(i)
plt.show()


plt.figure(figsize=(20,15))
plt.subplot(2,1,1)
sns.boxplot(data=df,x=df['Age'])
plt.subplot(2,1,2)
sns.boxplot(data=df,x=df['EstimatedSalary'])


df["Gender"].value_counts()
df["Purchased"].value_counts()
df['Gender'].replace(['Female','Male'],[0,1],inplace=True)
df.head()


countplot = sns.countplot(data=df, x="Purchased", hue="Gender", palette="twilight")
for i in countplot.containers:
    countplot.bar_label(i)
plt.show()

sns.heatmap(df.corr(),annot=True)
plt.show()


x = df[["Age","EstimatedSalary"]]
y = df["Purchased"]
scaler = StandardScaler()
x = scaler.fit_transform(x)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
y_pred
np.array(y_test)


cm = confusion_matrix(y_test,y_pred)
print(cm)
plot_confusion_matrix(conf_mat=cm, figsize=(5,5), show_normed=True)
plt.show()


print("TN:",cm[0][0])
print("FP:",cm[0][1])
print("FN:",cm[1][0])
print("TP:",cm[1][1])


print("Accuracy score: ",accuracy_score(y_test,y_pred))
print("Error rate: ",1-accuracy_score(y_test,y_pred))
print("Precision score: ",precision_score(y_test,y_pred))
print("Recall score: ",recall_score(y_test,y_pred))


print(classification_report(y_test,y_pred))



