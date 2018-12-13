import pandas as pd
import pygal as pg
dic = {}

data = pd.read_csv("esportsearning.csv") # import file
data_top = data[:20] # filter
data_top_name = data_top['TeamName'] # only name
data_top = data_top['TotalUSDPrize'] # only prize

for i in range(20):
    dic[data_top_name[i]] = data_top[i] # create dict
line_chart = pg.HorizontalBar() # set graph
line_chart.title = 'Top_Team' # graph name

for i in data_top_name:
    line_chart.add(i, dic[i]) # create
line_chart.render_to_file('Top_Team.svg') # export file svg
