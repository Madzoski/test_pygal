import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Fuehrt einen API-Aufruf durch und speichert die Antwort.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Speichert die API-Antwort in einer Variablen.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Gibt informationen ueber die Repositories aus.
repo_dicts = response_dict['items']
#print("Number of items:", len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


    #plot_dict = {
       # 'value': repo_dict['stargazers_count'],
       # 'label': repo_dict['description'],
     #    }

  #  plot_dicts.append(plot_dict)

# Erstellt die Visualisierung.
my_style = LS('#334466', base_style=LCS)

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
chart.title = 'Meist angeSTARte Projekte auf GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')