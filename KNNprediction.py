import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

st.title("Fruit Classification with KNN")

data = pd.read_csv("fruitdata.csv")
st.write(data)

x = data[['Size', 'Weight']]
y = data['Fruit']

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

size = st.number_input("Enter Fruit Size:", 1.0, 15.0, step=0.5)
weight = st.number_input("Enter Fruit Weight (grams):", 50.0, 300.0, step=10.0)

prediction = model.predict([[size, weight]])[0]
st.write("Predicted Fruit Type:", prediction)