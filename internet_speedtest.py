# This project will check internet speed and send an email with the up and the down speed
from selenium import webdriver
import time
import smtplib

CHROME_DRIVE_PATH = user_chrome_drive_path
speedtest_webpage = "https://www.speedtest.net/"

USER = user_password
PASSWORD = user_password


class InternetSpeedTwitterBot:
    def __init__(self, drive_path):
        self.driver = webdriver.Chrome(drive_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(speedtest_webpage)

        """Consent button"""
        consent = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        consent.click()

        """Start button"""
        start_test = self.driver.find_element_by_css_selector(".start-button a")
        start_test.click()

        time.sleep(50)

        # down value
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # up value
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def send_email_with_results(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(
                from_addr=USER,
                to_addrs=person_email,
                msg=f"Internet speed. Up: {self.up}, down: {self.down}")


bot = InternetSpeedTwitterBot(CHROME_DRIVE_PATH)

bot.get_internet_speed()
bot.send_email_with_results()

