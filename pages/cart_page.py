from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
  _URL = "https://www.saucedemo.com/cart.html"
  
  _CART_ITEM = (By.CSS_SELECTOR, "[data-test='inventory-item']") 
  
  _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
  
  def __init__(self,driver):
    self.driver = driver
    self.wait = WebDriverWait(driver,10)
    
  def get_cart_items(self):
    return self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM))
  
  def get_item_name(self,item):
    return item.find_element(*self._ITEM_NAME)
  
  def remove_item(self,item):
    item_name = self.get_item_name(item)
    css_selector = self.get_id_of_remove_btn(item_name)
    item_remove_btn = item.find_element(By.CSS_SELECTOR, f"[data-test='{css_selector}']")
    item_remove_btn.click()
    
  def get_id_of_remove_btn(item_name):
    slug = item_name.lower().replace(" ", "-")
    return f"remove-{slug}"