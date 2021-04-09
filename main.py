from fetch_hubble import get_Hubble_collection, get_Hubble_images
from fetch_spacex import fetch_spacex_last_launch
from instabot import Bot
from PIL import Image
import requests
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт скачивает картинки с SpaceX или Hubble, а также может постить картинки из папки в инстаграм')
    parser.add_argument('-sx', '--SpaceX', action='store_true', help='Скачивает картинки с сайта SpaceX')
    parser.add_argument('-hi', '--Hubble_id', help='Скачивает картинки с сайта Hublle по их ID')
    parser.add_argument('-hc', '--Hubble_collection', help='Скачивает картинки с сайта Hubble по коллекциям')
    parser.add_argument('-ip', '--Instagram_post', action='store_true', help='Постит картинки в инсту')
    args = parser.parse_args()

    if args.SpaceX:
        fetch_spacex_last_launch()
    elif args.Hubble_id:
        id = args.Hubble_id
        get_Hubble_images(id)
    elif args.Hubble_collection:
        Hubble_collection = args.Hubble_collection
        get_Hubble_collection(Hubble_collection)
    elif args.Instagram_post:
        bot = Bot()
        bot.login(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
        for pic in os.listdir('images'):
            bot.upload_photo(f"images/{pic}")
    else:
        print("Введите 1 аргумент")
