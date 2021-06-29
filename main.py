import argparse
import os

from fetch_hubble import get_hubble_collection, get_hubble_images
from utils import get_cropped_images_for_inst
from fetch_spacex import fetch_spacex_last_launch
from instabot import Bot
from PIL import Image
import requests

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт скачивает картинки с SpaceX или Hubble, а также может постить картинки из папки в инстаграм')
    parser.add_argument('-sx', '--SpaceX', action='store_true', help='Скачивает картинки с сайта SpaceX')
    parser.add_argument('-hi', '--Hubble_id', help='Скачивает картинки с сайта Hublle по их ID')
    parser.add_argument('-hc', '--Hubble_collection', help='Скачивает картинки с сайта Hubble по коллекциям')
    parser.add_argument('-ip', '--Instagram_post', action='store_true', help='Постит картинки в инсту')
    args = parser.parse_args()

    main_folder = "images"
    second_folder = "cropped_images"

    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    if not os.path.exists(second_folder):
        os.makedirs(second_folder)

    if args.SpaceX:
        fetch_spacex_last_launch()
    elif args.Hubble_id:
        image_id = args.Hubble_id
        get_hubble_images(image_id)
    elif args.Hubble_collection:
        Hubble_collection = args.Hubble_collection
        get_hubble_collection(Hubble_collection)
    elif args.Instagram_post:
        get_cropped_images_for_inst()
        bot = Bot()
        bot.login(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
        for pic in os.listdir(second_folder):
            bot.upload_photo(f"{second_folder}/{pic}")
    else:
        print("Введите 1 из аргументов")
