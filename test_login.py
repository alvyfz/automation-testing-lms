import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant
import utils


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_logout(driver):
    utils.login(driver)
    utils.logout(driver)



def test_login_with_wrong_username_and_wrong_password(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.ID, 'username').send_keys(randomString)
    driver.find_element(
        By.ID, 'password').send_keys(randomString + Keys.ENTER)
    alert = driver.find_element(By.CLASS_NAME, 'alert')
    assert alert is not None

def test_login_with_correct_username_and_wrong_password(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(randomString + Keys.ENTER)
    alert = driver.find_element(By.CLASS_NAME, 'alert')
    assert alert is not None

def test_login_with_wrong_username_and_correct_password(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.ID, 'username').send_keys(randomString)
    driver.find_element(
        By.ID, 'password').send_keys(constant.PASSWORD + Keys.ENTER)
    alert = driver.find_element(By.CLASS_NAME, 'alert')
    assert alert is not None