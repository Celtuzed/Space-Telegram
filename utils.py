import os

from urllib.parse import unquote, urlsplit
from PIL import Image
import requests

#Основная часть функций, которая скачивает картинки
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

#Функция, которая непосредственно вытягивает форматы
def get_formats(response, images_formats):

    all_links = response.json()
    image_files = all_links["image_files"]

    for image_url in image_files:
        images = unquote(f'https:{image_url["file_url"]}')
        images_format = urlsplit(images).path[-3:]
        images_formats.append(images_format)

#Функция, которая получает картинки для hi
def get_formats_for_hi(url):

    images_formats = []

    response = requests.get(url)
    response.raise_for_status()

    get_formats(response, images_formats)

    return images_formats

#Функция, которая получает картинки для hc
def get_formats_for_hc(url, all_id):

    images_formats = []

    response = requests.get(url)
    response.raise_for_status()

    for image_id in all_id:
                url = f"http://hubblesite.org/api/v3/image/{image_id}"
                response = requests.get(url)
                response.raise_for_status()

                get_formats(response, images_formats)

    return images_formats

#Получение ID
def get_id(url):

    images_formats = []
    all_id = []

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()

    for image_id in all_links:
        all_id.append(image_id["id"])
    return all_id
