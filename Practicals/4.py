# 1-Import necessary libraries and read dataset
# 2-Fill null values in age column with mean and remove null values columns
# 3-Create correlation matrix
# 4-Create x (without MEDV) and y (MEDV) and also xTrain,xTest,yTrain,yTest
# 5-Create LinearRegression model, train the model, Predict value
# 6-Draw actual VS predicted
# 7-Check Accuracy, intercept and slope
# 8-Calculate MSE, RMSE

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("HousingData.csv")

meanAge = df['AGE'].mean().astype(int)
df["AGE"].fillna(meanAge,inplace=True)
df = df.dropna()
df

corrMat = df.corr()
plt.figure(figsize=(12,12))
sns.heatmap(corrMat,annot=True,cmap="coolwarm",linecolor="black",linewidth=0.5)

x = df.drop(columns=['MEDV'])
y = df['MEDV']
xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(xTrain,yTrain)
yPred = model.predict(xTest)

plt.scatter(yTest,yPred,label="Actual vs Predicted")
plt.plot([min(yTest), max(yTest)],[min(yTest), max(yTest)], linestyle='-', color='blue', linewidth=1, label='y=x')
plt.xlabel("Observed Prices")
plt.ylabel("Predicted Prices")
plt.title("Observed Prices vs Predicted Prices")
plt.show()

r_squared = model.score(xTest,yTest)
print("R-squared Score: ",r_squared*100)
print("Intercept: ",model.intercept_)
print("Slope: ",model.coef_[0])

residuals = yPred - yTest
squared_residuals = residuals**2
mse = np.mean(squared_residuals)
print("Mean Squared Error: ",mse)
rmse = np.sqrt(mse)
print("Root Mean Squared Error: ",rmse)