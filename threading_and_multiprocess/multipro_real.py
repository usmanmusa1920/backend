import time
import concurrent.futures
from PIL import Image, ImageFilter
import subprocess

subprocess.run(['clear'])

img_names = [
    'pic-Usman_N989gqS.jpg',
    'pic-Usman_Kc4jHRa.jpg',
    'pic-Usman.jpg',
    'pic-The-Internet_Gj7mu12.jpg',
    'pic-The-Internet_Bxso44i.jpg',
    'pic-Sim.jpg',
    'pic-QPR18_Copenhagen_3490-1024x683_FSqPaTD.jpg',
    'pic-physics_modeling_DO57TkA.jpg',
    'pic-pexels-photo-1181673.jpeg',
    'pic-pexels-photo-574073_Q26lpcA.jpeg',
    'pic-map.jpg',
    'pic-234_903_225_8167_20200712_123202.jpg'
]

t1 = time.perf_counter()

size = (100, 100)

def process_image(img_name):
# for img_name in img_names:
    img = Image.open(img_name)
    
    img = img.filter(ImageFilter.GaussianBlur(7))
    
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)
    
t2 = time.perf_counter()

print(f'Finished in {t2 - t1} seconds')