# Steps
# 1-install mlxtend
# 2-import necessary libraries
# 3-load datset, create x and y and display basic info
# 4-transform x
# 5-create GaussianNB model, display y_pred and y_test
# 6-create and display confusion matrix
# 7-display TN, TP, FN, FP
# 8-display all types of score
# 9-display classiffication report

# pip install mlxtend

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB  
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

iris = load_iris()
iris.keys()

x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
y = pd.DataFrame(iris['target'], columns=['target'])
x
y
x.info()
y.info()
x.describe()
y.describe()

scaler = StandardScaler()
x = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=62)
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred


cm = confusion_matrix(y_test,y_pred)
print(cm)
plot_confusion_matrix(conf_mat=cm,figsize=(5,5),show_normed=True)
plt.show()


print("TP:",cm[0,0])
print("TN:",cm[1,1]+cm[2,2])
print("FP:",cm[0,1]+cm[0,2])
print("FN:",cm[1,0]+cm[2,0])


print("Accuracy: ",accuracy_score(y_test,y_pred))
print("Error: ",1-accuracy_score(y_test,y_pred))
print("Precision Score: ",precision_score(y_test,y_pred,average='macro'))
print("Recall Score: ",recall_score(y_test,y_pred,average='macro'))

print(classification_report(y_test,y_pred))


