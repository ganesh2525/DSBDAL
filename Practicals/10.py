# 1-Import necessary libraries
# 2-Print Basic Info
# 3-Heatmap
# 4-Histplot for each
# 5-Boxplot for each
# 6-Overall Boaxplot

# pip install --upgrade setuptools wheel
# pip install scikit-learn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
data.keys()

df = pd.DataFrame(data.data, columns=data.feature_names)
df['label'] = data.target
df.head()

df = pd.DataFrame()
df[data['feature_names']] = data['data']
df['label'] = data['target']
df.head()

df.shape
df.info()
df.describe()

sns.heatmap(df.corr(),annot=True)

sns.histplot(df["sepal length (cm)"],kde=True)
sns.histplot(df["sepal width (cm)"],kde=True)
sns.histplot(df["petal length (cm)"],kde=True)
sns.histplot(df["petal width (cm)"],kde=True)

sns.boxplot(x=df['label'], y=df["sepal length (cm)"])
sns.boxplot(x=df['label'], y=df["sepal width (cm)"])
sns.boxplot(x=df['label'], y=df["petal length (cm)"])
sns.boxplot(x=df['label'], y=df["petal width (cm)"])

plt.figure(figsize=(12,6))
sns.boxplot(data=df.drop(columns='label'),orient='h')
plt.title("Box plot of features")
plt.xlabel("Value")
plt.ylabel("Features")
plt.show()