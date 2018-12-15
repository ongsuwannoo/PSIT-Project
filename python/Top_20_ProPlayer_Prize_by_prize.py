import pandas as pd
import pygal as pg
data_20_prize = {}

data = pd.read_csv("esportsplayer.csv") # import file
data_top_prize = list(data['TotalUSDPrize'])
data_top_name = list(data['CurrentHandle'])
for i in range(20):
    data_20_prize[data_top_name[i]] = data_top_prize[i]
data_20_prize = sorted(data_20_prize.items(), key=lambda x: x[1], reverse=True)

line_chart = pg.HorizontalBar()
line_chart.title = 'Top 20 Pro Player with the highest reward prize (in Dollars)' # graph name
for i in data_20_prize:
    line_chart.add(i[0], i[1]) # create
line_chart.render_to_file('Top_20_ProPlayer_Prize_by_prize.svg') # export file svg
