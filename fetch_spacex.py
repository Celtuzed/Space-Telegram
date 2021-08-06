import os

import requests


def fetch_spacex_last_launch():

    filename = 'sx'
    url = "https://api.spacexdata.com/v3/launches/latest"

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()["links"]
    images_links = all_links["flickr_images"]

    if images_links:
        for image_number, images in enumerate(images_links):
            response = requests.get(images)
            response.raise_for_status()
            with open(f'images/{filename}_{image_number}.jpeg', 'wb') as file:
                file.write(response.content)
    else:
        print("С последнего запуска нет картинок")
