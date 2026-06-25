import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load clean data
data = pd.read_csv('clean_data.csv')

# X = input, y = what we predict
X = data[['Temperature', 'Precipitation']]
y = data['Water_Level']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Check accuracy
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score:.2f}")

# Save model
pickle.dump(model, open('water_model.pkl', 'wb'))
print("Model saved successfully!")