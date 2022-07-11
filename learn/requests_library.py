import os
import time
import platform
import requests
import subprocess
import webbrowser

# clearing the terminal, and sleep for one second
subprocess.run(['clear'])
time.sleep(1)

# payload = {
#     'page':2,
#     'count':25
# }

# r = requests.get('http://localhost:8000', params=payload)

# this is a localhost server that I setup in my laptop
url = 'http://127.0.0.1:8000'

r = requests.get(url)

time.sleep(3)

with open('record.txt', 'wb') as f:
    print('The record has been saved')
    f.write(r.content)
time.sleep(3)

webbrowser.get().open(url)

# the r.text print the html source cod exactly together with the indentation
# print(r.text)

# r.content print the html source code without decoding the escape character e.g \n, \t, etc
# print(r.content)
# print(r.status_code)
# print(r.url)
# print(r.ok)
# print(r.headers)

print('Clearing the terminal and,')
print('Booting up the browser, it is loading...')
print('\nTo see more open this url in browser ' + url + '\n')


ox = platform.system()
u = subprocess.run(['whoami'], capture_output=True)
uu = u.stdout.decode()
subprocess.run(['echo', uu, 'you are using'])
try:
    l = subprocess.run(['banner', ox, 'OS'], capture_output=True)
    l = subprocess.run([ox, 'OS'], capture_output=True)
except:
    print('please install banner')
with open('n-11.txt', 'w') as f:
    f.write(l.stdout.decode())
    time.sleep(1)
    os.remove('n-11.txt')
print(l.stdout.decode())
