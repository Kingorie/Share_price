#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# In[2]:


driver = webdriver.Chrome()
driver.get('https://www.rich.co.ke/rcdata/nsestocks.php')
driver.maximize_window
#driver.close()


# In[3]:


stocks = driver.find_elements(By.XPATH, '//tr/td/a')[11:75]
prev = driver.find_elements(By.XPATH, '//tr/td[3]')[2:]
now = driver.find_elements(By.XPATH, '//tr/td[4]')[1:]
percentage = driver.find_elements(By.XPATH, '//tr/td[5]')[1:]
volume = driver.find_elements(By.XPATH, '//tr/td[7]')[1:]


"""
# To confirm if code works:

for stocks in stocks:
     print(stocks.text) 
    
"""


# In[4]:


print(len(stocks))
print(len(prev))
print(len(now))
print(len(prev))


# In[5]:


# To loop over all lists and get text elements:


stock_result = []

# to get length of the rows. Can use len(countries, popultaion or world_share)

for i in range(len(volume)):
    temporary_data = {
        'stocks': stocks[i].text,
        'prev': prev[i].text,
        'now': now[i].text,
        'percentage': percentage[i].text,
        'volume': volume[i].text}

    stock_result.append(temporary_data)


# In[6]:



df = pd.DataFrame(stock_result)
df


# In[7]:


df.to_excel('nse_share_prices.xlsx', index=False)


# In[8]:


driver.close()


# In[ ]:




