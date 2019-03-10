from selenium import webdriver
import time
from pytesseract import image_to_string
from PIL import Image
import base64

browser = webdriver.Chrome(executable_path='/Users/mac/Desktop/webdriver/chromedriver')


class Bot:
    def __init__(self):
        self.driver = browser
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    # def crop(self, location, size):
    #     image = Image.open('avito_screenshot.png')
    #     x = location['x']
    #     y = location['y']
    #     width = size['width']
    #     height = size['height']
    #     print(x, y, width, height)
    #
    #     image.crop((x, y, x+width, y+height)).save('tel.gif')

    def tel_recon(self):
        image = Image.open('imageToSave.png')
        print(image_to_string(image))
        with open('phones.txt','a') as f:
            f.write(image_to_string(image)+'\n')

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/detskaya_odezhda_i_obuv/puhovik_patagonia_m_10_let_945629810')
        time.sleep(5)
        button = self.driver.find_element_by_xpath(
            '//a[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        time.sleep(3)
        button.click()
        time.sleep(3)
        self.take_screenshot()
        time.sleep(5)

        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]/img')
        image_src = image.get_attribute('src').split(',')[1]
        img = base64.decodebytes(bytearray(image_src, 'utf-8'))
        with open("imageToSave.png", "wb") as f:
            f.write(img)

        time.sleep(3)

        self.tel_recon()

        browser.close()


def main():
    r = Bot()


if __name__ == '__main__':
    main()
