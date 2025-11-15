import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time



url = "https://blog.scrapinghub.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

print("\n---- BeautifulSoup Blog Posts ----")

titles = soup.find_all("h2", class_="post-title")

for t in titles[:5]:  
    print(t.text.strip())




options = Options()
options.add_experimental_option("detach", True)  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://blog.scrapinghub.com/")
print("\nSelenium browser opened!\n")

time.sleep(2)  

posts = driver.find_elements(By.CSS_SELECTOR, "h2.post-title")

scraped_data = []

for post in posts[:5]: 
    title = post.text.strip()
    link = post.find_element(By.TAG_NAME, "a").get_attribute("href")
    scraped_data.append({"Title": title, "URL": link})
    print(title, " --> ", link)




df = pd.DataFrame(scraped_data)
df.to_csv("blog_data.csv", index=False)

print("\nData saved as blog_data.csv")
