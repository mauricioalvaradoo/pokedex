import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# import pandas
# from selenium.webdriver.support.ui import Select

# from time import sleep
# import re



def get_urls(url):
    """ Obtención de URLs de Pokemons
    
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
    list_name [list]: Nombre
    list_generation [list]: Generación
    list_type [list]: Tipo
    list_image_url [list]: Url de imagen
    list_kind [list]: Egg group
    list_stats [dict]: Stats  
    
    """
    
    list_name = []
    list_generation = []
    list_type = []
    list_image_url = [] 
    list_kind = []
    list_stats = []
    
    
    for url in list_urls:
        
        # Vinculación a web
        driver = webdriver.Chrome('./Driver/chromedriver.exe')
        driver.get(url)
        html = driver.page_source   
        soup = BeautifulSoup(html, 'html.parser')
        
             
        # Nombres
        try: 
            name = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[1]/h2[1]').text
        except:
            try:
                name = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div[2]/section[1]/h2[1]').text
            except:
                try:
                    name = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div/section[1]/h2[1]').text
                except:
                    name = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[1]/h2[1]').text
       
        # Generación
        try:
            generation = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[2]/section[1]/section[2]/div/a').text
        except:
            try:
                generation = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div[2]/section[2]/section[1]/section[2]/div').text
            except:
                try:
                    generation = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div/section[2]/section[1]/section[2]/div').text
                except:
                    generation = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[2]/section[1]/section[2]/div').text
        
        # Tipos
        try:
            all_types = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[2]/div[1]/div')
        except:
            try:
                all_types = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div[2]/section[2]/div[1]/div')
            except:
                try:
                    all_types = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section/div/section[2]/div[1]/div')
                except:
                    all_types = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/aside/section[2]/div[1]/div')
        types = []
        all_types = all_types.find_elements(By.CSS_SELECTOR, value='a')
        for i in all_types:
            types.append( i.get_attribute('title') )
        
        # URL de imágenes
        try:
            image_url = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/figure/a').get_attribute('href')
        except:
            try:
                image_url = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section/div[2]/figure/a').get_attribute('href')
            except:
                try:
                    image_url = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section/div/figure/a').get_attribute('href')
                except:
                    try:
                        image_url = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/figure/a').get_attribute('href')
                    except:
                        image_url = ''
        ## Egg group
        try:
            all_kinds = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section[6]/section[3]/section[2]/div[1]')
        except:
            try:
                all_kinds = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section/div[2]/section[6]/section[3]/section[2]/div[1]')
            except:
                try:
                    all_kinds = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section/div/section[6]/section[3]/section[2]/div[1]')
                except:
                    all_kinds = driver.find_element(By.XPATH, value = '//*[@id="mw-content-text"]/div[1]/aside/section[6]/section[3]/section[2]/div[1]')
        kinds = []
        all_kinds = all_kinds.find_elements(By.CSS_SELECTOR, value='a')
        for i in all_kinds:
            kinds.append( i.get_attribute('title').replace(' (egg group)', '' ) )
        
        # Stats
        stats = soup.find('table', {'class': 'roundy'})
        stats = pd.read_html(str(stats))[0]
        stats = stats.set_index(stats.columns[0])
        stats = list(stats.to_dict().values())[0]

        
        # Guardado
        list_name.append(name)
        list_generation.append(generation)
        list_type.append(types)
        list_image_url.append(image_url)
        list_kind.append(kinds)
        list_stats.append(stats)
        
        driver.close()

    return (
        list_name, list_generation, list_type, list_image_url,
        list_kind, list_stats
        )




  