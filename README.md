# Overview
This Python script uses Selenium to scrape NSE (Nairobi Securities Exchange) share prices from the Rich Management website. The scraped data includes stock names, previous prices, current prices, percentage changes, and trading volumes.

# Dependencies
- Selenium: A web testing library.
- Pandas: A data manipulation library.
- Schedule: A simple job scheduling library.




# Share price Scraper

This is a Python program that gets the current stock prices of shares trading at the Nairobi Stock Exchange (NSE).
The program then stores the prices in a table in an excel file.

# Objective

While there is access to intrad-day live data, historical data is hard to come by. 
Using Selenium web driver for chrome, this script launches a headless browser and then scrapes all the relevant share details.

# How it works

1. Download your appropriate chromedriver and save it to drive
2. Run "All Cells" on ipynb file. A *.csv* file is created for this date. Script overwrites previous file



