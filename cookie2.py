from selenium import webdriver
import time

chrome_drive_path = YOUR_PATH
game_page = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(chrome_drive_path)
driver.get(game_page)

# the game (game_time) lasts 5 minutes, every 5 seconds bot will buy the most expensive, affordable upgrade.
game_time = time.time() + 5 * 60
buy_time = time.time() + 5

cookie_click = driver.find_element_by_id("cookie")

upgrade_items = driver.find_element_by_id("store")
upgrades_list = {}
upgrades_list = [item.text.split(sep=" - ") for item in upgrade_items.find_elements_by_css_selector("b")]

while True:
    cookie_click.click()

    if time.time() >= buy_time:
        money = int(driver.find_element_by_id("money").text.replace(",", ""))

        for price in range(len(upgrades_list) - 1):
            item_price = int(upgrades_list[price][1].replace(",", ""))
            if money >= item_price:
                upgrade = upgrades_list[price][0]

        if upgrade != "":
            selected_upgrade = driver.find_element_by_id(f"buy{upgrade}")
            selected_upgrade.click()

        buy_time += 5

    if time.time() > game_time:
        results = driver.find_element_by_id("cps").text
        print(results)
        break