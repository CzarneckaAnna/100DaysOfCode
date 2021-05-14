# This project will login to LinkedIn profile and save job offer for defined parameters.
# Job = Python developer, location = Wroclaw
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

linkedin_page = "https://www.linkedin.com/jobs/search/?geoId=105001681&keywords=Python%20developer&location=Wroc%C5%82aw%2C%20Woj.%20Dolno%C5%9Bl%C4%85skie%2C%20Polska"
chrome_drive_path = CHROME_DRIVE_PATH

linkedin_login = LINKEDIN_LOGIN
linkedin_password = LINKEDIN_PASSWORD

driver = webdriver.Chrome(chrome_drive_path)
driver.get(linkedin_page)

# login to application
login_to_linkedin = driver.find_element_by_class_name("nav__button-secondary")
login_to_linkedin.click()

login_input = driver.find_element_by_id("username")
login_input.send_keys(linkedin_login)

password_input = driver.find_element_by_id("password")
password_input.send_keys(linkedin_password)
password_input.send_keys(Keys.ENTER)

# select job offers
jobs_title = driver.find_elements_by_css_selector(".jobs-search-two-pane__wrapper .job-card-container--clickable .artdeco-entity-lockup__content .job-card-list__title")
companies = driver.find_elements_by_css_selector(".jobs-search-two-pane__wrapper .job-card-container--clickable .job-card-container__company-name")
locations = driver.find_elements_by_css_selector(".jobs-search-two-pane__wrapper .job-card-container--clickable .job-card-container__metadata-item")


title = []
company = []
location = []

for i in jobs_title:
    title.append(i.text)

for j in companies:
    company.append(j.text)

for k in locations:
    location.append(k.text)

for nbr in range(0, len(title) - 1):
    print(f"Job title: {title[nbr]},\n"
          f"company: {company[nbr]},\n"
          f"location: {location[nbr]}.")

driver.close()
