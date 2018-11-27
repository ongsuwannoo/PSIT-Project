import pandas as pd
import pygal as pg
dic = {}

data = pd.read_csv("esportsplayer.csv") # import file
data_top_list = list(data['Highest Paying Game'])
data_top_set = set(data['Highest Paying Game'])

for i in data_top_set:
    dic[i] = data_top_list.count(i)
lis_top_game_by_player = sorted(dic.items(), key=lambda x: x[1], reverse=True)

pie_chart = pg.Pie()
pie_chart.title = 'Top_100_ProPlayer_Prize_by_game'
for i in range(len(lis_top_game_by_player)):
    pie_chart.add(lis_top_game_by_player[i][0], lis_top_game_by_player[i][1])
pie_chart.render_to_file('Top_100_ProPlayer_Prize_by_game.svg')
