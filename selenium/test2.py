from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

browser = webdriver.Chrome(
    executable_path='path/to/driver')

browser.get('https://bandcamp.com')



time.sleep(5)
next_page = browser.find_elements_by_class_name('item-page')
time.sleep(5)
print(len(next_page))
time.sleep(2)
next_page[-1].click()






time.sleep(5)
tracks = browser.find_elements_by_class_name('discover-item')
time.sleep(3)
print(len(tracks))


discover_section = browser.find_element_by_class_name('discover-results')

index = 0
for i,v in enumerate(tracks):
    print(i,v.text)
    if 'City Girl' in v.text:
        tracks[i].click()
        index = i

time.sleep(7)
print('====')
print(discover_section.location)
print('--')
left_x = discover_section.location['x']
print(left_x)

right_x = left_x + discover_section.size['width']
print(right_x)

tracks[index].click()
browser.close()
quit()
