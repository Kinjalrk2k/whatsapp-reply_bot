from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import os
if not os.path.exists('userdata'):
    os.makedirs('userdata')

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=userdata")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')

time.sleep(15)

names = ["Me"]

for name in names:
    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()
    for i in range(1, 3):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')

    msg_got = driver.find_elements_by_css_selector(
        "span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]
    # print(msg)

    if msg[-1] == "Thank You :)":
        reply = driver.find_element_by_class_name(
            "_3u328.copyable-text.selectable-text")
        reply.clear()
        reply.send_keys("Your Welcome ! :)")
        reply.send_keys(Keys.RETURN)
    else:
        reply = driver.find_element_by_class_name(
            "_3u328.copyable-text.selectable-text")
        reply.clear()
        reply.send_keys("Will look to this")
        reply.send_keys(Keys.RETURN)
