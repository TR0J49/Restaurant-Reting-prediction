# -*- coding: utf-8 -*-
"""rating of a restaurant

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H2kvOPM4QWpU_ppifH-fNnWvczKAG1MT
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

data = pd.read_csv('/content/Dataset .csv')

"""# Data Preprocess

"""

data.head()

data.tail()

data.shape

data.info()

data.isnull().sum()

data.describe()

numeric_data = data.select_dtypes(include='number')


correlation_train = numeric_data.corr()
print("Correlation Matrix for Training Data:")
print(correlation_train)


numeric_data = data.select_dtypes(include='number')


correlation_test = numeric_data.corr()
print("\nCorrelation Matrix for Test Data:")
print(correlation_test)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_train, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap for Training Data')
plt.show()

"""# Data Visualization"""

numerical_columns = ['Restaurant ID', 'Country Code', 'Longitude', 'Latitude',
                     'Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_columns, 1):
    plt.subplot(2, 4, i)
    sns.histplot(data[col], kde=True, color='blue', bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt


columns = ['Restaurant ID', 'Country Code', 'Longitude', 'Latitude',
                     'Average Cost for two', 'Price range', 'Aggregate rating', 'Votes']


fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(20, 20))
fig.subplots_adjust(hspace=0.5)


for col, ax in zip(columns, axes.flatten()):
    if col in data.columns:
        if data[col].dtype == 'object':
            sns.countplot(x=col, data=data, ax=ax)
            ax.set_title(f'Distribution of {col}')
            ax.set_xlabel(col)
            ax.set_ylabel('Count')
            ax.tick_params(axis='x', rotation=45)
        else:
            sns.histplot(x=data[col], ax=ax, kde=True, color='skyblue')
            ax.set_title(f'Distribution of {col}')
            ax.set_xlabel(col)
            ax.set_ylabel('Frequency')

#
for i in range(len(columns), len(axes.flatten())):
    fig.delaxes(axes.flatten()[i])

plt.tight_layout()
plt.show()

"""# Machine  Learning Deployment"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

X = data[['Average Cost for two', 'Price range', 'Votes']]  # Example features
y = data['Aggregate rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

"""# Linear Regression"""

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='green', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Actual vs Predicted Ratings (Linear Regression)')
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.show()

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""# Random Forest"""

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)  # Using 100 decision trees
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

print(y_pred_rf)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, color='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Actual vs Predicted Ratings (Random Forest)')
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.show()

mse_rf = mean_squared_error(y_test, y_pred_rf)
print("Random Forest Mean Squared Error:", mse_rf)

"""# KNN K-Nearest Neighbors"""

from sklearn.neighbors import KNeighborsRegressor

knn_model = KNeighborsRegressor(n_neighbors=5)  # Using 5 nearest neighbors
knn_model.fit(X_train, y_train)

y_pred_knn = knn_model.predict(X_test)

print(y_pred_knn)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_knn, color='orange', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Actual vs Predicted Ratings (KNN Regression)')
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.show()

mse_knn = mean_squared_error(y_test, y_pred_knn)
print("KNN Mean Squared Error:", mse_knn)

average_cost = float(input("Enter the average cost for two: "))
price_range = int(input("Enter the price range (1-4): "))
votes = int(input("Enter the number of votes: "))

# Make prediction using the trained model
input_features = [[average_cost, price_range, votes]]
predicted_rating = knn_model.predict(input_features)

print("Predicted Rating:", predicted_rating[0])