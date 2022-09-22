import requests
import time
import concurrent.futures
import subprocess

subprocess.run(['clear'])

img_urls = [
    'http://127.0.0.1:8000/media/users_profile_pics/The-Internet_Gj7mu12.jpg',
    'http://127.0.0.1:8000/media/users_profile_pics/Usman_N989gqS.jpg',
    'http://127.0.0.1:8000/media/users_profile_pics/234_903_225_8167_20200712_123202.jpg',
    'http://127.0.0.1:8000/static/base/img/map.jpg',
    'http://127.0.0.1:8000/media/users_profile_pics/Sim.jpg',
    'http://127.0.0.1:8000/media/blog_pic/QPR18_Copenhagen_3490-1024x683_FSqPaTD.jpg',
    'http://127.0.0.1:8000/media/blog_pic/physics_modeling_DO57TkA.jpg',
    'http://127.0.0.1:8000/media/blog_pic/The-Internet_Bxso44i.jpg',
    'http://127.0.0.1:8000/media/blog_pic/pexels-photo-1181673.jpeg',
    'http://127.0.0.1:8000/media/blog_pic/Usman.jpg',
    'http://127.0.0.1:8000/media/blog_pic/Usman_Kc4jHRa.jpg',
    'http://127.0.0.1:8000/media/blog_pic/pexels-photo-574073_Q26lpcA.jpeg'
]

t1 = time.perf_counter()

def download_image(img_url):
# for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    img_name = f'pic-{img_name}'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    
t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')