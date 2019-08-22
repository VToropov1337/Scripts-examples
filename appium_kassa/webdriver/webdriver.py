from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import json


class Driver:

    def __init__(self, path_to_desired, url):
        with open(path_to_desired, 'r') as f:
            desired_cap = json.loads(f.read())

        self.instance = webdriver.Remote(url, desired_cap)
        self.instance.implicitly_wait(3)
        self.instance.wait = WebDriverWait(self.instance,3)
