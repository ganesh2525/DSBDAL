# 1-Import necessary libraries
# 2-Print Basic Info and remove null values from Age column
# 3-countplot, boxplot, jointplot, boxplot, boxplot, boxplot, scatterplot,  histplot, histplot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic_data.csv")
df.shape
df.head()
df.info()
df.describe()
df.isna().sum()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df.isna().sum()

sns.countplot(x="Survived",data=df)
sns.boxplot(x="Survived",y="Age",data=df)
sns.jointplot(x="Survived",y="Fare",kind="scatter",data=df)

sns.boxplot(x="Pclass",y="Age",data=df)
sns.boxplot(x="Pclass",y="Age",hue="Survived",data=df)

sns.histplot(x="Fare",data=df)
sns.histplot(x='Fare',bins=20,kde=True,data=df)
sns.scatterplot(x="Fare",y="Age",hue="Survived",data=df)



