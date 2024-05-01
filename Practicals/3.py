import pandas as pd
from sklearn.datasets import load_iris
import warnings 
warnings.filterwarnings("ignore")

df = pd.read_csv("nba.csv")
df.shape
df.head()
df.info()
df.describe()
df.isna().sum()

df["Salary"].fillna(df["Salary"].mean(),inplace=True)
df["Age"].fillna(df["Age"].mean(),inplace=True)
df[["Salary","Age"]]

dk=df.groupby('Age')
dk['Salary'].mean()
dk['Weight'].median()

bins=[19,25,30,35,40]
label=['19-25','26-30','31-35','36-40']
df['Age Group']=pd.cut(df['Age'],bins=bins,labels=label)
df

df['Age Group'].value_counts()
df.groupby('Age Group')['Salary'].describe()
df.groupby('Age Group').get_group('19-25')

grouping=df.groupby(['Age','Weight','Salary'])
grouping.first()

grouping = df.groupby("Age").agg({"Weight":list,"Salary":"mean"})
grouping

mini = df.groupby('Age')['Salary'].min()
print(mini)

maxi = df.groupby('Age')['Salary'].max()
print(maxi)

sd = df.groupby('Age')['Salary'].std()
print(sd)

df = pd.read_csv("iris.csv")

iris = load_iris()
iris.keys()

iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df["label"] = iris.target

iris.target_names
iris_df.shape

iris_df.head()
iris_df.info()
iris_df.describe()

setosa = iris_df[iris_df["label"] == 0].drop("label", axis=1)
setosa.describe()

versicolor = iris_df[iris_df["label"] == 1].drop("label", axis=1)
versicolor.describe()

virginica = iris_df[iris_df["label"] == 2].drop("label", axis=1)
virginica.describe()