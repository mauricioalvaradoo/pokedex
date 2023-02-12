from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
# import pandas
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from time import sleep
# import re



def get_urls(url):
    """ Obtención de URL de Pokemons
    
    Parámetros
    ----------
    url [str]: Url de página web
    
    Retorno
    ----------
    list_urls [list]: Lista de Urls
    
    """
    
    driver = webdriver.Chrome('./Driver/chromedriver.exe')
    driver.get(url)
    html = driver.page_source   
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()

    list_urls = [] 
    observations = soup.find_all('tr')

    for i in observations:
        tds = i.find_all('td')
        
        for j in tds:
            try:  
                url = j.find('a').get('href')
                list_urls.append(url)
            except: 
                pass
    
    # Modificaciones finales
    list_urls = [u for u in list_urls if u.startswith('/wiki')]
    list_urls = [u for u in list_urls if not (u.endswith('type') or u.endswith('UserLogin'))]
    list_urls = [u for u in list_urls if not u.endswith('Pok%C3%A9dex')]
    
    return list_urls



def get_information(list_urls):
    """ Extracción de los datos por Pokemon

    Parámetros
    ----------
    list_urls [list]: Lista de urls de página web
    
    Retorno
    ----------
    list_id [list]: Número
    list_name [list]: Nombre
    list_generation [list]: Generación
    list_type [list]: Tipo
    list_image_url [list]: Url de imagen
    list_kind [list]
    list_abilities [dict]: Habilidades    
    
    """
    
    list_id = []
    list_name = []
    list_generation = []
    list_type = []
    list_image_url = [] 
    list_kind = []
    list_abilities = [] 
    
    for url in list_urls:
        
        # Vinculación a web
        driver = webdriver.Chrome('./Driver/chromedriver.exe')
        driver.get(url)
        html = driver.page_source   
        soup = BeautifulSoup(html, 'html.parser')
        dom = etree.HTML(str(soup)) # Para trabajo con xpath
        driver.close()
        
        # Recoger los valores
        pid = dom.xpath('//*[@id="mw-content-text"]/div[1]/aside/section[4]/section[1]/section[2]/div[1]')[0].text
        name = dom.xpath('//*[@id="mw-content-text"]/div[1]/aside/section[1]/h2[1]')[0].text
        generation = dom.xpath('//*[@id="mw-content-text"]/div[1]/aside/section[2]/section[1]/section[2]/div/a')[0].text
        image_url = soup.xpath('//*[@id="mw-content-text"]/div[1]/aside/figure/a//@href')
        
        # types = []
        # ptype = soup.find_all('div', {'xpath': 'pi-data-value pi-font'})
        # for i in ptype:
        #     types.append( i.find('a').text )    
        
        # kinds = []
        # kind = soup.find_all('div', {'xpath': '//*[@id="mw-content-text"]/div[1]/aside/section[6]/section[3]/section[2]/div[1]'})
        # for i in kind:
        #     kinds.append( i.find('a').text )
        
        # abilities =                                                       

        # Guardado
        list_id.append(pid)
        list_name.append(name)
        list_generation.append(generation)
        # list_type.append(types)
        list_image_url.append(image_url)
        # list_kind.append(kinds)
        # list_abilities.append()


    return list_id, list_name, list_generation, list_type, list_image_url, list_kind #, list_abilities




  