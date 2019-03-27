import os

path = os.pwd()

for root, dirs, files in os.walk(path):
    for filename in files:
        if "bash" in filename:
            os.rename(filename,filename + ".html")


        
