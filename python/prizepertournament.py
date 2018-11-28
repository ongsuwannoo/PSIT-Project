import pandas, numpy, pygal
def main():
    """ arrange data """
    dataFrame = pandas.read_csv('earningbytournaments.csv', encoding = "ISO-8859-1")
    data = numpy.array(dataFrame[['TournamentName','Prize']]).tolist()
    graph(data)
    
def graph(data):
    """ plot graph """
    line_chart = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=3)
    line_chart.title = 'Top 12 Highest Tournaments Earning (in Dollars)'
    for i in range(12):
        line_chart.add(str(data[i][0]), [{'value': int(data[i][1]), 'label': '{:.2f}%'.format(100*int(data[i][1])/sum([j[1] for j in data]))}])
    line_chart.render_to_file('earningbytournaments.svg')  

main()
