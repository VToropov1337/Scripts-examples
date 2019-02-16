#!/usr/bin/env python3
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS




url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code:', r.status_code)
response_dict = r.json()

# Сохранение ответа API в переменной.
print("Total repositories:", response_dict['total_count'])

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Анализ первого репозитория.
# repo_dict = repo_dicts[0]
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])




# Анализ информации о репозиториях.
# repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#        print('\nName:', repo_dict['name'])
#        print('Owner:', repo_dict['owner']['login'])
#        print('Stars:', repo_dict['stargazers_count'])
#        print('Repository:', repo_dict['html_url'])
#        print('Description:', repo_dict['description'])
       
       
       
       
names, stars = [], []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    plot_dicts.append({'value' :repo_dict['stargazers_count'], 'label' : str(repo_dict['description']),'xlink': repo_dict['html_url']})
    

   
print(plot_dicts)

# Построение визуализации.
# my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
# chart.add('', stars)
# chart.render_to_file('python_repos.svg')
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')