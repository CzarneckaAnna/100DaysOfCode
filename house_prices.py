"""This project will gather information about houses price and url link of houses, which pass selected criteria.
House Criteria:
1. House type: "Domy"
2. Operation type: "na sprzedaż"
3. Region: "dolnośląskie"

Get information about:
1. Address
2. Price
3. Size of house
4. Url address
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import requests
from bs4 import BeautifulSoup

CHROME_DRIVE_PATH = DEFINE_PATH
web_side_address = "https://www.otodom.pl/"

houses_list_url = "https://www.otodom.pl/sprzedaz/dom/dolnoslaskie/?search%5Bregion_id%5D=1"
form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfVtVjWGys8rrZ8HVFY3kiTCM_jajrEPoAhbYuNJIBJ_NeeMA/viewform?usp=sf_link"

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
select_region.click()
region = select_region.find_element_by_xpath("//*[@id='downshift-0-item-2']/span").click()

# click search button
# option 1: accept_search_button = page.find_element_by_id("downshift-1-toggle-button").submit()
accept_search_button = page.find_element_by_xpath("/html/body/main/section[1]/div/div/div/div/div/form/div[1]/div[3]/button").click()

# add: sort by date (from the newest to the oldest one)
# sort_parameter = page.find_element_by_xpath("/html/body/div[3]/main/section[2]/div/div/div[1]/div/div[1]/div[2]/div/button")
# sort_parameter.click()
# select_date_sort = sort_parameter.find_element_by_xpath("/html/body/div[3]/main/section[2]/div/div/div[1]/div/div[1]/div[2]/div/ul/li[2]/a")
# select_date_sort.click()


# prepare list of houses address, price and url address.
response = requests.get(houses_list_url)
houses = response.text

houses_list = BeautifulSoup(houses, "html.parser")
house = houses_list.find_all(name="article")

form = webdriver.Chrome(CHROME_DRIVE_PATH)
form.get(form_link)

for home in house:
    question_1 = form.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_1.send_keys(home.find(name="p", class_="text-nowrap").getText())

    question_2 = form.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_2.send_keys(home.find(name="li", class_="offer-item-price").getText().strip())

    question_3 = form.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_3.send_keys(home.find(name="li", class_="hidden-xs offer-item-area").getText())

    question_4 = form.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
    question_4.send_keys(home.find(name="a").get("href"))

    submit_button = form.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span").click()
    add_new_record = form.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()

form.close()
page.close()










