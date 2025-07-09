import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
data = pd.read_csv('sleep_quality_data.csv')  # Use relative path

# Select only the relevant columns
columns_to_use = [
    "Sleep Duration (hrs)",
    "Caffeine Intake (cups)",
    "Stress Level (1-10)",
    "Physical Activity (steps)",
    "Mood (1-10)",
    "Environmental Factors (Temp°C)"
]
target_column = "Sleep Quality (1-10)"

# Prepare features and target variable
X = data[columns_to_use]
y = data[target_column]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train a Random Forest model
best_rf_model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
best_rf_model.fit(X_train, y_train)

# Evaluate the model
y_pred = best_rf_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save the trained model and scaler
joblib.dump(best_rf_model, 'best_rf_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Model and scaler saved successfully!")
