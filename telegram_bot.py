import time
import os

import telegram
from dotenv import load_dotenv


def upload_images(tg_token, main_folder):
    bot = telegram.Bot(token = tg_token)
    updates = bot.get_updates()

    for image_name in os.listdir(main_folder):
        image = os.listdir("images")[image_number]
        bot.send_document(document = open(f'images/{image_name}','rb'), chat_id = "@space_tg_bot")
        time.sleep(5)
