from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "C:/Users/Anna/Development/chromedriver.exe"
game_page = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_drive_path)
driver.get(game_page)

