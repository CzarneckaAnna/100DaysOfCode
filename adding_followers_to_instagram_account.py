"""This program will fallow all followers from selected account (SIMILAR_ACCOUNT)"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

INSTAGRAM_URL = "https://www.instagram.com/"
"""Update with you personal credential"""
CHROME_DRIVE_PATH = USER_CHROM_PATH
INSTAGRAM_LOGIN = USER_INSTAGRAM_LOGIN
INSTAGRAM_PASSWORD = USER_INSTAGRAM_PASSWORD
SIMILAR_ACCOUNT = ACCOUNT_SELECTED_BY_USER


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVE_PATH)

    def login(self):
        page = self.driver
        page.get(INSTAGRAM_URL)
        wait = WebDriverWait(page, 10)
        waiting_1 = wait.until(EC.invisibility_of_element_located((By.ID, "loginForm")))

        # cookies accept
        cookies = page.find_element_by_xpath("/html/body/div[2]/div/div/button[1]").click()

        time.sleep(2)
        # login to instagram
        login = page.find_element_by_name("username")
        password = page.find_element_by_name("password")

        login.send_keys(INSTAGRAM_LOGIN)
        password.send_keys(INSTAGRAM_PASSWORD)

        password.send_keys(Keys.ENTER)

        # information pop-aps:
        waiting_2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='react-root']/section/main/div/div")))
        save_login_data = page.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()

        waiting_3 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[4]/div/div/div")))
        notification_off = page.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    def find_followers(self):
        selected_page = self.driver
        selected_page.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
		        wait = WebDriverWait(selected_page, 10)

        followers = selected_page.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()									   

		waiting = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[5]/div/div/div[2]")))
        lists = followers.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

        for i in range(3):
            selected_page.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", lists)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            if button.text == "Obserwuj":
                button.click()
                time.sleep(2)
            else:
                pass																			


inst_page = InstaFollower()
inst_page.login()
inst_page.find_followers()
inst_page.follow()




