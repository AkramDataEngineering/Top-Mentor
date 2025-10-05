import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

st.title("Train-Test Split with Linear Regression")

# Sample data
data = pd.DataFrame({
    'Area': [1000, 1200, 1500, 1800, 2000, 2200],
    'Price': [150, 180, 220, 260, 300, 330]
})

# Split into X and y
X = data[['Area']]
y = data['Price']

# Split using train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Output
st.write("✅ Training Data", X_train)
st.write("✅ Testing Data", X_test)
st.write("✅ Predicted Prices", y_pred)