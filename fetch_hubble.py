import os

from utils import get_images, get_id, get_formats
from urllib.parse import urlparse
from PIL import Image
import requests
#функция для скацивания паков картинок
def get_hubble_collection(Hubble_collection):

    filename = 'hc'
    url = f'http://hubblesite.org/api/v3/images/{Hubble_collection}'
    images_formats = get_formats(url)
    all_id = get_id(url)

    for image_id in all_id:
        url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(url)
        response.raise_for_status()

        all_links = response.json()
        image_files = all_links["image_files"]

        for image_number, images in enumerate(image_files):
            url = f'https:{images["file_url"]}'
            get_images(image_id, url, image_number, images_formats, filename)

#Функция для скачивания отдельных картинок
def get_hubble_images(image_id):

    filename = 'hi'
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    images_formats = get_formats(url)

    response = requests.get(url)
    response.raise_for_status()
    all_links = response.json()
    image_files = all_links["image_files"]

    for image_number, images in enumerate(image_files):

        url = f'https:{images["file_url"]}'
        get_images(image_id, url, image_number, images_formats, filename)
