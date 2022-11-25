import streamlit as st
import re
# re for regular expression matching operations
import requests
# requests for sending HTTP requests
from urllib.parse import urlsplit
# urlsplit for breaking URLs down into component parts
from collections import deque
# deque is a list-like container with fast appends and pops on either end
from bs4 import BeautifulSoup
import lxml.etree as xml
import lxml
#BeautifulSoup for pulling data out of HTML files of websites
import pandas as pd
#pandas for formatting emails into a DataFrame for further manipulation
from PIL import Image
from utils import *
import numpy as np

# For alignment of image
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.image("https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/logo-jpic.png")
with col3:
    st.write("")


#st.markdown("[![Foo](https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/logo-jpic.png)](http://worldpediatricsociety.org/jpic/index.html)")

# Introduction
st.markdown("<h2 style='text-align: center; color: white;'>Belli anahtar sözcüklerle Pubmed üzerinden konu ile ilgili hakemlerin maillerine ulaşabilirsin</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Using specific keywords, you can find the e-mail addresses of the authors on the relevant subject on Pubmed. </h5>", unsafe_allow_html=True)

# Simple Rule
st.markdown("<h4 style='text-align: justify-center; color: white;'>Aşağıdaki kutucuğa ilgili keywordleri aralarına virgül koyarak giriniz</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: justify-center; color: white;'>Enter the necessary keywords in the box below, separated by a comma.</h5>", unsafe_allow_html=True)


key_words = st.text_input("Keyword")

splitted_keywords = key_words.split(",")

prepared_keywords = '+'.join(map(str, splitted_keywords))

original_url = "https://pubmed.ncbi.nlm.nih.gov/?term="+str(prepared_keywords)+"&format=pubmed&size=200"



if st.button("Ara - Search"):
        
        result = scraper(original_url)

        st.success(result)

st.markdown("[![Foo](https://cdn.ncbi.nlm.nih.gov/pubmed/bb4dbd9c-a268-461f-bd04-a93af5e9df18/core/images/pubmed-logo-white.svg)](https://pubmed.ncbi.nlm.nih.gov/)")        


#pipreqs --savepath=requirements.txt && pip-compile