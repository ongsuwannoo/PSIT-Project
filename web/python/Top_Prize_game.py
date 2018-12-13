import pandas as pd
import pygal as pg
from pygal.style import NeonStyle
dic = {}
lis = []
name_game_all = set()
year = list(range(2012, 2018))
for i in range(2012, 2018):
    name = "TopGamesof"+str(i)
    data = pd.read_csv(name+".csv")
    data_name = list(data['NameGame'])
    data_prize = list(data['TotalPrize'])
    for j in range(5):
        dic[data_name[j]] = data_prize[j]
    lis.append(dic)
    dic = {}

for i in range(6):
    for j in lis[i]:
        name_game_all.add(j)

name_game_all = list(name_game_all)
for i in range(len(name_game_all)):
    dic[name_game_all[i]] = []
    for j in range(6):
        if name_game_all[i] in lis[j]:
            dic[name_game_all[i]].append(lis[j][name_game_all[i]])
        else:
            dic[name_game_all[i]].append(None)

line_chart = pg.Bar()
line_chart.title = 'Top_Prize_game'
line_chart.x_labels = map(str, range(2012, 2018))
for i in dic:
    line_chart.add(i, dic[i])
line_chart.render_to_file('Top_Prize_game.svg')