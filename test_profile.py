import os
import random
import string
from ast import Assert
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant

characters = string.ascii_letters + string.digits + string.punctuation
randomString = ''.join(random.choice(characters) for i in range(8))
profile_description = 'test_' + randomString + '_profile_description'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_edit_profile(driver):
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(constant.PASSWORD + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="profile,moodle"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[@id="action-menu-toggle-2"]').click()
    sleep(1)  
    driver.find_element(By.XPATH, '(//div[@class="dropdown-item"])[1]').click()
    driver.find_element(
        By.ID, 'id_description_editoreditable').send_keys(Keys.CONTROL + "a")
    driver.find_element(
        By.ID, 'id_description_editoreditable').send_keys(Keys.DELETE)       
    driver.find_element(
        By.ID, 'id_description_editoreditable').send_keys(profile_description)
    driver.find_element(By.XPATH, '//input[@name="submitbutton"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '(//div[@class="card-text"]//a)[1]').click()
    profile_updated =driver.find_element(By.XPATH, '//p[contains(text(),"' + profile_description + '")]')
    assert profile_updated is not None
    sleep(1)
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="logout,moodle"]').click()
    sleep(3)