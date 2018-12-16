import pandas, numpy, pygal

def main():
    """ arrange data """
    dataFrame1 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\June2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame2 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\July2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame3 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\August2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame4 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\September2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame5 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\October2018(Youtube).csv', encoding = "ISO-8859-1")
    # data1 is list()    
    data1 = numpy.array(dataFrame1[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame2[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame3[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame4[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame5[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    # data2 is set()
    data2 = set()
    for i in range(len(data1)):
        data2.add(data1[i][0])
    # data3 is dict()
    data3 = dict()
    for i in data2:
        data3[i] = 0
    for i in range(len(data1)):
        data3[data1[i][0]] += data1[i][1]
    var = sorted(data3.items(), key=lambda x: x[1], reverse=True)
    graph(var)


def graph(var):
    """ plot graph """
    from pygal.style import Style
    custom_style = Style(
    legend_font_size=8,
    title_font_size=10,
    legend_at_bottom_columns=3,
    plot_background='#FFFFFF',
    background='#FFFFFF')

    line_chart = pygal.Bar(x_title='Third Graph', style=custom_style, truncate_legend=1500)
    for i in range(10):
        line_chart.add(var[i][0], var[i][1])
    line_chart.render_to_file('mostviewedyoutube.svg')

main()
