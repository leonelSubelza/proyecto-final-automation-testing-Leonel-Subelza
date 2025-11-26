from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
  _URL = "https://www.saucedemo.com/inventory.html"
  
  _TITLE = (By.CSS_SELECTOR, "[data-test='title']")
  
  _INVENTORY_ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-list']")
  # _INVENTORY_ITEM = (By.CSS_SELECTOR, "data-test='inventory-item'")
  
  _BURGUER_MENU_BTN = (By.ID,'react-burger-menu-btn')
  _FILTER_BTN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
  
  _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
  _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
  
  _ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
  _ITEM_PRICE = (By.CSS_SELECTOR,'[data-test="inventory-item-price"]')
  _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
  
  _LOGOUT_BUTTON =(By.CSS_SELECTOR,'[data-test="logout-sidebar-link"]') 
  
  def __init__(self,driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)
  
  # def openPage(self):
  #   self.driver.get(self.URL)
  #   return self
  
  def get_page_title(self):
    """Obtiene el título de la página de inventario"""
    element_title = self.wait.until(EC.visibility_of_element_located(self._TITLE))
    # login.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))  
    return element_title.text
  
  def get_items(self):
    self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
    inventory_list = self.driver.find_elements(*self._INVENTORY_ITEMS)
    return inventory_list
  
  def get_total_items_count(self):
    self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
    inventory_list = self.driver.find_elements(*self._INVENTORY_ITEMS)
    return len(inventory_list)
  
  def get_items_names(self):
    items = self.driver.find_elements(*self._INVENTORY_ITEMS)
    return [item_name.text for item_name in items]
  
  def add_item_by_index(self,index):
    item_selected = self.get_item_by_index(index)
    
    item_button = item_selected.find_element(*self._ADD_TO_CART_BUTTON)
    item_button.click()
    return self
  
  def add_item_by_name(self,name):
    item_selected = self.get_item_by_name(name)
    
    item_button = item_selected.find_element(*self._ADD_TO_CART_BUTTON)
    item_button.click()
    return self
  
  def get_total_items_in_cart(self):
    try:
      self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
      cart_count = self.driver.find_element(*self._CART_BADGE)
      return int(cart_count.text)
    except:
      return 0
  
  def get_item_by_index(self,index):
    if index < 0:
      raise Exception(f"Index of item selected not valid, index:{index}")
    items = self.get_items()
    item_selected = items[index]
    if not item_selected:
      raise Exception(f"Item not found by index: {index}")
    return item_selected
  
  def get_item_by_name(self,name):
    items = self.get_items()
    item_selected = None
    for item in items:
      if(item.find_element(*self._ITEM_NAME).text.strip() == name.strip()):
        item_selected = item
    
    if(not item_selected):
      raise Exception(f"Item not found by name {name}")
    return item_selected
  
  def get_item_title(self,item):
    return item.find_element(*self._ITEM_NAME).text
  
  def get_item_price(self,item):
    return item.find_element(*self._ITEM_PRICE).text
  
  def get_burguer_menu_btn(self):
    return self.driver.find_element(*self._BURGUER_MENU_BTN)
  
  def get_filter_btn(self):
    return self.driver.find_element(*self._FILTER_BTN)
  
  def get_shopping_cart_btn(self):
    return self.driver.find_element(*self._CART_LINK)
  
  def go_to_cart(self):
    self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
    return self
  
  def logout(self):
    self.get_burguer_menu_btn().click()
    self.wait.until(EC.visibility_of_element_located(self._LOGOUT_BUTTON)).click()
    return self