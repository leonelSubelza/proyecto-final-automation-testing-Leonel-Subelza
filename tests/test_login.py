from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from utils.data import read_csv_login
from utils.logger import logger

# Cargar datos del CSV
LOGIN_CASES = read_csv_login('data/login_cases.csv')

@pytest.mark.parametrize("username, password, must_work, error_text", LOGIN_CASES)
# @pytest.mark.parametrize("username, password, must_work, error_text", [
  # (fake.user_name(),fake.password(length=8,upper_case=True,lower_case=True),False,"Epic sadface: Username and password do not match any user in this service"),
  # (fake.user_name(),fake.password(length=8,upper_case=True,lower_case=True),False,"Epic sadface: Username and password do not match any user in this service"),
# ])
def test_login(driver,username,password,must_work,error_text):
  try:
    logger.info("-----Ejecutando test_login.py-----")
    logger.debug("Realizando login válido...")
    login = LoginPage(driver).openPage().do_complete_login(username,password)
    logger.debug("Login válido realizado correctamente")
  
    if must_work:  
      logger.debug("Realizando Verificación y Navegación de la página")
      login.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))    
      
      #Navegación y Verificación del Catálogo: (Clases 6 a 8)
      assert '/inventory.html' in driver.current_url, f"URL inesperada: {driver.current_url}"
      assert driver.find_element(By.CLASS_NAME, 'title').text == 'Products', f"Título inesperado: {driver.title}"
      logger.info("-----test_login.py exitoso completado correctamente-----")
    else:
      # if username == '' and password == '':
      #   raise Exception("Lanzando error forzado en test_login.py para captura de pantalla")
      text_error = LoginPage(driver).get_error_message_page()
      assert text_error in error_text
      logger.info("-----test_login.py fallido completado correctamente-----")
      
  except Exception as e:
    print(f"Error en test_login: {e}")
    logger.warning(f"Error en test_login: {e}")
    raise