import time
import os

import telegram
from dotenv import load_dotenv


def upload_images(tg_token, main_folder):
    bot = telegram.Bot(token = tg_token)
    updates = bot.get_updates()

    for image_name in os.listdir(main_folder):
        with open(f"{main_folder}/{image_name}", "rb") as document:
            bot.send_document(document = document, chat_id = "@space_tg_bot")
            time.sleep(86400)
