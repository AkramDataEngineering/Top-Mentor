import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Linear Regression with Streamlit")

data = pd.read_csv("linear_regression.csv")
st.write(data)

x = data[['Hours_Studied']]
y = data['Marks_Scored']

first_model = LinearRegression()
first_model.fit(x, y)

hours = st.number_input("Enter Hours Studied:", 1.0, 20.0, step=0.5)
prediction = first_model.predict([[hours]])
st.write("Predicted Marks:", prediction[0])

#--------------------------------------------------------
st.title("Linear Regression with for House Price Prediction")

house_data = pd.read_csv("house_price.csv")
st.write(house_data)

a = house_data[['Area_in_Sqft']]
b = house_data['Price_in_Thousands']

second_model = LinearRegression()
second_model.fit(a, b)

price = st.number_input("Enter Hours Studied:", 1000.0, 20000.0, step=500.0)
Expected_price = second_model.predict([[price]])
st.write("House Price will be :", Expected_price[0])


#--------------------------------------------------------
st.title("Linear Regression with for Salary Prediction")

salary = pd.read_csv("salary.csv")
st.write(salary)

exp_age = salary[["Experience_in_Years","Age"]] # # features , independent variables
s = salary[['Salary_in_Thousands']] # target should be salary

third_model = LinearRegression()
third_model.fit(exp_age, s)

exp = st.number_input("Tell me your experience:", 0, 50, step=1)
age = st.number_input("May i Know you age:", 18, 100, step=1)

Expected_salary = third_model.predict([[exp, age]])
st.write("salary expected will be in Thousands:", Expected_salary[0])



#----------------------------------------------------------------------------------

#LOGICTICS REGRESSION
from sklearn.linear_model import LogisticRegression

st.title("Diabetes Prediction App")

data = pd.read_csv("patient_data.csv")
st.write(data)

x = data[['Age', 'Glucose_Level']]
y = data['Diabetes'].map({'No': 0, 'Yes': 1})

model = LogisticRegression()
model.fit(x, y)

age = st.number_input("Enter Age:", 18, 100, step=1)
glucose = st.number_input("Enter Glucose Level:", 50 300 step=20)

prediction = model.predict([[age, glucose]])[0]
result = "Yes" if prediction == 1 else "No"

st.write("The Patient have Diabatic? :", result)



#---------------------------------------------------------------------------
from sklearn.tree import DecisionTreeClassifier

st.title("Student Result Prediction App")s

data = pd.read_csv("student.csv")
st.write(data)

x = data[['Marks', 'Attendance']]
y = data['Result'].map({'Fail': 0, 'Pass': 1})

model = DecisionTreeClassifier()
model.fit(x, y)

marks = st.number_input("Enter Marks:", 0.0, 100.0, step=1.0)
attendance = st.number_input("Enter Attendance (%):", 0.0, 100.0, step=1.0)

prediction = model.predict([[marks, attendance]])[0]
result = "Pass" if prediction == 1 else "Fail"

st.write("Predicted Result:", result)