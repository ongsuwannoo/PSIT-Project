import pandas as pd
import pygal as pg
dic = {}

data = pd.read_csv("esportsplayer.csv") # import file
data_top_list = list(data['CountryCode'])
data_top_set = set(data['CountryCode'])

for i in data_top_set:
    dic[i] = data_top_list.count(i)
lis_top_continent_by_player = sorted(dic.items(), key=lambda x: x[1], reverse=True)

worldmap_chart = pg.maps.world.World()
worldmap_chart.title = 'Top_100_ProPlayer_Prize_by_continent'
worldmap_chart.add('Pro', dic)
worldmap_chart.render_to_file('Top_100_ProPlayer_Prize_by_continent.svg')
