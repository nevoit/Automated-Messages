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
config.read(r'whatsapp\config.ini')
setting = config['SETTINGS']
# Setting up variable from config file
driver_path = setting['WEB_DRIVER']
website_url = setting['WEBSITE_URL']
msg_json = setting['JSON']
json_file = open(msg_json, encoding='utf8')
messages = json.load(json_file)
time_to_sleep = int(setting['TIME_TO_SLEEP'])
range_default = int(setting['RANGE'])
time_night_start = int(setting['TIME_NIGHT_START'])
time_night_end = int(setting['TIME_NIGHT_END'])
time_morning_start = int(setting['TIME_MORNING_START'])
time_morning_end = int(setting['TIME_MORNING_END'])
time_hour_start = int(setting['START_HOUR'])


class WhatsApp(object):

    def __init__(self, contact_name: str, hours_between_msg: float):
        self.time_between_msg: int = int(hours_between_msg * 3600)  # hours to seconds
        self.phone_name = contact_name
        self.browser = webdriver.Chrome(driver_path)
        self.browser.get(website_url)
        print("Please go to your smart phone -> WhatsApp -> WhatsApp Web -> Use the QR code reader to connect"
              "\nNote: you have only {0} seconds to connect".format(time_to_sleep))
        time.sleep(time_to_sleep)  # time to connect
        # Finding the search element
        self.document_element = self.browser.find_element_by_xpath("//input[@title='Search or start new chat']")
        self.document_element.click()
        self.document_element.send_keys(self.phone_name)
        time.sleep(time_to_sleep)
        # Finding the contact name
        self.browser.find_element_by_xpath("//*[@title='" + self.phone_name + "']").click()
        time.sleep(time_to_sleep)
        # not sure
        self.document_element = self.browser.find_element_by_xpath("//div[@data-tab='1']")
        self.document_element.click()

    def run(self):
        print("Welcome to AutomaticSocial, we will send your messages to {0}, every {1} hours ({2} seconds),"
              "\nThank you for using our program!".format(self.phone_name,
                                                          self.time_between_msg/3600,
                                                          self.time_between_msg))
        for i in range(range_default):
            now = datetime.now()
            now_time = now.time()
            if clock(time_night_start, time_hour_start) <= now_time <= clock(time_night_end, time_hour_start):
                key_in_dict, value_in_dict = random.choice(list(messages['night'].items()))
                message_to_send = value_in_dict
            elif clock(time_morning_start, time_hour_start) <= now_time <= clock(time_morning_end, time_hour_start):
                key_in_dict, value_in_dict = random.choice(list(messages['morning'].items()))
                message_to_send = value_in_dict
            else:
                key_in_dict, value_in_dict = random.choice(list(messages['day'].items()))
                message_to_send = value_in_dict
            self.document_element.send_keys(message_to_send + " " + Keys.ENTER)
            time.sleep(self.time_between_msg)
