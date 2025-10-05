import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title("Loan Approval Prediction")

data = pd.read_csv("LoanData.csv")
st.write(data)

x = data[['Income', 'Credit_Score']]
y = data['Loan_Approved'].map({'No': 0, 'Yes': 1})

model = RandomForestClassifier()
model.fit(x, y)

income = st.number_input("Enter Monthly Income:", 1000, 100000, step=1000)
credit = st.number_input("Enter Credit Score:", 300, 850, step=10)

prediction = model.predict([[income, credit]])[0]
result = "Yes" if prediction == 1 else "No"

st.write("Loan Approved:", result)