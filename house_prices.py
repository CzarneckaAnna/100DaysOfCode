"""This project will gather information about houses price and url link of houses, which pass selected criteria.
House Criteria:
1. House type: "Domy"
2. Operation type: "na sprzedaż"
3. Region: "dolnośląskie"
4. sort by date: from the he newest to the oldest one
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup

CHROME_DRIVE_PATH = "C:/Users/Anna/Development/chromedriver.exe"
web_side_address = "https://www.otodom.pl/"

form_link = "https://docs.google.com/forms/d/e/1FAIpQLScak2BSckfTPXW1WmWTcp6yGjdOdrkjPKj7VP8k9fwzFFVkCA/viewform?usp=sf_link"

page = webdriver.Chrome(CHROME_DRIVE_PATH)
# page = webdriver.Chrome(ChromeDriverManager().install())
page.get(web_side_address)


# Cookie button - adding 1 second break since there was a problem with cookies information
# (without it program shows an error)
time.sleep(1)
accept_cookies = page.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']").click()
# accept_cookies.click()

# house type ("Mieszkania, Domy, ...")
house_type_selection = page.find_element_by_xpath("//*[@id='downshift-1-toggle-button']/span")
house_type_selection.click()
house_type = house_type_selection.find_element_by_xpath("//*[@id='downshift-1-item-1']").click()


# operation type (for sale or for rent)
operation_type = page.find_element_by_xpath("//*[@id='downshift-2-toggle-button']")
operation_type.click()
for_sale = operation_type.find_element_by_xpath("//*[@id='downshift-2-item-0']").click()

# region
select_area = page.find_element_by_xpath("//*[@id='downshift-0-label']/span")
select_area.click()
select_region = select_area.find_element_by_xpath("//*[@id='downshift-0-item-1']")
# select_region.click()
region = select_region.find_element_by_xpath("//*[@id='downshift-0-item-2']/span").click()

# click search button
# option 1: accept_search_button = page.find_element_by_id("downshift-1-toggle-button").submit()
accept_search_button = page.find_element_by_xpath("/html/body/main/section[1]/div/div/div/div/div/form/div[1]/div[3]/button").click()

# add: sort by date (from the newest to the oldest one)
sort_parameter = page.find_element_by_xpath("/html/body/div[3]/main/section[2]/div/div/div[1]/div/div[1]/div[2]/div/button")
sort_parameter.click()
select_date_sort = sort_parameter.find_element_by_xpath("/html/body/div[3]/main/section[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a")
select_date_sort.click()

# TODO 3.1: prepare house address list.
# TODO 3.2: prepare house price list.
# TODO 3.3: prepare house url list.
# TODO 4: update information in form_link.