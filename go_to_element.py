import time

from prompt_toolkit.keys import Keys

import configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(3)

# Buscar el campo Correo electrónico y rellenarlo
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys(configuration.email)

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys(configuration.password)

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Buscar el pie de página
element = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(3)

# Comprobar que el pie de página contiene el string 'Around'
assert "Around" in element.text

driver.quit()
