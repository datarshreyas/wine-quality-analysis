import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("winequality.csv")

# Drop unnecessary column
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)

# Basic info
print(df.head())
print(df.info())

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Quality distribution
sns.countplot(x='quality', data=df)
plt.title("Wine Quality Distribution")
plt.show()

# Key relationships
sns.scatterplot(x='alcohol', y='quality', data=df)
plt.title("Alcohol vs Quality")
plt.show()

sns.scatterplot(x='volatile acidity', y='quality', data=df)
plt.title("Volatile Acidity vs Quality")
plt.show()

# Group insights
quality_avg = df.groupby('quality').mean()
print("\nAverage feature values by quality:\n", quality_avg)

# Simple classification (bonus)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("\nModel Accuracy:", model.score(X_test, y_test))
