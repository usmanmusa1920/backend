"""
  in other to run this program you have to make sure you have a server like apache or even create a simple project with django or flask and then use the host and the port for tthat project after you make the server connection
"""

import time
import requests
import  webbrowser
import subprocess as sp


sp.run(['clear'])
url = 'http://127.0.0.1:'


# host is the host number you want to use
host = ''


# route is for example \home, \signup of a website
route = ''


if host == '' or route == '':
  while host == '':
    host = input('Enter host: ')
  while route == '':
    route = input('Enter the route: ')
    
rr = url+str(int(host))
r = requests.get(rr)

print(r.status_code)
print('The webserver (host) is booting just a minute...')
print(rr+'/'+route)
time.sleep(2)

webbrowser.get().open(rr+'/'+route)
