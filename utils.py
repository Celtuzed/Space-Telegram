import os
import datetime
from dotenv import load_dotenv
from urllib.parse import unquote, urlsplit

import requests


def get_images(link, path):

    response = requests.get(link, verify=False)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def get_formats_and_filenames():

    links = get_images_urls()

    filenames = []
    formats = []

    for link in links:
        filenames.append(os.path.splitext(os.path.split(link)[1])[0])
        formats.append(os.path.splitext(link)[1])
    return formats, filenames


def get_dates():

    today = datetime.datetime.date(datetime.datetime.today())
    a_month_ago = today - datetime.timedelta(days = 30)

    return today, a_month_ago


def get_params():

    nasa_api_key = os.getenv('NASA_API_KEY')
    params = {
        "api_key" : nasa_api_key,
        "start_date" : get_dates()[1],
        "end_date" : get_dates()[0]
    }

    return params


def get_images_urls():

    links = []

    params = get_params()
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params)
    all_urls = response.json()
    for url in all_urls:
        links.append(url["url"])

    return links
