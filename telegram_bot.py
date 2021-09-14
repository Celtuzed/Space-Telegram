import time
import os

import telegram


def upload_images(tg_token, main_folder, chat_id):
    bot = telegram.Bot(token=tg_token)

    for image_name in os.listdir(main_folder):
        with open(f"{main_folder}/{image_name}", "rb") as document:
            bot.send_document(document=document, chat_id=chat_id)
        time.sleep(86400)
