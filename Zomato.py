import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Zomato Dashboard", layout="wide")
df = pd.read_csv("data.csv")

st.title("🍽️ Zomato Data Analysis Dashboard")
st.markdown("Overview of restaurants across countries based on Zomato data.")

# Sidebar Filters
st.sidebar.header("Filter")
city_list = df['City'].unique()
selected_city = st.sidebar.multiselect("Select Country", city_list, default=city_list[:3])

filtered_df = df[df['City'].isin(selected_city)]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Restaurants", filtered_df.shape[0])
col2.metric("Total Countries", filtered_df['City'].nunique())
col3.metric("Total Cuisines", filtered_df['Cuisines'].nunique())

# Bar chart - Restaurant count by country
st.subheader("📌 Number of Restaurants by Country")
country_counts = filtered_df['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Restaurants']
fig = st.bar_chart(country_counts, x='Country', y='Restaurants', color='Restaurants', height=400)
st.plotly_chart(fig, use_container_width=True)

# Pie chart - Ratings
st.subheader("⭐ Rating Distribution")
rating_counts = filtered_df['Aggregate rating'].value_counts().reset_index()
rating_counts.columns = ['Rating', 'Count']
fig2 = sns.countplot(rating_counts, values='Count', names='Rating', title="Rating Breakdown")
st.plotly_chart(fig2, use_container_width=True)
