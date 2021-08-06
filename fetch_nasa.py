import os

import requests

from utils import get_dates, get_formats_and_filenames, get_images, get_params, get_images_urls


def fetch_nasa_apod():

    params = get_params()
    url = "https://api.nasa.gov/planetary/apod"

    response = requests.get(url, params)

    response.raise_for_status()
    links = get_images_urls()
    formats = get_formats_and_filenames()[0]
    filenames = get_formats_and_filenames()[1]
    print(formats)
    print(filenames)
    for number, link in enumerate(links):
        if formats[number] == ".jpg":
            path = f"images/{filenames[number]}{formats[number]}"
            get_images(link, path)
        else:
            print("Это не картинка!")

def fetch_nasa_epic():

    nasa_api_key = os.getenv('NASA_API_KEY')
    params = {
        "api_key" : nasa_api_key
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(url, params)

    identifiers = []
    images = []

    epic_images = response.json()
    for epic_image in epic_images:
        identifiers.append(epic_image["identifier"])
        images.append(epic_image["image"])

    for number, image in enumerate(images):
        identifier = identifiers[number]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{identifier[:4]}/{identifier[4:6]}/{identifier[6:8]}/png/{image}.png"
        response = requests.get(image_url, params)
        path = f"images/{image}.png"
        link = response.url
        get_images(link, path)
