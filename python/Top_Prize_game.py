import pandas as pd
import pygal as pg
from pygal.style import NeonStyle
dic = {}
dic_all = {}
lis = []
year = list(range(2012, 2018))
temp = {}
name_game_all = set()
for i in range(2012, 2018):
    name = "TopGamesof"+str(i)
    data = pd.read_csv(name+".csv")
    data_name = list(data['NameGame'])
    data_prize = list(data['TotalPrize'])

    for j in range(5):
        dic[data_name[j]] = data_prize[j]
        name_game_all.add(data_name[j])
    lis.append(dic)
    dic = {}

name_game_all = list(name_game_all)

for i in range(len(name_game_all)):
    dic[name_game_all[i]] = []
    for j in range(6):
        if name_game_all[i] in lis[j]:
            dic[name_game_all[i]].append(lis[j][name_game_all[i]])
        else:
            dic[name_game_all[i]].append(None)
name_game_all = []

for i in dic:
    temp[i] = dic[i].count(None)
temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
for i in temp:
    name_game_all.append(i[0])

for i in range(len(year)):
    line_chart = pg.Bar(legend_at_bottom=True, legend_at_bottom_columns=3, style=NeonStyle, rounded_bars=2)
    name = 'Top_Prize_game_'+str(year[i])
    line_chart.title = name
    line_chart.x_labels = [str(year[i])]
    for j in name_game_all:
        if dic[j][i] != None:
            line_chart.add(j, dic[j][i])
    line_chart.render_to_file(name+'.svg')