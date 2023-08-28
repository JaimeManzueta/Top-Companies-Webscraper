from bs4 import BeautifulSoup
import requests
import re

url = f"https://companiesmarketcap.com/"

request = requests.get(url).text

soup = BeautifulSoup(request, "html.parser")

tbody = soup.tbody


Companies = tbody.find_all(class_="company-name")


for company in Companies[:]:
    print(company.text)
    print()
    

    
    






