import argparse
import os

import requests
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch
from telegram_bot import upload_images


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser(description='Скрипт скачивает картинки с SpaceX или Hubble, а также может постить картинки из папки в инстаграм')
    parser.add_argument('-sx', '--SpaceX', action='store_true', help='Скачивает картинки с сайта SpaceX')
    parser.add_argument('-ena', '--EPIC_NASA', action='store_true', help='Скачивает картинки с EPIC NASA api за последние сутки (или ранее)')
    parser.add_argument('-ana', '--APOD_NASA', action='store_true', help='Скачивает картинки с APOD NASA api за последние 30 дней')
    parser.add_argument('-tg', '--Telegram', action='store_true', help='Выкладывает картинки в телеграм канал')
    args = parser.parse_args()


    main_folder = "images"

    os.makedirs(main_folder, exist_ok=True)

    if args.SpaceX:
        fetch_spacex_last_launch()
    elif args.EPIC_NASA:
        fetch_nasa_epic()
    elif args.APOD_NASA:
        fetch_nasa_apod()
    elif args.Telegram:
        tg_token = os.getenv("TG_BOT_API_KEY")
        upload_images(tg_token)
    else:
        print("Введите 1 из аргументов")
