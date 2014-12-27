# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    response = requests.get("http://www.winebid.com/")
    data = response.text
    soup =BeautifulSoup(data)
    
    for link in soup.find_all('a'):
        print(link.get('href'))