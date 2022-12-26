import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant

characters = string.ascii_letters + string.digits + string.punctuation
randomString = ''.join(random.choice(characters) for i in range(8))
file_name = 'test_' + randomString


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_upload_file(driver):
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(constant.PASSWORD + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    sleep(3)
    driver.find_element(
        By.XPATH, '//button[@aria-controls="nav-drawer"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/user/files.php"]').click()
    url = driver.current_url
    assert url == 'https://elearning.ibik.ac.id/user/files.php'
    sleep(5)
    driver.find_element(
        By.XPATH, '//a[@title="Add..."]').click()
    sleep(1)
    button_upload = driver.find_element(
        By.XPATH, '//input[@type="file"]')
    button_upload.send_keys(constant.FILE_PATH)
    form_title = driver.find_element(
        By.XPATH, '//input[@name="title"]')
    form_title.send_keys(file_name)
    driver.find_element(
        By.XPATH, '//button[@class="fp-upload-btn btn-primary btn"]').click()
    sleep(4)
    driver.find_element(
        By.XPATH, '//input[@id="id_submitbutton"]').click()
    sleep(10)
    file_uploaded = driver.find_element(
        By.XPATH, '//span[contains(text(),"' + file_name + constant.FILE_TYPE + '")]')
    assert file_uploaded is not None
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="logout,moodle"]').click()
    sleep(3)
