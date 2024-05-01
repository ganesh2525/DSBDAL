# 1-Import necessary libraries
# 2-Print Basic Info and remove null values from Age column
# 3-Write Fun1 and Fun2 and apply it to respective colmns
# 4-Drop cabin column and draw boxplot

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

def fun1(value):
    if(value=="male"):
        return 1
    else:
        return 0
    
def fun2(value):
    if(value=='S'):
        return 0
    elif (value=='C'):
        return 1
    elif (value=='Q'):
        return 2
    else:
        return 0

df["Sex"] = df["Sex"].apply(fun1)
df["Embarked"] = df["Embarked"].apply(fun2)

df = df.drop("Cabin",axis=1)
df.shape
sns.boxplot(x="Sex",y="Age",hue="Survived",data=df)