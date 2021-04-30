from download_images import get_images
from PIL import Image
import requests
import os


def get_hubble_collection(Hubble_collection):

    filename = 'hc'
    url = f'http://hubblesite.org/api/v3/images/{Hubble_collection}'
    images_formats = get_formats_for_collections(url)[1]
    all_id = get_formats_for_collections(url)[0]

    for image_id in all_id:
        url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(url)
        response.raise_for_status()

        all_links = response.json()
        image_files = all_links["image_files"]

        for image_number, images in enumerate(image_files):
            url = f'https:{images["file_url"]}'
            get_images(image_id, url, image_number, images_formats, filename)

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

def get_formats(url):

    images_formats = []

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()
    image_files = all_links["image_files"]

    for image_url in image_files:
            images = f'https:{image_url["file_url"]}'
            images_format = images[-3:]
            images_formats.append(images_format)
    return images_formats


def get_formats_for_collections(url):

    images_formats = []
    all_id = []

    response = requests.get(url)
    response.raise_for_status()

    all_links = response.json()

    for image_id in all_links:
        all_id.append(image_id["id"])

    for image_id in all_id:
        url = f"http://hubblesite.org/api/v3/image/{image_id}"
        response = requests.get(url)
        response.raise_for_status()

        all_links = response.json()
        image_files = all_links["image_files"]

        for image_url in image_files:
            images = f'https:{image_url["file_url"]}'
            images_format = images[-3:]
            images_formats.append(images_format)
    return all_id, images_formats