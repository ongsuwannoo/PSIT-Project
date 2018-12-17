import pandas, numpy, pygal

def main():
    """ arrange data """
    dataFrame17 = pandas.read_csv('Rate of Top 5 Players Earning\Top Players of 2017.csv', encoding = "ISO-8859-1")
    dataFrame16 = pandas.read_csv('Rate of Top 5 Players Earning\Top Players of 2016.csv', encoding = "ISO-8859-1")
    dataFrame15 = pandas.read_csv('Rate of Top 5 Players Earning\Top Players of 2015.csv', encoding = "ISO-8859-1")
    dataFrame14 = pandas.read_csv('Rate of Top 5 Players Earning\Top Players of 2014.csv', encoding = "ISO-8859-1")
    dataFrame13 = pandas.read_csv('Rate of Top 5 Players Earning\Top Players of 2013.csv', encoding = "ISO-8859-1")

    data17 = numpy.array(dataFrame17[['PlayerID', 'Total (Year)']]).tolist()
    data16 = numpy.array(dataFrame16[['Player ID', 'Total (Year)']]).tolist()
    data15 = numpy.array(dataFrame15[['Player ID', 'Total (Year)']]).tolist()
    data14 = numpy.array(dataFrame14[['Player ID', 'Total (Year)']]).tolist()
    data13 = numpy.array(dataFrame13[['Player ID', 'Total (Year)']]).tolist()

    var1 = loop(data13)
    var2 = loop(data14)
    var3 = loop(data15)
    var4 = loop(data16)
    var5 = loop(data17)

    graph(var1[:5], var2[:5], var3[:5], var4[:5], var5[:5])

def loop(data):
    """ loop """
    var = set()
    for i in range(len(data)):
        var.add(int(data[i][1]))
    return(sorted(list(var), reverse=True))


def graph(var1, var2, var3, var4, var5):
    """ plot graph """
    line_chart = pygal.Bar(legend_at_bottom=True, legend_at_bottom_columns=5)
    line_chart.x_labels = ('Top1', 'Top2', 'Top3', 'Top4', 'Top5')
    name = 2013
    line_chart.add("2013", var1)
    line_chart.add("2014", var2)
    line_chart.add("2015", var3)
    line_chart.add("2016", var4)
    line_chart.add("2017", var5)
    line_chart.render_to_file('RateofTop5PlayersEarning.svg')

main()
