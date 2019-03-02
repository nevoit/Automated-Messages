from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
import time
import json
from datetime import datetime
from datetime import time as clock
import random

# Config initialization -
config = configparser.ConfigParser()
config.read('config.ini')
info = config['INFORMATION']
setting = config['SETTINGS']

# Setting up variable from config file
contact_name = info['LOVER_PHONE_NAME']
driver_path = setting['WEB_DRIVER']
website_url = setting['WEBSITE_URL']
lovers_json = setting['JSON_LOVERS']
time_between_messages = int(float(setting['TIME_BETWEEN_MESSAGES'])*60*60)
json_file = open(lovers_json, encoding='utf8')
messages = json.load(json_file)
time_to_sleep = int(setting['TIME_TO_SLEEP'])
range_default = int(setting['RANGE'])
time_night_start = int(setting['TIME_NIGHT_START'])
time_night_end = int(setting['TIME_NIGHT_END'])
time_morning_start = int(setting['TIME_MORNING_START'])
time_morning_end = int(setting['TIME_MORNING_END'])
time_hour_start = int(setting['START_HOUR'])

browser = webdriver.Chrome(driver_path)
browser.get(website_url)

time.sleep(time_to_sleep)  # time to connect
# Finding the search element
document_element = browser.find_element_by_xpath("//input[@title='Search or start new chat']")
document_element.click()
document_element.send_keys(contact_name)
time.sleep(time_to_sleep)
# Finding the contact name
browser.find_element_by_xpath("//*[@title='" + contact_name + "']").click()
time.sleep(time_to_sleep)
# not sure
document_element = browser.find_element_by_xpath("//div[@data-tab='1']")
document_element.click()

for i in range(range_default):
    now = datetime.now()
    now_time = now.time()
    message_to_send = ''
    if clock(time_night_start, time_hour_start) <= now_time <= clock(time_night_end, time_hour_start):
        key_in_dict, value_in_dict = random.choice(list(messages['night'].items()))
        message_to_send = "This is night time: " + value_in_dict
    elif clock(time_morning_start, time_hour_start) <= now_time <= clock(time_morning_end, time_hour_start):
        key_in_dict, value_in_dict = random.choice(list(messages['morning'].items()))
        message_to_send = "This is morning time: " + value_in_dict
    else:
        key_in_dict, value_in_dict = random.choice(list(messages['day'].items()))
        message_to_send = "This is day time: " + value_in_dict
    document_element.send_keys(message_to_send + " " + Keys.ENTER)
    time.sleep(time_between_messages)
