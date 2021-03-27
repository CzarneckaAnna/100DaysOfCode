from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""This project will create bot, which will play cookie game."""
chrome_drive_path = "C:/Users/Anna/Development/chromedriver.exe"
game_page = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_drive_path)
driver.get(game_page)

# the game (game_time) lasts 5 minutes, every 5 seconds bot will buy the most expensive, affordable upgrade.
game_time = time.time() + 1 * 60
buy_time = time.time() + 5

cookie_click = driver.find_element_by_id("cookie")

upgrade_items = driver.find_element_by_id("store")
upgrades_list = {}
upgrades_list = [item.text.split(sep=" - ") for item in upgrade_items.find_elements_by_css_selector("b")]

while True:
    cookie_click.click()

    if time.time() >= buy_time:
        money = driver.find_element_by_id("money").text.replace(",", "")
        buy_time += 5
        print(f"end game:{game_time}")
        print(f"time: {time.time()}")

    # TODO 4: Every 5 seconds, check if it's possible to buy upgrade - if yes, select the most expensive from available.

    if time.time() > game_time:
        results = driver.find_element_by_id("cps").text
        print(results)
        break




