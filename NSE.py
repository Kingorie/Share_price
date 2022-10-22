#!/usr/bin/env python
# coding: utf-8

# In[4]:


# %load "C:\Users\Kingori\Downloads\NSE2.py"
#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import pandas as pd

def get_price_table():
    
    driver = webdriver.Chrome()
    driver.get('https://www.rich.co.ke/rcdata/nsestocks.php')
    driver.maximize_window

    stocks = driver.find_elements(By.XPATH, '//tr/td/a')[11:75]
    prev = driver.find_elements(By.XPATH, '//tr/td[3]')[2:]
    now = driver.find_elements(By.XPATH, '//tr/td[4]')[1:]
    percentage = driver.find_elements(By.XPATH, '//tr/td[5]')[1:]
    volume = driver.find_elements(By.XPATH, '//tr/td[7]')[1:]

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

    df = pd.DataFrame(stock_result)
    df

    df.to_excel('nse_share_prices.xlsx', index=False)

    driver.close()

    # Function to get current date and append it to name of new file
    import datetime
    def _getToday():
            return datetime.date.today().strftime("%Y%m%d")
    outpath = r"D:\OneDrive\Documents\SQL\PostgreSQL\Python\Projects\NSE_Data"
    filename = "%s_%s%s" % ("nse_share_prices", _getToday() ,".xlsx")
    filename_1 = outpath + "\\" + filename
    filename_1

    # To create the duplicate of
    # an already existing file

    import os
    D = r"D:\OneDrive\Documents\SQL\PostgreSQL\Python\Projects\NSE_Data"

    # importing the shutil module
    import shutil


    print("Before copying file:")
    print(os.listdir(D))

    # src contains the path of the source file
    src = r"D:\OneDrive\Documents\SQL\PostgreSQL\Python\Projects\NSE_Data\nse_share_prices.xlsx"

    # dest contains the path of the destination file
    dest = filename_1

    # create duplicate of the file at the destination,
    # with the name mentioned
    # at the end of the destination path
    # if a file with the same name doesn't already
    # exist at the destination,
    # a new file with the name mentioned is created
    path = shutil.copyfile(src, dest)

    print("After copying file:")
    print(os.listdir(D))

    # print path of the newly created duplicate file
    print("Path of the duplicate file is:")
    print(path)


    # create duplicate of the file at the destination,
    # with the name mentioned
    # at the end of the destination path
    # if a file with the same name doesn't already
    # exist at the destination,
    # a new file with the name mentioned is created
    path = shutil.copyfile(src, dest)

    print("After copying file:")
    print(os.listdir(D))

get_price_table()


# In[ ]:




