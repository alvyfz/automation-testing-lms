import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    yield driver
    driver.quit()


def test_googling(driver):
    driver.find_element(By.NAME, 'q').send_keys('Alvy Fauzi' + Keys.ENTER)
    assert "Alvy Fauzi" in driver.title
    assert "Alvy Fauzi" in driver.find_element(By.CSS_SELECTOR, 'H3').text
