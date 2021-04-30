from PIL import Image
import requests


def get_images(image_id, url, image_number, images_formats, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()

    if not url[-3:] == "pdf":
        with open(f'images/{filename}_{image_id}_number-{image_number}.{images_formats[image_number]}', 'wb') as file:
            file.write(response.content)
        image = Image.open(f'images/{filename}_{image_id}_number-{image_number}.{images_formats[image_number]}')
        image.thumbnail((1080, 1080))
        image.save(f'images/thumbnail_{filename}_{image_id}_number-{image_number}.{images_formats[image_number]}')
