import numpy as np
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("student_performance_2.csv")
df.isnull()
df.notnull()
df.isnull().sum()
df.isnull().sum().sum()

pd.set_option('display.max_rows', None)
df["Math Score"]

d1 = df["Math Score"].copy()
d1 = d1.fillna(method="pad")
d1

d2 = df["Math Score"].copy()
d2 = d2.fillna(method="bfill")
d2

d3 = df["Math Score"].copy()
d3 = d3.interpolate(method="linear",limit_direction="forward")
d3

d4 = df['Math Score'].copy()
d4 = d4.dropna()
d4

df['Math Score'] = df['Math Score'].fillna(df['Math Score'].mean())
df.isnull().sum()
df['Reading Score'] = df['Reading Score'].fillna(df['Reading Score'].median())
df.isnull().sum()
df['Writing Score'] = df['Writing Score'].fillna(df['Writing Score'].min())
df.isnull().sum()

from numpy.random import seed, randn
from numpy import mean, std

seed(1) # the same set of random numbers will be generated every time the code is run.
data = 5*randn(10000)+50 # generates a dataset of 10,000 random numbers sampled from a normal distribution with a mean of 50 and a standard deviation of 5.
data

sns.boxplot(x=data, orient='h')

data_mean = mean(data)
data_std = std(data)
cut_off = data_std*3
lower = data_mean-cut_off
upper = data_mean+ cut_off

outliers_removed=[x for x in data if lower<=x or x<=upper]
outliers_removed


df.shape
sns.histplot(df["Math Score"])

def remove_outliers(df,feature):
    q3 , q1 = np.percentile( df[feature] , [ 75 , 25 ] )
    iqr = q3 - q1
    dt = df[ (df[feature] >= q1 - 1.5 * iqr) & (df[feature] <= q3 + 1.5 * iqr) ]
    return dt
    
dt = remove_outliers(df,"Math Score" )

dt.shape
sns.histplot(dt["Math Score"])

# Identifying outliers using z-score
plt.scatter(df.index+1,df['Reading Score'], color='red')

outliers = df[(np.abs(df["Reading Score"] - df["Reading Score"].mean()) > (3 * df["Reading Score"].std()))]
print(outliers)

plt.scatter(outliers.index + 1, outliers['Reading Score'], color='red', label='Outliers')

cleaned_df = df.drop(outliers.index)
print(cleaned_df)

plt.scatter(cleaned_df.index + 1, cleaned_df['Reading Score'], color='red', label='Cleaned Data')


df[['Math Score','Reading Score','Writing Score']]
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
df[['Math Score','Reading Score','Writing Score']]=mms.fit_transform(df[['Math Score','Reading Score','Writing Score']])
df[['Math Score','Reading Score','Writing Score']]


rollno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
name = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", np.nan, np.nan, "k", "l", "m"]
marks = [40, 23, 50, 78, 48, 89, 90, 67, 84, 96, 76, np.nan, 97, np.nan, 65]
grade = ["F", "F", "P", "P", "P", "P", "P", "P", "P", "P", "P", "F", "P", np.nan, np.nan]

df = pd.DataFrame({"rollno" : rollno, "name" : name, "marks" : marks, "grade" : grade})

df