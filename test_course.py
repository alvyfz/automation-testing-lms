from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_course_announcement(driver):
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
        By.XPATH, '//a[@data-title="mymoodle,admin"]').click()
    sleep(3)
    course_card = driver.find_element(By.CLASS_NAME, "card")
    assert course_card is not None
    clickable_card_course = driver.find_element(
        By.XPATH, ' (//a[@class ="aalink coursename mr-2"])[1]')
    clickable_card_course.click()
    driver.find_element(
        By.XPATH, '(//a[@class="aalink"])[1]').click()
    announcement = driver.find_element(
        By.XPATH, '//h2[contains(text(),"Announcements")]')
    assert announcement is not None
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    driver.find_element(
        By.XPATH, '//a[@data-title="logout,moodle"]').click()
