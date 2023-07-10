import requests
from bs4 import BeautifulSoup

# url = 'https://theuselessweb.com/'
# out = requests.get(url)


# f = open("demofile.html", "a")
# f.write(out.text)
# f.close()

from selenium import webdriver
  
driver = webdriver.Chrome()
driver.get("https://theuselessweb.com/")
with open("page_source.html", "w", encoding='utf-8') as f:
    f.write(driver.page_source)