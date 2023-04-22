import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from collections import OrderedDict
# from selenium.webdriver.support.ui import Select




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
        try:  
            url = i.find('a', {'class': 'ent-name'}).get('href')
            list_urls.append(url)
        except: 
            pass


    return list_urls



def get_information(list_urls):
    """ Extracción de los datos por Pokemon

    Parámetros
    ----------
    list_urls [list]: Lista de urls de página web
    
    Retorno
    ----------
    list_name [list]:       Nombre
    list_generation [list]: Generación
    list_height[list]:      Altura
    list_weight[list]:      Peso
    list_type [list]:       Tipo
    list_image_url [list]:  Url de imagen
    list_kind [list]:       Egg group
    list_stats [dict]:      Stats
    list_evolution[list]:   Línea de evolución
    
    """
    
    list_name       = []
    list_generation = []
    list_height     = []
    list_weight     = []
    list_type       = []
    list_image_url  = [] 
    list_kind       = []
    list_stats      = []
    list_evolution  = []
    
    
    for url in list_urls:
        
        # Vinculación a web
        driver = webdriver.Chrome('./Driver/chromedriver.exe')
        driver.get(url)
        html = driver.page_source   
        soup = BeautifulSoup(html, 'html.parser')
        
             
        # Nombres
        try: 
            name = driver.find_element(By.XPATH, value='/html/body/main/h1').text
        except:
            name = ''
       
        # Generación
        try:
            generation = driver.find_element(By.XPATH, value='/html/body/main/p/abbr').text
        except:
            generation = ''
        
        # Altura
        try:
            height = driver.find_element(By.XPATH, value='/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td').text
        except:
            height = '' 
            
        # Peso
        try:
            weight = driver.find_element(By.XPATH, value='/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[5]/td').text
        except:
            weight = ''  
        
        # Tipos
        try:
            all_types = driver.find_element(By.XPATH, value='/html/body/main/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td')
        except:
            all_types = ''
        
        types = []
        all_types = all_types.find_elements(By.CSS_SELECTOR, value='a')
        for i in all_types:
            types.append( i.text )
        types = [w.capitalize() for w in types] # Capitalizar el texto
        
        # URL de imágenes
        try:
            image_url = driver.find_element(By.XPATH, value = '/html/body/main/div[2]/div[2]/div/div[1]/div[1]/p[1]/a').get_attribute('href')
        except:
            image_url = ''
        
        ## Egg group
        try:
            all_kinds = driver.find_element(By.XPATH, value = '/html/body/main/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/table/tbody/tr[1]/td')
        except:
            pass
        kinds = []
        all_kinds = all_kinds.find_elements(By.CSS_SELECTOR, value='a')
        for i in all_kinds:
            kinds.append( i.text )
        
        # Stats
        stats = soup.find('div', {'class': 'resp-scroll'})
        stats = pd.read_html(str(stats))[0]
        
        stats = stats[[0, 1]]
        stats = stats.set_index(stats.columns[0])
        stats = list(stats.to_dict().values())[0]
        
        # Línea de evolución
        evol = driver.find_element(By.XPATH, value = '/html/body/main/div[5]')
        evol = evol.find_elements(By.CSS_SELECTOR, value='div')
            
        evols = []
        for e in evol:
            e = e.find_element(By.CLASS_NAME, value='ent-name')
            evols.append( e.text )
        evols = list(OrderedDict.fromkeys(evols))
        
        if evols == []:
            evols = [name]


        # Guardado
        list_name.append(name)
        list_generation.append(generation)
        list_height.append(height)
        list_weight.append(weight)
        list_type.append(types)
        list_image_url.append(image_url)
        list_kind.append(kinds)
        list_stats.append(stats)
        list_evolution.append(evols)
        
        driver.close()

    return (
        list_name, list_generation, list_height, list_weight, list_type,
        list_image_url, list_kind, list_stats, list_evolution
        )




  