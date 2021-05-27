from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "Your_Chrome_Driver_Path"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0e")

sing_up_button = driver.find_element_by_class_name("nav__button-secondary")
sing_up_button.click()

time.sleep(1)
username = driver.find_element_by_id("username")
username.send_keys("Your_Linkedin_Email")
password = driver.find_element_by_id("password")
password.send_keys("Your_Linkedin_Password")
password.send_keys(Keys.ENTER)

time.sleep(3)
y = 0
# jobs = driver.find_element_by_link_text("Python Developer")
for i in range(25):
    jobs = driver.find_elements_by_css_selector(".artdeco-entity-lockup__title")[i]
    jobs.click()
    time.sleep(2)

    save_button = driver.find_element_by_css_selector(".jobs-save-button")
    save_button.click()

    time.sleep(2)
    see_more = driver.find_element_by_css_selector(".artdeco-card__actions")
    see_more.click()

    time.sleep(1)
    job_info = driver.find_element_by_css_selector(".jobs-box__html-content")
    try:
        with open("linkedIn job Info.txt", "a") as file:
            file.write("\n\n========New Job========\n\n\n")
            file.write(job_info.text)
        with open("linkedIn job Info.txt") as data:
            content = data.read()
            print(content)
    except:
        print("Encoding Problem")
    driver.back()
    y += 120
    driver.execute_script(f"window.scroll(0, {y})")
    time.sleep(2)
