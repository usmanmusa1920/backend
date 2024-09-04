import requests
from pathlib import Path


img_url = "https://www.python.org/static/img/python-logo.png"


def download_image():

    img_bytes = requests.get(img_url).content
    
    img_split = img_url.split("/")[-1]
    img_extension = img_split.split(".")[-1]

    img_name = f"downloaded-image.{img_extension}"

    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"  Downloaded image name: {img_name}")

    location = Path(img_name).resolve()
    print(f"  Image file location: {location}")

download_image()
