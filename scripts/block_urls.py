#/usr/local/bin/python3

import time
from datetime import datetime as dt


host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = ["www.instagram.com","www.facebook.com","www.vk.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          19):
        with open(host_path, "r+") as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + " " + website + "\n")
    else:
        with open(host_path,'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
                f.truncate()

    time.sleep(60)