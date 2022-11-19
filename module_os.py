import os
from datetime import datetime

#os.chdir('/home/usman/Desktop')
print(os.getcwd())

#for making a single directory
try:
  os.mkdir('mmme')
except:
  pass
#for creating a directory tree, similar to 'mkdir -p /me/you/them' (recursively)
try:
  os.makedirs('ko/l')
except:
  pass


#for removing a single directory
try:
  os.rmdir('mmme')
except:
  pass
#for removing a directory tree, similar to 'rm -rf /me/you/them' (recursively)
try:
  os.removedirs('ko/l')
except:
  pass
  
#for ranaming a file
try:
  os.rename('text.txt', 'docs.txt')
except:
  pass

#for seeing a file detail
print(os.stat('docs.txt'))

#for seeing human readable time
mod_time  = os.stat('docs.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# we can pass a path as argument in the list dir
#print(os.listdir('/home/usman'))
#print(os.listdir())

#for seeing a tree of directory (similar to tree, in command line)
#for dirpath, dirnames, filenames in os.walk('/home/usman/Desktop/ae'):
#  print('Current path:', dirpath)
#  print('Directories in this path:', dirnames)
#  print('Files in this path:', filenames)
#  print()

#for showing all environment variable
#print(os.environ)
#for showing a single environment variable
#print(os.environ.get('HOME'))


print(os.path.join(os.environ.get('HOME'), 'me.txt'))

#for spliting file from a directory tree
print(os.path.split('kk/po/m.py'))

#for spliting filename and it extension
print(os.path.splitext('kk/po/m.py'))

