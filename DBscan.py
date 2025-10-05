from sklearn.cluster import DBSCAN
import numpy as np
import streamlit as st

# Coordinates of 6 points
X = np.array([
    [1, 2], [2, 2], [2, 3],   # Close together (Cluster 0)
    [8, 7], [8, 8],           # Another group (Cluster 1)
    [25, 80]                  # Far away (Noise)
])

# Apply DBSCAN
model = DBSCAN(eps=3, min_samples=2)
model.fit(X)

# Show which point is in which cluster
st.write("Labels:", model.labels_)