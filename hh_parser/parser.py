import requests
from bs4 import BeautifulSoup as bs

headers = {'Accept': '*/*','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0'}
url = 'https://hh.ru/search/vacancy?area=1&search_period=7&text=qa+python'


def parse_hh(url, headers):
    print('========')
    vacancies = list()
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
        for i in divs:
            title = i.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
            link = i.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = i.find('a', attrs={'data-qa':'vacancy-serp__vacancy-employer'}).text
            responsibility = i.find('div', attrs={'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text
            requirement = i.find('div', attrs={'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
            if i.find('div', attrs={'data-qa':'vacancy-serp__vacancy-compensation'}):
                salary = i.find('div', attrs={'data-qa':'vacancy-serp__vacancy-compensation'}).text
            else:
                salary = None
            vacancies.append(
                {   'title':title,
                    'company':company,
                    'url': link,
                    'requirements':requirement,
                    'responsobolities':responsibility,
                    'salary': salary
                }
            )
        return vacancies 
    else:
        print('Connection refused')






if __name__ == '__main__':
    hh = parse_hh(url,headers)
    for i in hh:
        print(i['company'],' - ', i['title'], ' - ',i['salary'])