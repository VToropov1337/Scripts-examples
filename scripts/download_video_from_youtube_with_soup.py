import pytube
from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


def get_html(url):
	r = requests.get(url)
	return r.text


def get_links(url):
	soup = BeautifulSoup(url, features='html.parser')
	video_links = []
	data = soup.find_all('a',class_='pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link')
	for i in data:
		video_links.append('https://www.youtube.com' + i.get('href'))

	return video_links


def download_video(link):
	pytube.YouTube(link.replace('\n','')).streams.first().download()





if __name__ == '__main__':
	location_to_download = 'path/to/dir'
	a = get_links(get_html('https://www.youtube.com/playlist?list=***'))
	with Pool(26) as pool:
		pool.map(download_video,a)
