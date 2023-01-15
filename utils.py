from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant

def login(driver):
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(constant.PASSWORD + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    
def logout(driver):
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//a[@data-title="logout,moodle"]').click()
    sleep(1)
    header_login = driver.find_element(
        By.XPATH, '//a[contains(text(),"Log in")]')
    assert header_login is not None
    sleep(2)

