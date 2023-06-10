import os
import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant
import utils

characters = string.ascii_letters + string.digits + string.punctuation
randomString = ''.join(random.choice(characters) for i in range(8))
profile_description = 'test_' + randomString + '_profile_description'
change_password = 'Fauzi2903200!'


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()    
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_edit_profile(driver):
    utils.login(driver)
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

def test_change_password(driver):
    utils.login(driver)
    change_password_step(driver, constant.PASSWORD, change_password)
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(change_password + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    change_password_step(driver, change_password, constant.PASSWORD)
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(change_password + Keys.ENTER)
    alert = driver.find_element(By.CLASS_NAME, 'alert')
    assert alert is not None
    
def change_password_step(driver, old_password, new_password):
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="profile,moodle"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//a[@id="action-menu-toggle-2"]').click()
    sleep(1)  
    driver.find_element(By.XPATH, '(//div[@class="dropdown-item"])[2]').click()
    driver.find_element(By.XPATH,'(//input[@type="password"])[1]').send_keys(old_password)
    driver.find_element(By.XPATH,'(//input[@type="password"])[2]').send_keys(new_password)
    driver.find_element(By.XPATH,'(//input[@type="password"])[3]').send_keys(new_password)
    driver.find_element(By.XPATH, '//input[@name="submitbutton"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(1)
    utils.logout(driver)