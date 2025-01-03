from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://foodfrillz.com/")
element1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/section[2]/div/div/div/div[3]/div/div[1]/div/div[1]/div/div[5]/div/div[1]/a/div/img"))
)
element1.click()
element2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/section[1]/div/div[2]/div/div[3]/div/div/form/div[2]/button[2]"))
)
element2.click()
element3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/form/div[1]/div[1]/div/div[2]/input"))
)
element3.send_keys("abhigyanseth03@gmail.com")
driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/form/div[1]/div[2]/div/div/input").send_keys("Gyan@1506")
driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div[1]/form/div[3]/button").click()
time.sleep(5)
