import streamlit as st
import pandas as pd

def display_dataframe(tweets_df):
    
    if 'number_of_rows' not in st.session_state:
        st.session_state['number_of_rows'] = 5


    df = tweets_df

    increment = st.button('Show more columns ⬆️', key = 31644534)
    if increment:
        st.session_state.number_of_rows += 1

    decrement = st.button('Show less columns ⬇️', key = 32623643464)
    if decrement:
        st.session_state.number_of_rows -= 1

    #st.table(df.head(st.session_state['number_of_rows']))
    st.dataframe(df.head(st.session_state['number_of_rows']))
    

    