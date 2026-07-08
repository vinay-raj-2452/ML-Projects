# ==========================================
# Fabric Consumption Prediction Model
# ==========================================

# Import Libraries
import numpy as np
import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================
# Load Dataset
# ==========================================

dataset = pd.read_csv(r"C:\Users\laksh\Downloads\FSDS\fabric_consumption_dataset_1000.csv")


# ==========================================
# Define Independent Variable (X)
# ==========================================

X = dataset[['Number_of_Garments']].values

# ==========================================
# Define Dependent Variable (y)
# ==========================================

y = dataset['Fabric_Required_kg'].values

# ==========================================
# Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

print("\nTraining Data Shape :", X_train.shape)
print("Testing Data Shape  :", X_test.shape)

# ==========================================
# Train Linear Regression Model
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)

# ==========================================
# Predict Test Data
# ==========================================

y_pred = model.predict(X_test)

# ==========================================
# Model Parameters
# ==========================================

print("\nCoefficient (Slope)")
print(model.coef_)

print("\nIntercept")
print(model.intercept_)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n" + "=" * 50)
print("ERROR METRICS")
print("=" * 50)

print("\nMean Absolute Error (MAE)")
print(round(mae, 4))

print("\nMean Squared Error (MSE)")
print(round(mse, 4))

print("\nRoot Mean Squared Error (RMSE)")
print(round(rmse, 4))

print("\nR² Score")
print(round(r2_score(y_test, y_pred), 2))

# ==========================================
# Save Model using Pickle
# ==========================================

with open("fabric_model.pkl", "wb") as file:
    pickle.dump(model, file)

# ==========================================
# Verify Model Saved
# ==========================================

print("\n" + "=" * 50)

if os.path.exists("fabric_model.pkl"):
    print("Model Saved Successfully!")
    print("File Name : fabric_model.pkl")
else:
    print("Model Saving Failed!")

print("=" * 50)