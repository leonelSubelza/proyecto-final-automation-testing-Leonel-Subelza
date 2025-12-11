from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

@pytest.mark.parametrize("username, password", [("standard_user","secret_sauce")])
def test_add_product_to_cart(driver,username,password):
  try:
    logger.warning("-----Ejecutando test_cart.py-----")
    logger.info("Realizando login válido...")
    LoginPage(driver).openPage().do_complete_login(username,password)
    logger.info("Login válido realizado correctamente")
    inventory_page = InventoryPage(driver)
    
    # Espera explícita para garantizar que los productos existen
    inventory_page.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    
    inventory_page.add_item_by_index(0)
    # inventory_page.add_item_by_name("Sauce Labs Backpack")
    
    #esperar a que aparezca el badge de carrito
    #confirmar que dice 1
    assert inventory_page.get_total_items_in_cart() == 1
    
    # verificar que hay un elemento en el carrito
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    assert cart_page.get_cart_items(), "No hay elemento en carrito"
    logger.info("-----test_cart.py ejecutado correctamente-----")
  except Exception as e:
    print(f"Error en test_cart: {e}")
    logger.error(f"Error durante el test_cart: {e}")
    raise