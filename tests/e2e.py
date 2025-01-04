from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:5000"

def test_scores_service(URL):
    driver = webdriver.Chrome()
    driver.get(URL)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'score')))
    score = int(element.text)
    if(0 <= score <= 1000):
        driver.quit()
        return True
    else:
        driver.quit()
        return False


def main_funtction():
    if(test_scores_service(URL)):
        return 0
    else:
        return -1