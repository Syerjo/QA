'''
Welcome, cyber ninjas! 🐱‍💻 Today you face a task that can be compared to finding a needle in a haystack. But not just any needle—a golden needle with a serial number, lost in an endless ocean of information.

🕵️‍♀️ Your mission, should you choose to accept it, is to infiltrate the labyrinth of infinite checkboxes, appearing like mushrooms after the rain. Each checkbox is a miniature lock, opening only under one condition: its "value" attribute must be even.

🚀 If you make a mistake, your mission fails. But if you succeed, you will receive more than just congratulations in the chat. At the bottom, a mysterious button with the class `alert_button` will appear, giving you a secret code. This code is the key to our next operation, so ninja, there is no room for error.

Task:
1. Initialization: Open the specified website (https://parsinger.ru/selenium/5.7/4/index.html) using Selenium.
2. Infinite Scrolling: The website contains a block with infinite loading of checkboxes. There are 100 containers in total, and each container has 10 checkboxes.
3. Even Selection: Select only the checkboxes with an even value attribute.
4. Alert Button: After selecting all checkboxes in all containers, a button with the class `alert_button` will appear. Click on it to trigger an alert message, which will contain the key to the task.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)

    while True:
        last_child = browser.find_element(By.CSS_SELECTOR, '#main_container div:last-child')
        action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()
        div_elements = browser.find_elements(By.CLASS_NAME, 'child_container')
        if len(div_elements) == 100:
            break

    for div in div_elements:
        inp_elements = div.find_elements(By.TAG_NAME, 'input')
        action.move_to_element(div).perform()
        for inp in inp_elements:
            if int(inp.get_attribute('value')) % 2 == 0:
                inp.click()

    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    alert_text = browser.switch_to.alert.text
print(alert_text)
