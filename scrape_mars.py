#!/usr/bin/env python
# coding: utf-8

# In[89]:


import requests
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# In[18]:


URL = 'https://mars.nasa.gov/news/'
page = requests.get(URL)


# In[11]:


soup = BeautifulSoup(page.content, 'html.parser')

#results = soup.find(id='ResultsContainer')


# In[14]:


for div in soup.find_all(class_='item_list'):
    for childdiv in div.find_all('slide'):
        print (childdiv.string) #london, york


# In[20]:


#print(page.content)
 print(soup.find_all(class_='image_and_description_container'))
#print(results.prettify())


# In[25]:


results = soup.find_all(class_='image_and_description_container')
first_children = [i.text for i in soup.select('.image_and_description_container div:first-child')]
print(first_children)
#print(results)


# In[81]:


results = soup.select('.image_and_description_container')
#results.find_all('a', href=True)

div = soup.find(class_='image_and_description_container')
for p in div.find_all('img', alt=True):
    if p['alt'] != 'More':
        news_title = p['alt']
        print(news_title)
news_p = div.get_text(strip=True)
print(news_p)


# In[111]:


executable_path = {'executable_path':'chromedriver.exe'}

browser = Browser('chrome', **executable_path , headless=False)


# In[119]:


url = "https://www.jpl.nasa.gov/images/"
browser.visit(url)

featured_image_url='https://d2pn8kiwq2w21t.cloudfront.net/images/jpegPIA24364.2e16d0ba.fill-400x400-c50.jpg'


# In[ ]:


import pandas as pd


# In[120]:


url = 'https://space-facts.com/mars/'
dfs = pd.read_html(url)


# In[123]:


dfs[0]


# In[124]:


html_df = df.to_html()


# In[125]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]


# In[ ]:


#get_ipython().system('jupyter nbconvert --to script config_template.ipynb')

