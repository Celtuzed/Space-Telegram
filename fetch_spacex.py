import os

import requests

from utils import get_images


def fetch_spacex_last_launch(main_folder):

    filename = "sx"
    url = "https://api.spacexdata.com/v3/launches/latest"

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()["links"]
    images_links = all_links["flickr_images"]

    if images_links:
        for image_number, link in enumerate(images_links):
            path = f"{main_folder}/{filename}_{image_number}.jpeg"
            get_images()
