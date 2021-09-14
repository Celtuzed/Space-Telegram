import datetime
import os

import requests
from urllib.parse import unquote, urlsplit

from utils import download_image, check_status


def fetch_nasa_apod(main_folder, nasa_api_key):

    params = get_params(nasa_api_key)
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params)
    check_status(response)

    links = []
    all_urls = response.json()
    for url in all_urls:
        links.append(url["url"])

    for number, link in enumerate(links):
        format, filename = get_format_and_filename(link)
        if format == ".jpg":
            path = f"{main_folder}/{filename}"
            download_image(link, path, params)


def fetch_nasa_epic(main_folder, nasa_api_key):

    params = {
            "api_key": nasa_api_key
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(url, params)
    check_status(response)
    epic_images = response.json()

    for number, epic_image in enumerate(epic_images):
        date = datetime.datetime.fromisoformat(epic_image["date"])
        link = f"https://api.nasa.gov/EPIC/archive/natural/"\
               f"{date.strftime('%Y/%m/%d')}/png/{epic_image['image']}.png"
        path = f"{main_folder}/{epic_image['image']}.png"
        download_image(link, path, params)


def get_format_and_filename(link):

    formated_path = urlsplit(unquote(link)).path
    filename = os.path.split(formated_path)[1]
    format = os.path.splitext(formated_path)[1]

    return format, filename


def get_dates():

    today = datetime.datetime.date(datetime.datetime.today())
    a_month_ago = today - datetime.timedelta(days=30)

    return today, a_month_ago


def get_params(nasa_api_key):

    today, a_month_ago = get_dates()
    params = {
        "api_key": nasa_api_key,
        "start_date": a_month_ago,
        "end_date": today
    }

    return params
