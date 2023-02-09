from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(service=service)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(button.get_attribute('innerHTML'))
# sleep(10)

# if 'Selenium Easy Demo' in chrome_browser.title
#   print("Yes in title.")

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
