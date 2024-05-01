import numpy as np
import pandas as pd

df = pd.read_csv("student_performance_2.csv")


df.isnull()
df.isnull().sum()
df.isnull().sum().sum()


df.dtypes
df['Age'] = df['Age'].astype('float')
df.dtypes
df['Age'] = df['Age'].astype('int64')
df.dtypes


df.head()
df.tail()
df.info()
df.describe()
df.shape


df.count()
df['Age'].value_counts()
df['Gender'].unique()


def min_max_normalize(name: str):
    df[ name ] = (df[ name ] - df[ name ].min()) / ( df[ name ].max() - df[ name ].min() )

min_max_normalize( "Age" )
df["Age"]

df.loc[ df.Gender == "Male" , "Gender" ] = 0
df.loc[ df.Gender == "Female" , "Gender" ] = 1
df["Gender"]

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['School'] = label_encoder.fit_transform(df['School'])
df["School"]