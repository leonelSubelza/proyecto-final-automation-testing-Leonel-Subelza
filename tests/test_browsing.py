from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger
import pytest


""" 
* Las funciones fixture son tratadas como inyeccion de dependencias (como Beans en Spring), cada una vive en el contexto de la aplicacion al momento de la ejecución
* Los valores parametrizados viven cada uno por cada 'iteracion' supongo, en una primera instancia se tomaran los primeros valores para ejecutar la funcion y python los puede usar/manejar como si fuesen valores globales, es decir, si username y password son argumentos de algun fixture entonces usara estos valores para ese fixture
Python instancia los fixture y los valores parametricados implicitamente. En tiempo de ejecucion, para los primeros valores del fixture hace:

  driver_instance = driver()
  username="standard_user"
  password="secret_sauce"
  must_work=True
  login_in_driver_instance = login_in_driver(driver_instance, username, password)
  test_login(login_in_driver_instance, username, password, must_work)
"""


@pytest.mark.parametrize("username, password", [("standard_user","secret_sauce")])
def test_browsing(driver,username,password):
  try:
    logger.warning("-----Ejecutando test_browsing.py-----")
    logger.info("Realizando login válido...")
    login = LoginPage(driver).openPage().do_complete_login(username,password)
    logger.info("Login válido realizado correctamente")
    # Espera explícita para garantizar que los productos existen
    # wait = WebDriverWait(driver, 10)
    inventory_page = InventoryPage(driver)
    inventory_page.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    
    # validar titulo
    assert inventory_page.get_page_title() in "Products"
    
    # Validar presencia de productos 
    first_item = inventory_page.get_item_by_index(0)
    assert first_item, "Primer producto no encontrado"
    # Nombre y precio del primero
    assert inventory_page.get_item_title(first_item) == 'Sauce Labs Backpack' , "Titulo de Primer producto incorrecto"
    assert len(inventory_page.get_items()) > 0, "No hay productos cargados"
    assert inventory_page.get_item_price(first_item) == '$29.99' , "Precio de Primer producto incorrecto"
    
    # validar presencia de elementos importantes
    assert inventory_page.get_burguer_menu_btn(), "Botón menú no encontrado"
    assert inventory_page.get_filter_btn(), "Filtro no encontrado"
    assert inventory_page.get_shopping_cart_btn(), "Carrito no encontrado"
    logger.info("-----test_browsing.py ejecutado correctamente-----")
  except Exception as e:
    print(f"Error en test_browsing: {e}")
    logger.info(f"Error en test_browsing.py: {e}")
    raise