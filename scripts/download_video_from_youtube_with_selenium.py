import pytube
from selenium import webdriver


dir = 'path/to/dir'

driver = webdriver.Chrome(executable_path='/path/to/webdriver/chromedriver')
driver.get('https://www.youtube.com/playlist?list=*list*')

all_links = driver.find_elements_by_xpath('//*[@class="yt-simple-endpoint style-scope ytd-playlist-video-renderer"]')
print(len(all_links)) # check quantity of videos


with open ('test.txt','a') as f:
    for link in all_links:
        f.write(link.get_attribute("href"))
        f.write('\n')
      
driver.close()
    

with open('test.txt','r') as f:
    for line in f.readlines():
        video = pytube.YouTube(line.replace('\n','')).streams.first().download(dir)