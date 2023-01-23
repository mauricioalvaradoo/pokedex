import pandas
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
 
import re

def get_urls(url):
    
    #Ingresar a la pag.web y extraer el código HTML. 
    driver = webdriver.Chrome("./Driver/chromedriver.exe")
    driver.get(url)
    html = driver.page_source   
    soup = BeautifulSoup(html, "html.parser")
    
    #Se genera una variable que agrupe todos los pokemones hallados. 
    observations = soup.find_all('tr')
    
     
    list_names = []
    list_urls = []
    list_images = []
    
    
    for i in observations:
        tds = i.find_all("td")
        for j in tds:
            try: 
                
                url = j.find("a").get("href")
                list_urls.append(url)
                
            except: 
                pass
    
    
    list_urls = [i for i in list_urls if i.startswith("/wiki")]
    list_urls = [i for i in list_urls if not (i.endswith("type") or i.endswith("UserLogin"))]
    list_urls = [i for i in list_urls if not i.endswith("Pok%C3%A9dex")]
    
        
      
    return list_urls


   
   
   
   
   
   
   
   
   
   
   
  