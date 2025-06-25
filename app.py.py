import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Contoh data, bisa diganti dengan data Anda sendiri
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55],
    'Experience': [1, 6, 11, 16, 21, 26, 31],
    'Income': [30000, 40000, 50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)

# Fitur & label
X = df[['Age', 'Experience']]
y = df[['Income']]

# Training model
model = LinearRegression()
model.fit(X, y)

# Simpan model
joblib.dump(model, 'model_income.pkl')
print("Model saved as model_income.pkl")
