import random
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


def test_course_card_dashboard(driver):
    utils.login(driver)
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
    utils.logout(driver)


def test_custom_section_course(driver):
    # it should be different on every account
    list_section = ['inst30101', 'inst30102',
                    'inst30103', 'inst30104', 'inst30105']
    section_selected = random.choice(list_section)
    utils.login(driver)
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
        By.XPATH, '(//button[@type="submit"])[2]').click()
    sleep(1)
    section_customed = driver.find_element(
        By.XPATH, '//section[@id="' + section_selected + '"]')
    first_section = driver.find_element(By.XPATH, '(//section)[2]')
    # check first section is selected section its move to first section
    assert section_customed == first_section
    utils.logout(driver)
