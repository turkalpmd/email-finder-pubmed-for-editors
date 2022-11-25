import streamlit as st
import re
# re for regular expression matching operations
import requests
import lxml.etree as xml
import lxml
# requests for sending HTTP requests
from urllib.parse import urlsplit
# urlsplit for breaking URLs down into component parts
from collections import deque
# deque is a list-like container with fast appends and pops on either end
from bs4 import BeautifulSoup
#BeautifulSoup for pulling data out of HTML files of websites
import pandas as pd
#pandas for formatting emails into a DataFrame for further manipulation

def scraper(original_url):
  def list_diff(a, b):
      r = []

      for i in a:
          if i not in b:
              r.append(i)
      return r
      
  different = []
  invited = []

  unscraped = deque([original_url])  
  scraped = set()  
  emails = set()  

  while len(unscraped):
      url = unscraped.popleft()  
      scraped.add(url)
      parts = urlsplit(url)
      base_url = "{0.scheme}://{0.netloc}".format(parts)
      if '/' in parts.path:
        path = url[:url.rfind('/')+1]
      else:
        path = url
      #print("Crawling URL %s" % url)
      try:
          response = requests.get(url)
      except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
          continue
      new_emails = set(re.findall(r"[A-Za-z0-9_%+-.]+"
                                  r"@[A-Za-z0-9.-]+"
                                  r"\.[A-Za-z]{2,10}", response.text, re.I))
      emails.update(new_emails) 
      soup = BeautifulSoup(response.text, 'lxml')
      for anchor in soup.find_all("a"):
        if "href" in anchor.attrs:
          link = anchor.attrs["href"]
        else:
          link = ''
          if link.startswith('/'):
              link = base_url + link
          elif not link.startswith('http'):
              link = path + link
          if not link.endswith(".gz"):
            if not link in unscraped and not link in scraped:
                unscraped.append(link)



  df = pd.DataFrame(emails,
                    columns=["Email"])

  df.Email = df.Email.unique() # Bu şekilde aynı listedeki unique'leri alır mükerrer olanlar drop edilir.


  new = list(df.Email.values) # yani bir liste oluşturduk. Bu listeyi önceki mailler ile karşılaştıracağız. 

  different = list_diff(new,invited) # önceki mail gönderilen kümeden farkını alıyoruz bu şekilde


  for i in different: # Bu yeni gelenleri de eklemiş olalım. 
    invited.append(i)

  return different 