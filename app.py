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
st.markdown("<center><h4 style='color: white;'>Belli anahtar sözcüklerle Pubmed üzerinden konu ile ilgili hakemlerin maillerine ulaşabilirsin</h4></center>", unsafe_allow_html=True)
st.markdown("<center><h7 style= 'color: gray;'>Using specific keywords, you can find the e-mail addresses of the authors on the relevant subject on Pubmed.</h7></center>", unsafe_allow_html=True)

# Simple Rule
st.markdown("<center><h7 style= 'color: white;'>Aşağıdaki kutucuğa ilgili keywordleri aralarına virgül koyarak giriniz</h7></center>", unsafe_allow_html=True)
st.markdown("<center><h7 style= 'color: gray;'>Enter the necessary keywords in the box below, separated by a comma.</h7></center>", unsafe_allow_html=True)


key_words = st.text_input("Keyword")

splitted_keywords = key_words.split(",")

prepared_keywords = '+'.join(map(str, splitted_keywords))

original_url = "https://pubmed.ncbi.nlm.nih.gov/?term="+str(prepared_keywords)+"&format=pubmed&size=200"



if st.button("Ara - Search"):
        
        result = scraper(original_url)

        if len(result) < 1 :

            st.success("Yeni anahtar kelime deneyiniz - Try out a new keyboard")

        else:
            
            st.success(result)

st.markdown("[![Foo](https://cdn.ncbi.nlm.nih.gov/pubmed/bb4dbd9c-a268-461f-bd04-a93af5e9df18/core/images/pubmed-logo-white.svg)](https://pubmed.ncbi.nlm.nih.gov/)")        



print()

print()

print()

print()
st.markdown("<center><a href = https://turkalpmd.github.io><h7 style= 'color: red;'> Designer of this web-app: Izzet Turkalp Akbasli MD</h7></a></center>", unsafe_allow_html=True)
#pipreqs --savepath=requirements.txt && pip-compile