from selenium import webdriver
import pytest
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets():

   pytest.driver.find_element_by_id('email').send_keys('valid_email')
   pytest.driver.find_element_by_id('pass').send_keys('valid_password')

   pytest.driver.implicitly_wait(10)

   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


   images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
   names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
   descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')


   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

