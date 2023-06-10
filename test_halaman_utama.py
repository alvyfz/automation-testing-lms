import random
import string
from ast import Assert
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
    driver.maximize_window()    
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(driver):
    utils.login(driver)
    utils.logout(driver)


def test_course_card(driver):
    utils.login(driver)
    course_card = driver.find_element(By.CLASS_NAME, "card")
    assert course_card is not None
    course_button = driver.find_element(
        By.XPATH, '(//h4//a)[1]')
    course_button.click()
    sleep(5)
    enroll_page = driver.find_element(By.CSS_SELECTOR, "h2")
    assert enroll_page.text == "Enrolment options"
    utils.logout(driver)


def test_pengumuman(driver):
    try:
        utils.login(driver)
        pengumuman = driver.find_element(By.ID, "site-news-forum")
        assert pengumuman is not None
        link_download_pengumuman = driver.find_element(
            By.XPATH, "//article[@id='p2']/div/div/div/div[2]/div[2]/a")
        link_download_pengumuman.click()
        utils.logout(driver)
    except:
        Assert.assertFalse("Download failed")


def test_chat_send_and_received(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    utils.login(driver)
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="messages,message"]').click()
    sleep(3)
    driver.find_element(
        By.XPATH, '//a[@class="py-0 px-2 d-flex list-group-item list-group-item-action align-items-center"]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//textarea[@data-region="send-message-txt"]').send_keys(randomString + Keys.ENTER)
    sleep(10)
    assert driver.find_element(
        By.XPATH, '//p[contains(text(),"' + randomString + '")]') is not None
    utils.logout(driver)
