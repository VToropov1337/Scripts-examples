from bs4 import BeautifulSoup
import requests
import csv


# -*- coding: utf-8 -*-


def get_html(url):
    request = requests.get(url)
    return request.text


def get_count_pages(html):
    soup = BeautifulSoup(html, features='html.parser')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f,delimiter=';')

        writer.writerow((data['title'],
                         data['url'],
                         data['price'],
                         data['address']))


def get_data_from_page(html, query):
    soup = BeautifulSoup(html, 'lxml')
    announcement_of_the_sale = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for i in announcement_of_the_sale:
        try:
            title = i.find('div', class_='description').find('h3').text.strip()
        except:
            title = ''

        try:
            url = i.find('div', class_='description').find('a').get('href')
        except:
            url = ''

        try:
            price = i.find('div', class_='about').text.strip().replace(' ', '').replace('₽', '')
        except:
            price = ''

        try:
            address = i.find('div', class_='data').find_all('p')[-1].text.strip().replace('\xa0', '')
        except:
            address = ''
        if query[3:] in title.lower():
            data = {
                'title': title,
                'price': price,
                'url': 'https://www.avito.ru' + url,
                'address': address
            }
            write_csv(data)
        else:
            continue


def main():

    url = 'https://www.avito.ru/moskva/odezhda_obuv_aksessuary?q=patagonia'
    base_url = 'https://www.avito.ru/moskva/odezhda_obuv_aksessuary?'
    page = 'p='
    query = '&q=patagonia'

    total_pages = get_count_pages(get_html(url))

    for i in range(1, total_pages + 1):
        url_gen = base_url + page + str(i) + query
        html = get_html(url_gen)
        get_data_from_page(html, query)


if __name__ == '__main__':
    main()


with open ('avito.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
