from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.parametrize("username, password", [("standard_user","secret_sauce")])
def test_add_product_to_cart(driver,username,password):
  try:
    LoginPage(driver).openPage().do_complete_login(username,password)
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
  except Exception as e:
    print(f"Error en test_product_interaction: {e}")
    raise
  
"""
def test_add_product_to_cart(login_in_driver):
  try:
    driver = login_in_driver
    
    # Espera explícita para garantizar que los productos existen
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    
    cart_btn = driver.find_element(By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
    
    btn_primer_elem = driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    btn_primer_elem.click()
    
    #esperar a que aparezca el badge de carrito
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    #confirmar que dice 1
    assert cart_badge.text == '1'
    
    # verificar que hay un elemento en el carrito
    cart_btn.click()
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-item"]'), "No hay elemento en carrito"
  except Exception as e:
    print(f"Error en test_product_interaction: {e}")
    raise
    
"""