import shutil
import os

source = '/Users/Molly/Desktop/Folder A/'
destination = '/Users/Molly/Desktop/Folder B/'

for files in os.listdir(source):
    if files.endswith('.txt'):
       shutil.move(source + files, destination)

for files in os.listdir(destination):
    if files.endswith('.txt'):
        print destination + files
