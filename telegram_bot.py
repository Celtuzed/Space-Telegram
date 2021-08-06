import time
import os

import telegram
from dotenv import load_dotenv


def upload_images(tg_token):
    bot = telegram.Bot(token = tg_token)
    updates = bot.get_updates()

    image_number = 0
    while True:
        image = os.listdir("images")[image_number]
        bot.send_document(document = open(f'images/{image}','rb'), chat_id = "@space_tg_bot")
        image_number = image_number + 1
        time.sleep(5)
