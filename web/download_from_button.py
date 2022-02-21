# modulos
from selenium import webdriver
import time 
# Crea el objeto webdriver
# Aqui pones el path del driver
driver = webdriver.Chrome(<< path del chrome driver>>) 
# Aqui va el url de la pagina
driver.get(<< url de la pagina >>) 
# Abre la ventana de la url y automatiza la descarga por id de objeto
driver.maximize_window()
time.sleep(3) 
# Obtiene el boton de descarga por id (se obtiene el id inspecionando el html de la pagina)
button = driver.find_element_by_id(<< id del objeto que hay que apretar >>)
button.click()
