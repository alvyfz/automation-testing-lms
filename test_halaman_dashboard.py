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


def test_course_card_dashboard(driver):
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
        By.XPATH, '//a[@data-title="mymoodle,admin"]').click()
    sleep(3)
    course_card = driver.find_element(By.CLASS_NAME, "card")
    assert course_card is not None
    clickable_card_course = driver.find_element(
        By.XPATH, ' (//a[@class ="aalink coursename mr-2"])[1]')
    clickable_card_course.click()
    announcement_on_course = driver.find_element(
        By.XPATH, '//div[@class="activityinstance"]')
    assert announcement_on_course is not None
# (//section)[3] == //section[@id="inst30103"]


def test_custom_section_course(driver):
    # it should be different in every account
    list_section = ['inst30101', 'inst30102',
                    'inst30103', 'inst30104', 'inst30105']
    section_selected = random.choice(list_section)
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
        By.XPATH, '//a[@data-title="mymoodle,admin"]').click()
    sleep(3)
    course_card = driver.find_element(By.CLASS_NAME, "card")
    assert course_card is not None
    driver.find_element(
        By.XPATH, '//*[@type="submit"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//section[@id="' + section_selected + '"]//div[@class="action-menu-item"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//ul[@class="dragdrop-keyboard-drag"]//li[1]//a').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '/html/body/div[6]/div[2]/header/div/div/div/div[2]/div[1]/div[2]/form/button').click()
    sleep(1)
    section_customed = driver.find_element(
        By.XPATH, '//section[@id="' + section_selected + '"]')
    first_section = driver.find_element(By.XPATH, '(//section)[2]')
    # check first section is selected section its move to first section
    assert section_customed == first_section
