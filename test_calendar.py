import os
from ast import Assert
from time import sleep


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

import constant
import utils

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


calendar_name = 'test_calendar_' + datetime.now().strftime("%d%m%Y%H%M%S")


def test_export_calendar(driver):
    utils.login(driver)
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/calendar/view.php?view=month"]').click()
    driver.find_element( By.XPATH, '//button[contains(text(),"Export calendar")]').click()
    sleep(1)
    driver.find_element( By.XPATH, '(//label[@class="form-check-inline form-check-label  fitem  "])[1]').click()
    driver.find_element( By.XPATH, '(//label[@class="form-check-inline form-check-label  fitem  "])[6]').click()
    driver.find_element(By.XPATH,'//input[@value="Export"]').click()
    sleep(2)
    while not os.path.exists(constant.FILE_PATH_DOWNLOADS + "icalexport.ics" ):
        sleep(1)

    if os.path.isfile(constant.FILE_PATH_DOWNLOADS + "icalexport.ics"):
        assert os.path.isfile(constant.FILE_PATH_DOWNLOADS + "icalexport.ics") is not None
        sleep(2)
        utils.logout(driver)
    else:
        Assert.assertFalse("%s isn't a file!" % constant.FILE_PATH_DOWNLOADS + "icalexport.ics")

    sleep(3)
    utils.logout(driver)


def test_import_calendar(driver):
    utils.login(driver)
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/calendar/view.php?view=month"]').click()
    driver.find_element( By.XPATH, '//button[contains(text(),"Manage subscriptions")]').click()
    driver.find_element(By.ID, 'id_name').send_keys(calendar_name)
    driver.find_element(By.XPATH, '//select[@id="id_importfrom"]//option[@value="0"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//input[@name="importfilechoose"]').click()
    sleep(1)
    button_upload = driver.find_element(
        By.XPATH, '//input[@type="file"]')
    button_upload.send_keys(constant.ICS_PATH)
    # driver.find_element(By.NAME, 'repo_upload_file').send_keys(calendar_name)
    driver.find_element(By.XPATH, '//button[contains(text(), "Upload this file")]').click()
    sleep(1)
    alert_success = driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    sleep(1)
    alert_success = driver.find_element(By.XPATH, '//div[@class="alert alert-info alert-block fade in "]')
    alert_success is not None
    sleep(1)
    utils.logout(driver)


def test_create_event(driver):
    utils.login(driver)
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/calendar/view.php?view=month"]').click()  
    driver.find_element(
        By.XPATH, '//button[contains(text(),"New event")]').click()
    sleep(2)
    driver.find_element(By.ID, 'id_name').send_keys(calendar_name)
    driver.find_element(
        By.XPATH, '//button[contains(text(),"Save")]').click()
    sleep(4)
    event =  driver.find_element(By.XPATH, '//a[@title="' + calendar_name + '"]')
    event is not None
    utils.logout(driver)
