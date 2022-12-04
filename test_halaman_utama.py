import random
import string
from ast import Assert
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_login(driver):
    driver.find_element(
        By.ID, 'username').send_keys('192310009')
    driver.find_element(
        By.ID, 'password').send_keys('Fauzi29030!' + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None


def test_course_card(driver):
    driver.find_element(
        By.ID, 'username').send_keys('192310009')
    driver.find_element(
        By.ID, 'password').send_keys('Fauzi29030!' + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    course_card = driver.find_element(By.CLASS_NAME, "card")
    assert course_card is not None
    button_course_card = driver.find_element(
        By.XPATH, '(//a[@class="card-link btn btn-primary"])[1]')
    button_course_card.click()
    enroll_page = driver.find_element(By.CSS_SELECTOR, "h2")
    assert enroll_page.text == "Enrolment options"


def test_pengumuman(driver):
    try:
        driver.find_element(
            By.ID, 'username').send_keys('192310009')
        driver.find_element(
            By.ID, 'password').send_keys('Fauzi29030!' + Keys.ENTER)
        assert "Elearning" in driver.title
        banner = driver.find_element(
            By.XPATH, '//div/img')
        assert banner is not None
        pengumuman = driver.find_element(By.ID, "site-news-forum")
        assert pengumuman is not None
        link_download_pengumuman = driver.find_element(
            By.XPATH, "//article[@id='p2']/div/div/div/div[2]/div[2]/a")
        link_download_pengumuman.click()
    except:
        Assert.assertFalse("Download failed")

# testing chat send and received message
  # driver.find_element(By.XPATH, '//a[@data-title="logout,moodle"]').click()
    # driver.find_element(
    #     By.XPATH, '(//i[@class="icon fa slicon-bubble fa-fw "])[1]').click()
    # driver.find_element(
    #     By.XPATH, '//a[@data-user-id="4041"]').click()
    # driver.find_element(
    #     By.XPATH, '//textarea').send_keys(randomString + Keys.ENTER)
    # message_sends = driver.find_element(
    #     By.XPATH, "//*[text()={}]".format(randomString))
    # print(message_sends)


def test_chat(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.ID, 'username').send_keys('192310009')
    driver.find_element(
        By.ID, 'password').send_keys('Fauzi29030!' + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
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
