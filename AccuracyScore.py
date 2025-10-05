import streamlit as st
from sklearn.metrics import accuracy_score

st.title("📊 Accuracy Score Example")

# Predefined labels
y_true = [1, 0, 1, 1, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1]

# Show data
st.write("✅ Actual Labels:", y_true)
st.write("📌 Predicted Labels:", y_pred)

# Calculate accuracy
acc = accuracy_score(y_true, y_pred)
st.success(f"🎯 Accuracy Score: {acc:.2f}")