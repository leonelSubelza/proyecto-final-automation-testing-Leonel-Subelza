import pytest
from selenium import webdriver
from utils.saucedemo import login
from pages.login_page import LoginPage

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()
  
# @pytest.fixture
# def login_in_driver(driver,username,password):
#   LoginPage(driver).openPage().do_complete_login(username,password)
#   return driver
  

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


