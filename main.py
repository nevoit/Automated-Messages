import json
import logging
import time
from whatsapp.whatsapp import WhatsApp
from facebook.facebook import Facebook
import traceback

if __name__ == '__main__':
    wa = WhatsApp()

    json_file = open(r"resources/messages/whatsapp_friend_1.json", encoding='utf8')
    messages = json.load(json_file)
    wa.run(contact_name="Notes", hours_between_msg=0.01, number_of_msg=15, messages=messages)

    json_file = open(r"resources/messages/whatsapp_friend_2.json", encoding='utf8')
    messages = json.load(json_file)
    wa.run(contact_name="Notes", hours_between_msg=0.01, number_of_msg=3, messages=messages)
    """

    f = Facebook('shaked.eyal@protonmail.com')
    try:
        f.get_user_birthday('Nevo Itzhak')
    except Exception:
        traceback.print_exc()

    print("Goodbye :)")


def creat_logger():
    time_str = time.strftime("%d%m%Y-%H%M%S")
    log_file_name = 'automated_messages_' + time_str + '.log'
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
    logging.info('Create log file')


if __name__ == '__main__':
    main()
