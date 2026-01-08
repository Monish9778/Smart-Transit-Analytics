import streamlit as st
import pandas as pd


st.set_page_config(page_title='Smart Transit Analytics', layout='wide')


st.title('🚍 Smart Transit Analytics Dashboard')


data = pd.read_csv('../data/processed/cleaned_transit_data.csv')


st.subheader('Route Performance Overview')
st.dataframe(data)


st.subheader('Passenger Count by Route')
st.bar_chart(data.groupby('route_id')['passenger_count'].mean())
