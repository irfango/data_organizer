import os
import shutil
import time
from datetime import datetime
from os import scandir

cwd = os.getcwd()
PATH = cwd + '\\\\'

PHOTOS = PATH + '\\photos\\'
DOCUMENTS = PATH + '\\documents\\'
MUSIC = PATH + '\\music\\'
VIDEOS = PATH + '\\videos\\'

#make folder

os.mkdir("photos")
os.mkdir("videos")
os.mkdir("documents")
os.mkdir("music")

print("Directories created successfully")
print(PATH)


for f_name in os.listdir(cwd):
    if f_name.endswith('.txt'):
        print(f_name)

#music
        
for f_music in os.listdir(cwd):
    if f_music.endswith('.mp3'):
        print(f_music)
        shutil.move(PATH + f_music ,MUSIC + f_music)
        
for f_music in os.listdir(cwd):
    if f_music.endswith('.wav'):
        print(f_music)
        shutil.move(PATH + f_music ,MUSIC + f_music)

#photos
        
for f_photos in os.listdir(cwd):
    if f_photos.endswith('.jpg'):
        print(f_photos)
        shutil.move(PATH + f_photos ,PHOTOS + f_photos)
        
for f_photos in os.listdir(cwd):
    if f_photos.endswith('.png'):
        print(f_photos)
        shutil.move(PATH + f_photos ,PHOTOS + f_photos)
        
for f_photos in os.listdir(cwd):
    if f_photos.endswith('.PNG'):
        print(f_photos)
        shutil.move(PATH + f_photos ,PHOTOS + f_photos)

#documents

for f_doc in os.listdir(cwd):
    if f_doc.endswith('.txt'):
        print(f_doc)
        shutil.move(PATH + f_doc ,DOCUMENTS + f_doc)
        
for f_doc in os.listdir(cwd):
    if f_doc.endswith('.pdf'):
        print(f_doc)
        shutil.move(PATH + f_doc ,DOCUMENTS + f_doc)

#videoss

for f_video in os.listdir(cwd):
    if f_video.endswith('.mp4'):
        print(f_video)
        shutil.move(PATH + f_video ,VIDEOS + f_video)
        
for f_video in os.listdir(cwd):
    if f_video.endswith('.mov'):
        print(f_video)
        shutil.move(PATH + f_video ,VIDEOS + f_video)
        
for f_video in os.listdir(cwd):
    if f_video.endswith('.avi'):
        print(f_video)
        shutil.move(PATH + f_video ,VIDEOS + f_video)

for f_video in os.listdir(cwd):
    if f_video.endswith('.mpeg'):
        print(f_video)
        shutil.move(PATH + f_video ,VIDEOS + f_video)

print("file moved successfully")
        
