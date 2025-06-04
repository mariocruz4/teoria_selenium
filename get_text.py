import time
import configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

time.sleep(5)

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el campo Correo electrónico y rellenarlo
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
driver.find_element(By.ID,"email").send_keys(configuration.email)

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys(configuration.password)

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Buscar el botón, recuperar su texto y comprobar que el valor del texto es 'Cerrar sesión'
assert driver.find_element(By.CLASS_NAME, "header__logout").text == "Cerrar sesión"

driver.quit()
