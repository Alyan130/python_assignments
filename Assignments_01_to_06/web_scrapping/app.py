import requests 
from bs4 import BeautifulSoup as bs
import streamlit as st

BASE_URL="https://www.bbc.com/news"
response = requests.get(BASE_URL)

content = bs(response.text, "html.parser")
headings = content.find_all("h2",{"class":"sc-87075214-3 eywmDE"})

st.title("BBC NEWS SCRAPPER")
st.header("Latest News")

for news in headings:
    with st.container(border=True):
        st.markdown(news.text)


