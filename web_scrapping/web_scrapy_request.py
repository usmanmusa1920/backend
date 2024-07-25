# web scraping using the most popular python library (request) and pandas for storing data


# pip install beautifulsoup4
# pip install lxml              # lxml is recommended for beautiful
# pip install html5lib
# pip install requests


# NB: To access an attribute of an html e.g like iframe tag, image tag, or others, you are to access it like a dictionary e.g:
#     <iframe allowfullscreen="true" class="youtube-player" height="390" width="auto" src="https://www.youtube.com/embeded/fyghfevdwgs-9?version=3&amp;rel=1&amp;fs=2&amp"></iframe>
#     vid_src = soup.find('iframe', class_='youtube-player')['src]
#     vid_id = vid_src.split('/')[4]
#     vid_id = vid_id.split('?')[0]
#     yt_link = f"https://wwww.youtube.com/watch?v={vid_id}"


import requests
from bs4 import BeautifulSoup

# with open("index.html") as f:
#     soup = BeautifulSoup(f, 'lxml')
# print(soup.prettify())



# source = requests.get('http://127.0.0.1:8000/').text
# soup = BeautifulSoup(source, 'lxml')
# result = soup.find('post')
# print(result.prettify())



source = requests.get("http://127.0.0.1:8000").text
soup = BeautifulSoup(source, 'lxml')

# f = soup.find('div', class_='post')
# print(f.prettify())

for f in soup.find_all('div', class_='post_content_column'):
    title = f.h1.text
    summary = f.p.text
    print(title, "\n", summary, "\n")
