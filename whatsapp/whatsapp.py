from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
import time
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
time_to_sleep = int(setting['TIME_TO_SLEEP'])
range_default = int(setting['NUMBER_OF_MSG'])
time_night_start = int(setting['TIME_NIGHT_START'])
time_night_end = int(setting['TIME_NIGHT_END'])
time_morning_start = int(setting['TIME_MORNING_START'])
time_morning_end = int(setting['TIME_MORNING_END'])
time_hour_start = int(setting['START_HOUR'])


class WhatsApp(object):

    def __init__(self, ):
        self.browser = webdriver.Chrome(driver_path)
        self.browser.get(website_url)
        print("Please go to your smart phone -> WhatsApp -> WhatsApp Web -> Use the QR code reader to connect"
              "\nNote: you have only {0} seconds to connect".format(time_to_sleep))
        time.sleep(time_to_sleep)  # time to connect
        self.secure_code = random.SystemRandom()

    def run(self, contact_name: str, hours_between_msg: float, number_of_msg: int, messages: dict):
        time_between_msg: int = int(hours_between_msg * 3600)  # hours to seconds
        phone_name = contact_name.encode("utf-8").decode("utf-8")
        # Finding the search element
        document_element = self.browser.find_element_by_xpath("//input[@title='Search or start new chat']")
        document_element.click()
        document_element.send_keys(phone_name)
        time.sleep(time_to_sleep)
        # Finding the contact name
        self.browser.find_element_by_xpath("//*[@title='" + phone_name + "']").click()
        time.sleep(time_to_sleep)
        # not sure
        document_element = self.browser.find_element_by_xpath("//div[@data-tab='1']")
        document_element.click()

        print("Welcome to AutomaticSocial, we will send your messages to {0}, every {1} hours ({2} seconds),"
              "\nThank you for using our program!".format(phone_name,
                                                          time_between_msg/3600,
                                                          time_between_msg))
        for i in range(number_of_msg):
            now = datetime.now()
            now_time = now.time()
            if clock(time_night_start, time_hour_start) <= now_time <= clock(time_night_end, time_hour_start):
                key_in_dict, value_in_dict = self.secure_code.choice(list(messages['night'].items()))
                message_to_send = value_in_dict
            elif clock(time_morning_start, time_hour_start) <= now_time <= clock(time_morning_end, time_hour_start):
                key_in_dict, value_in_dict = self.secure_code.choice(list(messages['morning'].items()))
                message_to_send = value_in_dict
            else:
                key_in_dict, value_in_dict = self.secure_code.choice(list(messages['noon'].items()))
                message_to_send = value_in_dict
            document_element.send_keys(message_to_send + " " + Keys.ENTER)
            time.sleep(time_between_msg)
