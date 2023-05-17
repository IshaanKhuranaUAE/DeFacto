#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Libraries Import
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url = "http://quotes.toscrape.com/page/1/"


# In[3]:


response = requests.get(url)


# In[4]:


response = response.content


# In[6]:


soup = BeautifulSoup(response,'html.parser')


# In[7]:


print(soup.prettify())


# In[11]:


div_ = soup.find_all('div',class_ = 'quote')
len(div_)


# In[104]:


def get_quotes(div_):
    quotes = []
    for tag in div_:
        quote = tag.find('span',class_='text').text
        quotes.append(quote)
    return quotes


# In[105]:


get_quotes(div_)


# In[93]:


def get_authors(div_):
    authors = []
    for tag in div_:
        span_ = tag.find('span',class_=None)
        author = span_.find('small',class_='author').text
        authors.append(author)
    return authors


# In[94]:


get_authors(div_)


# In[95]:


def get_quoted(div_):
        keywords=[]
        for tag in div_:
            keyword =tag.find('div',class_='tags').meta['content']
            keywords.append(keyword)
        return keywords


# In[96]:


get_quoted(div_)


# In[103]:


def list_of_all(quotes_,authors_,keywords_):
    return[{'Quotes':quotes_[i],
           'Authors':authors_[i],
           'Tags':keywords_[i]}for i in range(len(quotes_))]
combined_dict = list_of_all(quotes_,authors_,keywords_)


# In[102]:


df = pd.DataFrame(combined_dict)
df.to_csv(combined_dict,index=None)


# In[ ]:




