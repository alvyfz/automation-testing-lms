import os
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
    utils.login(driver)
    sleep(3)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/user/files.php"]').click()
    # url = driver.current_url
    # assert url == 'https://elearning.ibik.ac.id/user/files.php'
    sleep(3)
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
    sleep(6)
    file_uploaded = driver.find_element(
        By.XPATH, '//span[contains(text(),"' + file_name + constant.FILE_TYPE + '")]')
    assert file_uploaded is not None
    utils.logout(driver)

def test_download_private_file(driver):
    utils.login(driver)
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/user/files.php"]').click()
    # url = driver.current_url
    # assert url == 'https://elearning.ibik.ac.id/user/files.php'
    sleep(3)
    file_uploaded = driver.find_element(
        By.XPATH, '//a//span[contains(text(),"' + file_name + constant.FILE_TYPE + '")]')
    file_uploaded.click()
    sleep(1)
    driver.find_element(By.XPATH,'//button[@class="fp-file-download btn btn-secondary"]').click()
    sleep(2)
    while not os.path.exists(constant.FILE_PATH_DOWNLOADS + file_name + constant.FILE_TYPE ):
        sleep(1)

    if os.path.isfile(constant.FILE_PATH_DOWNLOADS + file_name + constant.FILE_TYPE):
        assert os.path.isfile(constant.FILE_PATH_DOWNLOADS + file_name + constant.FILE_TYPE) is not None
        sleep(2)
        utils.logout(driver)
    else:
        Assert.assertFalse("%s isn't a file!" % constant.FILE_PATH_DOWNLOADS + file_name + constant.FILE_TYPE)


def test_folder_private_test(driver):
    # create a folder and move file uploaded  to the folder was created
    utils.login(driver)
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@href="https://elearning.ibik.ac.id/user/files.php"]').click()
    # url = driver.current_url
    # assert url == 'https://elearning.ibik.ac.id/user/files.php'
    sleep(3)
    driver.find_element(By.XPATH, '//a[@title="Create folder"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[@class="fp-mkdir-dlg-text"]//input').send_keys(file_name)
    driver.find_element(By.XPATH, '//button[@class="fp-dlg-butcreate btn-primary btn"]').click()
    sleep(1)
    file_uploaded = driver.find_element(
        By.XPATH, '//a//span[contains(text(),"' + file_name + constant.FILE_TYPE + '")]')
    file_uploaded.click()
    driver.find_element(By.XPATH, '//select[@class="custom-select form-control"]/option[contains(text(),"' + file_name + '")]').click()
    driver.find_element(By.XPATH, '//button[@class="fp-file-update btn-primary btn"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//span//input[@value="Save changes"]').click()
    sleep(1)
    assert file_uploaded is not None
    utils.logout(driver)

