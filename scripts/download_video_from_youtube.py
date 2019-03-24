import pytube
import os


dir = os.getcwd()

with open('urls.txt','r') as f:
    for line in f.readlines():
        video = pytube.YouTube(line.replace('\n','')).streams.first().download(dir)