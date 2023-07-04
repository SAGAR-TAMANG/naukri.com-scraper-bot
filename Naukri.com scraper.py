import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://www.naukri.com/it-jobs?k=it"

page = requests.get(url)
# print(page.text)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html5lib')

# print(soup.prettify())

driver.close()

df = pd.DataFrame(columns=['Title','Company','Ratings','Reviews','URL'])
results = soup.find(class_='list')
job_elems=results.find_all('article', class_='jobTuple')

# print(job_elems)

for job_elem in job_elems:
  # URL to apply for the job     
  URL = job_elem.find('a',class_='title ellipsis').get('href')
  print(URL)
  
  # Post Title
  Title = job_elem.find('a',class_='title ellipsis')
  print("Job Title: " + Title.text)
  
  Company = job_elem.find('a', class_='subTitle ellipsis fleft')
  print("Company: " + Company.text)

  Exp = job_elem.find('span', class_='ellipsis fleft expwdth')
  print('Experience: ' + Exp.text)
  print(" "*2)
