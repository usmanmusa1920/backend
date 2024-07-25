# This small script is use to show how old a file is in a folder
import os
from datetime import datetime


today = datetime.today()
print("Below files are moved.")
print()

def run():
    for i in os.listdir():
        mtime = datetime.fromtimestamp(os.stat(i)[8])
        filetime = mtime - today
        
        if filetime.days <= -30:
            print(f" {os.path.basename(i):<20} older {abs(filetime.days)} days\n")

run()
