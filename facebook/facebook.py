from getpass import getpass
from urllib.request import urlopen

from bs4 import BeautifulSoup
from fbchat import Client
from fbchat.models import FBchatException
from fbchat.models import Message
from fbchat.models import ThreadType


class Facebook:

    def __init__(self, user_name):
        self.username = user_name
        try:
            self.fb_client = Client(self.username, getpass())
        except FBchatException:
            print('Failed to log into facebook. Please check your credentials')

    def send_message_friend(self, friend_name, msg):
        try:
            friend_user = self.__get_user(friend_name)
            friend_uid = friend_user.uid
            sent = self.fb_client.send(Message(text=msg), thread_id=friend_uid,
                                       thread_type=ThreadType.USER)
            if sent:
                print('Message sent successfully!')
            else:
                raise FBchatException("Couldn't send message")
        except FBchatException:
            print("Couldn't find any friends. Please check the name")

    def send_message_group(self, group_name, msg):
        try:
            groups_list = self.fb_client.searchForGroups(group_name, limit=1)
            group = groups_list[0]
            group_uid = group
            sent = self.fb_client.send(Message(text=msg), thread_id=group_uid, thread_type=ThreadType.GROUP)
            if sent:
                print("Message sent successfully!")
            else:
                raise FBchatException("Coludn't send message")
        except FBchatException:
            print("Couldn't find any groups. Please check the group name")

    def get_user_birthday(self, user_name):
        try:
            friend_user = self.__get_user(user_name)
            friend_url = friend_user.url
            print(friend_url)
            html_file = urlopen(friend_url)
            user_file = BeautifulSoup(html_file, features="html.parser")
            print(user_file)
        except FBchatException:

            print("Couldn't get birthday")

    def __get_user(self, user_name):
        friends = self.fb_client.searchForUsers(user_name, limit=1)
        friend_user = friends[0]
        return friend_user
