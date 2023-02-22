import pandas as pd
import numpy as np
import streamlit as st 
import plotly.express as px 
import re  #regular expresion
from textblob import TextBlob


st.title("Sentiment Analysis 👨")

def remove_mentions(tweet):
    return re.sub('@[A-Za-z0-9]+',"",tweet)
def remove_hashtags(tweet):
    return re.sub('#[A-Za-z0-9]+',"",tweet)

def remove_links(tweet):
    tweet = re.sub('[()!?]',' ',tweet)
    tweet = re.sub(r'\[.*?\]',' ',tweet)
    tweet = re.sub(r'http\S+',' ',tweet)
    tweet = re.sub(r'www.\S+',' ',tweet)
    tweet = re.sub(r'[^a-z0-9]',' ',tweet)
    return tweet
    
    
    
def get_sentiment(tweet):
    try:
        blob = TextBlob(tweet)
        return blob.sentiment.polarity
    except:
        return np.nan

def get_sentiment_name(sentiment):
    if sentiment==0:
        return"🟢 Neutral"
    elif sentiment>0:
        return "😎 positive"
    else:
        return "👿 Negative"
    
@st.cache
def load_data():
    df = pd.read_csv('elonmusk.csv',
                     parse_dates=['Date Created'], dayfirst=True)
    df.sort_values(by='Date Created', inplace = True)
    df['Tweets']=df['Tweets'].str.lower()
    df['Tweets']=df['Tweets'].apply(remove_hashtags)
    df['Tweets']=df['Tweets'].apply(remove_mentions)
    df['Tweets']=df['Tweets'].apply(remove_links)
    df['Sentiment']=df['Tweets'].apply(get_sentiment)
    df['SentimentName']=df['Sentiment'].apply(get_sentiment_name)
    
    return df

df = load_data()
if st.checkbox("show raw data"):
    st.write(df)