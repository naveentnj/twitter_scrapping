import json
from turtle import onclick
import streamlit as st

import pandas as pd
import snscrape.modules.twitter as sntwitter
from pymongo_data_store import store_data

from datetime import date, timedelta, datetime
import json

search_types = ["Username", "Keyword", "#Hashtag"]

# Default Values
input_text = "hello" 

tweets_df = pd.DataFrame()

st.title("Twitter Scrapping Web App")

selected_search_type = st.selectbox("Select You want search for  Keyword or #Hashtag", search_types)
st.success(f"You have chosen {selected_search_type}")


if selected_search_type == "Username":
    input_text = st.text_input("Enter Username")
    st.success(f"Successfully Scrapping the Twitter {input_text}")
elif selected_search_type == "Keyword":
    input_text = st.text_input("Enter Keyword")
    st.success(f"Successfully Scrapping the Twitter {input_text}")
elif selected_search_type == "#Hashtag":
    input_text = st.text_input("Enter Hashtag without #")
    st.success(f"Successfully Scrapping the Twitter {input_text}")

no_of_tweets = st.number_input("Enter Number tweets", min_value = 50)


from_date = st.date_input("Enter the from date",value = (date.today()-timedelta(days=60)), )
to_date = st.date_input("Enter the to date")
st.write(f"You want {from_date} {to_date}")

data_collect = [input_text, from_date, to_date, no_of_tweets]

@st.cache_data
def search_function(input_text,from_date , to_date ,no_of_tweets = 50):
    # Creating list to append tweet data to
    tweets_list2 = []

    input_search_data = input_text
    # Using TwitterSearchScraper to scrape data and append tweets to list
    if selected_search_type == "Username":
        input_search_data = sntwitter.TwitterSearchScraper(f'from:{input_text} since:{from_date} until:{to_date}').get_items()
    elif selected_search_type == "Keyword":
        input_search_data = sntwitter.TwitterSearchScraper(f'{input_text} since:{from_date} until:{to_date}').get_items()
    else:
        input_search_data = sntwitter.TwitterSearchScraper(f'#{input_text} since:{from_date} until:{to_date}').get_items()

    for i,tweet in enumerate(input_search_data):
        if i>no_of_tweets:
            break
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        
    # Creating a dataframe from the tweets list above
    tweets_df3 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Usernames'])

    
    return tweets_df3


submitted_search = st.button("Submit to search")



#st.form_submit_button("Submit to search")

one_df = pd.DataFrame()




tweets_df = search_function(input_text,from_date,to_date,no_of_tweets)

    
    


if submitted_search:
    rows = {"number_of_rows": 40}
    st.dataframe(tweets_df.head(rows["number_of_rows"]))

    increment = st.button('Show more columns ⬆️')
    if increment:
        rows["number_of_rows"] += 1

    decrement = st.button('Show less columns ⬇️')
    if decrement:
        rows["number_of_rows"] += 1



@st.cache_data
def convert_df_to_dict(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_dict(orient="records")




st.write("Click if you want to load to Mongo DB server")
mongodb_button = st.button("Store in MongoDB")

if mongodb_button not in st.session_state:
    
    tweets_df_dict = convert_df_to_dict(tweets_df)
    #mongo_input_data = [[{"Scrapped Word Or Username":input_text},{"Scrapped Date ": date.today()}],tweets_df_dict]
    stored_ack = store_data(tweets_df_dict)
    st.success(f"Data Stored successfully with the ID {stored_ack}")



st.write("Click if you want to download CSV format")

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(tweets_df)

st.download_button(
    label="Download Twitter Scrapped data as CSV",
    data=csv,
    file_name='tweet.csv',
    mime='text/csv',
)


@st.cache_data
def convert_df_json(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_json()

json_data = convert_df_json(tweets_df)

json_string = json.dumps(json_data)

st.json(json_string, expanded=True)

st.download_button(
    label="Download JSON",
    file_name="data.json",
    mime="application/json",
    data=json_string,
)

