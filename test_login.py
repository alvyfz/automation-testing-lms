import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://elearning.ibik.ac.id/login/index.php')
    yield driver
    driver.quit()


def test_login_logout(driver):
    driver.find_element(
        By.ID, 'username').send_keys('192310009')
    driver.find_element(
        By.ID, 'password').send_keys('Fauzi29030!' + Keys.ENTER)
    assert "Elearning" in driver.title
    banner = driver.find_element(
        By.XPATH, '//div/img')
    assert banner is not None
    driver.find_element(By.ID, 'action-menu-toggle-1').click()
    driver.find_element(By.XPATH, '//a[@data-title="logout,moodle"]').click()
    sleep(2)
    header_login = driver.find_element(
        By.XPATH, '//a[contains(text(),"Log in")]')
    assert header_login is not None
