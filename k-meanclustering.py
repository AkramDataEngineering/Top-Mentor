import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("🎯 K-Means Clustering (Easy Example)")

# Step 1: Sample Data
data = pd.DataFrame({
    'X': [1, 2, 8, 9, 10, 25],
    'Y': [2, 3, 8, 10, 11, 30]
})
st.write("📌 Input Data", data)

# Step 2: Apply KMeans
model = KMeans(n_clusters=3)
data['Cluster'] = model.fit_predict(data[['X', 'Y']])

# Step 3: Show Clustered Data
st.write("✅ Clustered Output", data)

# Step 4: Show Plot
fig, ax = plt.subplots()
colors = ['red', 'green', 'blue']
for cluster in range(3):
    clustered_points = data[data['Cluster'] == cluster]
    ax.scatter(clustered_points['X'], clustered_points['Y'], label=f"Cluster {cluster}", color=colors[cluster])
ax.set_xlabel("Math Marks (X)")
ax.set_ylabel("Science Marks (Y)")
ax.set_title("K-Means Clustering Output")
ax.legend()
st.pyplot(fig)