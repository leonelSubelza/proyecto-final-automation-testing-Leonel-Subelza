from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
  
  URL = "https://www.saucedemo.com/"
  
  _USERNAME_INPUT = (By.CSS_SELECTOR,'[data-test="username"]')
  _PASSWORD_INPUT = (By.CSS_SELECTOR,'[data-test="password"]')
  _LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
  _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
  
  def __init__(self,driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 10)
    # self.get(self.URL)
    # self.openPage()
    
  def openPage(self):
    self.driver.get(self.URL)
    return self
    
  def set_username_input(self,username):
    input = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
    input.clear()
    input.send_keys(username)
    return self
  
  def set_password_input(self,password):
    # input = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
    # al hacer *self._PASSWORD_INPUT estamos desempaquetando el valor de self._PASSWORD_INPUT que son dos valores encerrados en un parentesis, con el * pasaría a valer lo mismo pero sin paréntesis, que serían dos valores
    input = self.driver.find_element(*self._PASSWORD_INPUT)
    input.clear()
    input.send_keys(password)
    return self
  
  def click_login_button(self):
    self.driver.find_element(*self._LOGIN_BUTTON).click()
    return self
    
  def do_complete_login(self,username,password):
    self.set_username_input(username)
    self.set_password_input(password)
    self.click_login_button()
    return self
  
  def get_error_message_page(self):
    div_error = self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
    return div_error.text