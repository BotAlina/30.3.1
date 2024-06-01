from selenium import webdriver
import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_show_my_pets():
   # Вводим email, пароль, открываем главную страницу сайта
   pytest.driver.find_element_by_id('email').send_keys('valid_email')
   pytest.driver.find_element_by_id('pass').send_keys('valid_password')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

def test_show_my_pets():

      element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

      pytest.driver.find_element_by_id('email').send_keys(valid_email)

      element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))

      pytest.driver.find_element_by_id('pass').send_keys(valid_password)

      element = WebDriverWait(pytest.driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

      pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

      element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

      pytest.driver.find_element_by_link_text("Мои питомцы").click()


      assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
