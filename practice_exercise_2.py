import time
import random
import configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
driver.find_element(By.ID, "email").send_keys(configuration.email)
driver.find_element(By.ID, "password").send_keys(configuration.password)
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
driver.implicitly_wait(10)

# Guardar el título de la tarjeta más reciente
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text
print(title_before)
# Hacer clic en el botón que publica una nueva tarjeta
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
new_title = "Tokio"+str((random.randint(100, 999)))
driver.find_element(By.NAME, "name").send_keys(new_title)

# Insertar el enlace a la imagen en el campo Enlace
driver.find_element(By.NAME, "link").send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

# Guardar los datos
driver.find_element(By.XPATH, ".//form[@name='new-card']/button[text()='Guardar']").click()

# Esperar a que aparezca el botón Eliminar
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='card__delete-button card__delete-button_visible']")))

# Comprobar que la tarjeta tiene el título correcto
title_after = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")

assert title_after.text == new_title

# Guardar la cantidad de tarjetas antes de eliminar
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# Eliminar la tarjeta
driver.find_element(By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']").click()

# Esperar a que el título de la tarjeta más reciente sea igual a title_before
#WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element( (By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before))

# Comprobar que ahora hay una tarjeta menos
#cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

#assert cards_before != cards_after

#driver.quit()
