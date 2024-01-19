# Overview
This Python script uses Selenium to scrape NSE (Nairobi Securities Exchange) share prices from the Rich Management website. The scraped data includes stock names, previous prices, current prices, percentage changes, and trading volumes.

# Dependencies
- Selenium: A web testing library.
- Pandas: A data manipulation library.
- Schedule: A simple job scheduling library.

# Usage

1. Make sure you have the ChromeDriver installed and available in your system PATH.
2. Run the script, and it will open the Rich Management NSE page, scrape the relevant data, and save it to an Excel file named nse_share_prices.xlsx.
3.The Excel file is saved in the specified output path, and its filename includes the current date.

# Code Structure
- Section 1: Imports necessary libraries.
- Section 2: Initializes the Selenium WebDriver and navigates to the target webpage.
- Section 3: Scrapes stock data using XPath queries.
- Section 4: Creates a Pandas DataFrame from the scraped data.
- Section 5: Saves the DataFrame to an Excel file.
- Section 6: Closes the WebDriver.

# Additional Functionality

- The script includes a function (_getToday) to generate the current date, which is used in the output file's name.
- It creates a duplicate of the generated Excel file, appending the current date to the filename for versioning.

# Output

The script outputs an Excel file (nse_share_prices.xlsx) containing the scraped NSE share prices. The file is saved in the specified output path with a filename that includes the current date.

Feel free to customize the script as needed for your specific use case.
