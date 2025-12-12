import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.saucedemo import login
from pages.login_page import LoginPage
import pathlib
import requests
from utils.logger import logger
from datetime import datetime

# creamos sino existe las carpetas reports/screens
target = pathlib.Path("reports/screens")
target.mkdir(parents=True,exist_ok=True)

# Para darle titulo y descripcion al reporte
def pytest_html_report_title(report):
    report.title = "TalentoLab – Resumen de ejecución"
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["Suite UI + API completa"])

# def pytest_html_results_table_header(cells):
#   """Añade una columna 'URL' justo después de 'Test ID'."""
#   cells.insert(2, 'URL')

# def pytest_html_results_table_row(report, cells):
#   """Rellena la columna con la URL almacenada en el atributo 'page_url'."""
#   cells.insert(2, getattr(report, 'page_url', '-'))

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  options = Options()
  service = Service()
  # options.addArguments("--incognito") # para que el navegador inicie en incognito
  # configuraciones para github
  options.add_argument("--no-sandbox") 
  options.add_argument("--disable-gpu") 
  options.add_argument("--window-size=1920x1080")
  options.add_argument("--headless=new")
  
  driver = webdriver.Chrome(service=service, options=options)
  yield driver
  driver.quit()
    

# coso del nuevo Page Object Model
@pytest.fixture
def valid_credentials():
  return ("standard_user","secret_sauce")

@pytest.fixture
def invalid_credentials():
  return ("error_user","secret_sauce")

@pytest.fixture
def valid_credentials():
  return ("locked_out_user","secret_sauce")

# api
@pytest.fixture
def url_base_reqres():
  return "https://reqres.in/api"

@pytest.fixture
def reqres_api_key():
  return "reqres_e22ecf95077349eab7badb0c6c68a17e"

# captura de pantalla
# las capturas solo se harán en caso de error
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
  outcome = yield
  
  # obtenemos la información que esta al final de la prueba/cuando sucede un error
  report = outcome.get_result()
  
  # si ocurre un error durante la preparación(setup) del test o si ocurre durante(call) la ejecución del test
  if report.when in ("setup","call") and report.failed:
    driver = item.funcargs.get("driver")
    if driver:
      # el nombre del archivo comenzará con el nombre del test que dió error, ej test_login....
      test_name = item.name.split("[")[0]
      # usamos la fecha exacta en la que ocurrió el error como parte del nombre de la foto a guardar
      timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
      # creamos el nombre de la imagen a guardar con el momento en que el test falló y nombre del test
      file_name = target / f"{test_name}_FAIL_{timestamp}.png"
      
      try:
        # guardamos la foto
        driver.save_screenshot(str(file_name))
        logger.warning(f"Screenshot Pytest guardado: {file_name}")
        
        if hasattr(report, 'extra'):
          report.extra = getattr(report, 'extra', [])
          report.extra.append({
            'name': 'screenshot',
            'format': 'image',
            'content': str(file_name)
            })
          
      except Exception as e:
        logger.error(f"Error al capturar pantalla en Pytest: {e}")
      