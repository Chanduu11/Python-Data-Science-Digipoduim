import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
 
# loading the data 
@st.cache_data
def load_data():
    path='data\kc_house_data.csv'
    df=pd.read_csv(path)
    return df 

# call the load data function
with st.spinner('Loading Data....'):
    df=load_data()

# call the title for your app
st.title('House Price Data Analytics')
st.subheader('Key Performance Indicators')

# get the list of all columns
cols=df.columns.tolist()
selected_cols=st.multiselect('Select columns',cols) #for multiple selection of columns
st.write(f'You selected:{ len(selected_cols)}columns')
# '''st.metric(label='Average price',
#           value=round(df['price'].mean()),
#           delta=round(df['price'].std())
#           )'''
for col in selected_cols:
    st.subheader(f'Column: {col}')
    try:
        st.metric(label=f'Mean {col}',
                   value=round(df[col].mean()),
                   delta=round(df[col].std()))
        st.line_chart(df[col],use_container_width=True)
    except:
        st.error(f'Cannot display {col} numeric data')
