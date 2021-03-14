from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime

from progress.bar import Bar
import requests 
  
def scrape_info(path): 

    # Load the urls for each country    
    df = pd.read_csv(path)

    # Load Selenium driver
    driver_path = "./chromedriver"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # Initializing a progress bar
    bar = Bar('Collecting song data', max=len(df))

    for url in df.url:
    
        driver.get(url)
        time.sleep(2)

        src = driver.page_source
        html = BeautifulSoup(src, 'html.parser')

        try:
            views = html.find("span", class_="view-count").text.replace(" views", "")
            
            try:
                views = int(views.replace(u"\xa0", ""))
            except:
                views = int(views.replace(",", ""))

            df.loc[df.url == url, 'views'] = views
        except:
            print("Could not load data for a track. See data results.")

        bar.next()

    bar.finish()

    # returning the dictionary 
    return df 
  
def save_info(df):

    date = datetime.today().strftime('%Y-%m-%d')
    path = f"data_{date}.csv"

    df.to_csv(path)

# main function
if __name__ == "__main__": 
      
    path = "songs.csv"

    data = scrape_info(path) 
      
    save_info(data)