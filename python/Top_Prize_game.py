import pandas as pd
import pygal as pg
from pygal.style import Style
lis, temp = [[], [], [], [], []], []
rank = ['1st', '2nd', '3rd', '4th', '5th']
rank.reverse()

for i in range(2012, 2018):
    name = "TopGamesof"+str(i)
    data = pd.read_csv(name+".csv")
    data_prize = list(data['TotalPrize'])
    data_prize.sort(reverse=True)

    for j in range(5):
        lis[j].append(data_prize[j])
lis.reverse()

custom_style = Style(
    colors=('#FF6600', '#FFD800', '#34DDDD', '#C1D208', '#D01A55'))

line_chart = pg.Bar(legend_at_bottom=True, legend_at_bottom_columns=5, style=custom_style)
line_chart.x_labels = map(str, range(2012, 2018))
line_chart.title = 'Top_Prize_game'
for i in range(5):
    line_chart.add(rank[i], lis[i])
line_chart.render_to_file('Top_Prize_game.svg')