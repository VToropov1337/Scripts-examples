from selenium import webdriver
import time
from PIL import Image

browser = webdriver.Chrome(executable_path='/Users/mac/Desktop/webdriver/chromedriver')


class Bot:
    def __init__(self):
        self.driver = browser
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        print(x, y, width, height)

        image.crop((x, y, x + width, y + height)).save('tel.gif')

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/detskaya_odezhda_i_obuv/puhovik_patagonia_m_10_let_945629810')
        time.sleep(5)
        button = self.driver.find_element_by_xpath(
            '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        time.sleep(3)
        button.click()
        time.sleep(3)
        self.take_screenshot()
        time.sleep(10)

        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location
        print('===')
        print(location)
        size = image.size
        print('////')
        print(size)
        self.crop(location, size)
        browser.close()


def main():
    r = Bot()


if __name__ == '__main__':
    main()
