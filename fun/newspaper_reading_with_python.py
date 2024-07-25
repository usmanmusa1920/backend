import subprocess as sp
import time

sp.run(['clear'])

my_str = '\tI am Usman Musa, software developer from Nigeria, I am so eager to do and to simplify task by automating and packaging things to make python to handle them for me, always, everytime, everywhere, instead of doing them over and over. As I am a developer I try to make things DRY (don\'t repeat your self)'

print()

for i in my_str:
    print(i, end='', flush=True)
    if i == ',':
        time.sleep(1)
    else:
        time.sleep(0.1)
print()
time.sleep(1)
print()
