from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(service=service)
# chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(show_message_button.get_attribute('innerHTML'))
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I am testing selenium.')

show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I am testing selenium.' in output_message.text
print(chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn'))

sleep(1)
chrome_browser.close()

# if 'Selenium Easy Demo' in chrome_browser.title
#   print("Yes in title.")

# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
