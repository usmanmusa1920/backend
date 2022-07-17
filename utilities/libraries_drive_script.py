# A simple python script, that I used to copy python
# libraries that are present on my machine to a specified location that I want


import os
import time


os.system('mkdir -p ~/Desktop/local-site-packages')
# sleepfor one second
time.sleep(1)

for i in os.listdir():
  
  # skipping this img file because something went wrong
  if i == "matplotlib/mpl-data/sample_data/grace_hopper.jpg":
    continue
  os.system(f'cp -r {i} ~/Desktop/third_dep')
  
  # printing the name of the current file
  print(i, 'on loop')


print("Program finish")
