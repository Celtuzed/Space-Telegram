import requests


def download_image(link, path, params=None):

    response = requests.get(link, params, verify=False)
    response.raise_for_status()

    with open(path, "wb") as file:
        file.write(response.content)
