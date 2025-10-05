import streamlit as st
import pandas as pd
from sklearn.svm import SVC

st.title("Disease Detection Using SVM")

data = pd.read_csv("Healthdata.csv")
st.write(data)

x = data[['Temperature', 'Heart_Rate']]
y = data['Disease'].map({'No': 0, 'Yes': 1})

model = SVC()
model.fit(x, y)

temp = st.number_input("Enter Body Temperature:", 95.0, 105.0, step=0.5)
hr = st.number_input("Enter Heart Rate:", 60.0, 120.0, step=1.0)

prediction = model.predict([[temp, hr]])[0]
result = "Yes" if prediction == 1 else "No"

st.write("Disease Detected:", result)