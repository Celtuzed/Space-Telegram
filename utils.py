import requests


def download_image(link, path, params=None):

    response = requests.get(link, params, verify=False)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)


def check_status(response):
    if response.raise_for_status():
        raise requests.HTTPError
    elif "error" in response.json():
        raise requests.exceptions.HTTPError(response.json()['error'])
