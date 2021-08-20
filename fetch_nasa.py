from datetime import datetime
import os

import requests

from utils import get_dates, get_formats_and_filenames, get_images, get_params, get_images_urls


def fetch_nasa_apod(main_folder, nasa_api_key):

    params = get_params(nasa_api_key)
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params)

    response.raise_for_status()
    links = get_images_urls(nasa_api_key)
    formats_and_filenames = get_formats_and_filenames(nasa_api_key, links)
    formats = formats_and_filenames[0]
    filenames = formats_and_filenames[1]
    for number, link in enumerate(links):
        if formats[number] == ".jpg":
            path = f"{main_folder}/{filenames[number]}{formats[number]}"
            get_images(link, path, params)

def fetch_nasa_epic(main_folder, nasa_api_key):

    params = {
        "api_key" : nasa_api_key
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(url, params)
    epic_images = response.json()

    for number, epic_image in enumerate(epic_images):
        date = datetime.fromisoformat(epic_image["date"])
        link = f"https://api.nasa.gov/EPIC/archive/natural/{date.strftime('%Y/%m/%d')}/png/{epic_image['image']}.png"
        path = f"{main_folder}/{epic_image['image']}.png"
        get_images(link, path, params)
