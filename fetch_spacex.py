import os
import requests
from PIL import Image

def fetch_spacex_last_launch():

    filename = 'sx'
    url = "https://api.spacexdata.com/v3/launches/latest"

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()["links"]
    images_links = all_links["flickr_images"]

    for image_number, images in enumerate(images_links):
        response = requests.get(images)
        response.raise_for_status()
        with open(f'images/{filename}_{image_number}.jpeg', 'wb') as file:
            file.write(response.content)
        image = Image.open(f'images/{filename}_{image_number}.jpeg')
        image.thumbnail((1080, 1080))
        image.save('images/{filename}_{image_number}.jpeg')
