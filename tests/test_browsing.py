from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_page

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
    login = LoginPage(driver).openPage().do_complete_login(username,password)
    # Espera explícita para garantizar que los productos existen
    # wait = WebDriverWait(driver, 10)
    inventory_page = Inventory_page(driver)
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
    
    """
    # validar titulo
    products_txt = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')
    assert "Products" in products_txt.text
    
    # Validar presencia de productos 
    assert driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-backpack"]'), "Primer producto no encontrado"
    # Nombre y precio del primero
    assert driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item-name"]')[0].text == 'Sauce Labs Backpack' , "Titulo de Primer producto incorrecto"
    assert driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item-price"]')[0].text == '$29.99' , "Precio de Primer producto incorrecto"
    
    # validar presencia de elementos importantes
    assert driver.find_element(By.ID,'react-burger-menu-btn'), "Botón menú no encontrado"
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="product-sort-container"]'), "Filtro no encontrado"
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'), "Carrito no encontrado"
       else:
      assert "Epic sadface" in driver.page_source
      """
  except Exception as e:
    print(f"Error en test_browsing: {e}")
    raise