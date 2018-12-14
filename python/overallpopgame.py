import pandas, numpy, pygal

def main():
    """ arrange data """
    dataFrame1 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\June2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame2 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\July2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame3 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\August2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame4 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\September2018(Youtube).csv', encoding = "ISO-8859-1")
    dataFrame5 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\October2018(Youtube).csv', encoding = "ISO-8859-1")

    dataFrame6 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\June2018(Twitch).csv', encoding = "ISO-8859-1")
    dataFrame7 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\July2018(Twitch).csv', encoding = "ISO-8859-1")
    dataFrame8 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\August2018(Twitch).csv', encoding = "ISO-8859-1")
    dataFrame9 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\September2018(Twitch).csv', encoding = "ISO-8859-1")
    dataFrame10 = pandas.read_csv('Most Watched Games on Twitch & YouTube Gaming\October2018(Twitch).csv', encoding = "ISO-8859-1")

    # data1 is list()
    data1 = numpy.array(dataFrame1[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame2[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame3[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame4[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame5[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame6[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame7[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame8[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame9[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()
    data1 += numpy.array(dataFrame10[['TITLE', 'ESPORTS HOURS(MILLION)']]).tolist()

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

    typ = {'League of Legends': 'MOBA', 'Dota 2': 'MOBA', 'Counter-Strike: Global Offensive': 'FPS',\
     'Hearthstone': 'CCG', 'Overwatch': 'FPS', 'Heroes of the Storm': 'MOBA', 'StarCraft II': 'RTS', \
     "PLAYERUNKNOWN'S BATTLEGROUNDS": 'BR', 'Rocket League': 'Sports',\
      "Tom Clancy's Rainbow Six: Siege": 'Tactical shooter', 'Street Fighter V': 'Fighting', \
      'Call of Duty: WWII': 'FPS', 'World of Warcraft': 'MMORPGs', 'Arena of Valor': 'MOBA', \
      'Magic: The Gathering':'CCG', 'Fortnite': 'BR', 'Age of Empires': 'RTS', 'Super Smash Bros. Melee': 'Fighting'\
      , 'FIFA 18': 'Sports', 'Warface': 'FPS', 'Garena RoV: Mobile MOBA': 'MOBA', 'FIFA Online 4': 'Sports'}

    lis, dic_2 = [], {}
    for i in var:
        if i[0] not in typ:
            pass
        else:
            if typ[i[0]] not in dic_2:
                dic_2[typ[i[0]]] = 1
            else:
                dic_2[typ[i[0]]] += 1
            lis.append(typ[i[0]])
    lis_1 = sorted(dic_2.items(), key=lambda x: x[1], reverse=True)
    graph(dic_2, lis, lis_1)


def graph(dic_2, lis, lis_1):
    """ plot graph """
    line_chart = pygal.Pie()
    for i in lis_1:
        line_chart.add(i[0], (int(((i[1]*100)/(len(lis))*100)))/100)
    line_chart.render_to_file('overallpopgame.svg')


main()