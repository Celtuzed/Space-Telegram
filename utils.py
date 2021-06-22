import os

from urllib.parse import unquote, urlsplit
from PIL import Image
import requests

#Основная часть функций, которая скацивает картинки
def get_images(image_id, url, image_number, images_formats, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    if not url[-3:] == "pdf":
        with open(f'images/{filename}_{image_id}_number-{image_number}.{images_formats[image_number]}', 'wb') as file:
            file.write(response.content)

def get_cropped_images_for_inst():
    for pic in os.listdir('images'):
        image = Image.open(f'images/{pic}')
        image.thumbnail((1080, 1080))
        image.save(f'cropped_images/cropped_{pic}')

#Получение форматов картинок вообще для -hc и -hi
def get_formats(url):

    images_formats = []

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()
    image_files = all_links["image_files"]

    for image_url in image_files:
            images = unquote(f'https:{image_url["file_url"]}')
            images_format = urlsplit(images).path[-3:]
            images_formats.append(images_format)
    return images_formats

#Получение ID для аргумента -hc
def get_id(url):

    images_formats = []
    all_id = []

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()

    for image_id in all_links:
        all_id.append(image_id["id"])
    return all_id
