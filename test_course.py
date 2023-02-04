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
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_course_announcement(driver):
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
    driver.find_element(
        By.XPATH, '(//a[@class="aalink"])[1]').click()
    announcement = driver.find_element(
        By.XPATH, '//h2[contains(text(),"Announcements")]')
    assert announcement is not None
    utils.logout(driver)

def test_course_attendance(driver):
    utils.login(driver)
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="mymoodle,admin"]').click()
    sleep(3)
    course_card = driver.find_element( By.XPATH, '//span[contains(text(),"Course untuk skripsi Alvy")]')
    assert course_card is not None
    course_card.click()
    driver.find_element( By.XPATH, '//span[contains(text(),"Attendance")]').click()
    driver.find_element( By.XPATH, '(//a[contains(text(),"Submit attendance")])[1]').click()
    driver.find_element( By.XPATH, '//span[contains(text(),"Hadir")]').click()
    driver.find_element( By.ID, 'id_submitbutton').click()
    sleep(1)
    attendance = driver.find_element( By.XPATH, '//td[contains(text(),"Hadir")]')
    assert attendance is not None
    utils.logout(driver)

def test_course_access_learning_material(driver):
    utils.login(driver)
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="mymoodle,admin"]').click()
    sleep(3)
    course_card = driver.find_element( By.XPATH, '//span[contains(text(),"Course untuk skripsi Alvy")]')
    assert course_card is not None
    course_card.click()
    driver.find_element( By.XPATH, '//span[contains(text(),"test akses materi")]').click()
    sleep(1)
    url = driver.current_url
    assert url == 'https://elearning.ibik.ac.id/pluginfile.php/55290/mod_resource/content/1/file%20test'
    driver.get('https://elearning.ibik.ac.id')
    utils.logout(driver)