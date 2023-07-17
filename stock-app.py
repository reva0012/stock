import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px
from stocknews import StockNews


st.set_page_config(page_title='Stock Dashboard', page_icon=":bar_chart:", layout='wide')

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

data = yf.download(ticker, start = start_date, end = end_date)
fig = px.line(data, x=data.index, y=data['Volume'], title = ticker)
st.plotly_chart(fig)

pricing_data, news = st.tabs(["Pricing Data", "Top 10 News"])

with pricing_data:
    st.header('Pricing Data')
    st.write(data)


with news:
    st.header(f'News of {ticker}')
    sn = StockNews(ticker, save_news = False)
    df_news = sn.read_rss()
    for i in range (10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Settlement {title_sentiment}')        
        news_sentiment = df_news ['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
