import pandas as pd
import pygal as pg
dic = {}
dic_conties = {'ad': 'Andorra', 'ae': 'United', 'af': 'Afghanistan', 'al': 'Albania', \
'am': 'Armenia', 'ao': 'Angola', 'aq': 'Antarctica', 'ar': 'Argentina', 'at': 'Austria', \
'au': 'Australia', 'az': 'Azerbaijan', 'ba': 'Bosnia', 'bd': 'Bangladesh', 'be': 'Belgium', \
'bf': 'Burkina', 'bg': 'Bulgaria', 'bh': 'Bahrain', 'bi': 'Burundi', 'bj': 'Benin', 'bn': 'Brunei', \
'bo': 'Bolivia,', 'br': 'Brazil', 'bt': 'Bhutan', 'bw': 'Botswana', 'by': 'Belarus', 'bz': 'Belize', \
'ca': 'Canada', 'cd': 'Congo,', 'cf': 'Central', 'cg': 'Congo', 'ch': 'Switzerland', 'ci': 'Cote', \
'cl': 'Chile', 'cm': 'Cameroon', 'cn': 'China', 'co': 'Colombia', 'cr': 'Costa', 'cu': 'Cuba', \
'cv': 'Cape', 'cy': 'Cyprus', 'cz': 'Czech', 'de': 'Germany', 'dj': 'Djibouti', 'dk': 'Denmark', \
'do': 'Dominican', 'dz': 'Algeria', 'ec': 'Ecuador', 'ee': 'Estonia', 'eg': 'Egypt', 'eh': 'Western', \
'er': 'Eritrea', 'es': 'Spain', 'et': 'Ethiopia', 'fi': 'Finland', 'fr': 'France', 'ga': 'Gabon', \
'gb': 'United', 'ge': 'Georgia', 'gf': 'French', 'gh': 'Ghana', 'gl': 'Greenland', 'gm': 'Gambia', \
'gn': 'Guinea', 'gq': 'Equatorial', 'gr': 'Greece', 'gt': 'Guatemala', 'gu': 'Guam', 'gw': 'Guinea-Bissau', \
'gy': 'Guyana', 'hk': 'Hong', 'hn': 'Honduras', 'hr': 'Croatia', 'ht': 'Haiti', 'hu': 'Hungary', \
'id': 'Indonesia', 'ie': 'Ireland', 'il': 'Israel', 'in': 'India', 'iq': 'Iraq', 'ir': 'Iran', \
'is': 'Iceland', 'it': 'Italy', 'jm': 'Jamaica', 'jo': 'Jordan', 'jp': 'Japan', 'ke': 'Kenya', \
'kg': 'Kyrgyzstan', 'kh': 'Cambodia', 'kp': 'Korea,', 'kr': 'Korea', 'kw': 'Kuwait', \
'kz': 'Kazakhstan', 'la': 'Lao', 'lb': 'Lebanon', 'li': 'Liechtenstein', 'lk': 'Sri', 'lr': \
'Liberia', 'ls': 'Lesotho', 'lt': 'Lithuania', 'lu': 'Luxembourg', 'lv': 'Latvia', \
'ly': 'Libyan', 'ma': 'Morocco', 'mc': 'Monaco', 'md': 'Moldova,', 'me': 'Montenegro', 'mg': \
'Madagascar', 'mk': 'Macedonia', 'ml': 'Mali', 'mm': 'Myanmar', 'mn': 'Mongolia', 'mo': 'Macao', \
'mr': 'Mauritania', 'mt': 'Malta', 'mu': 'Mauritius', 'mv': 'Maldives', 'mw': 'Malawi', 'mx': 'Mexico', \
'my': 'Malaysia', 'mz': 'Mozambique', 'na': 'Namibia', 'ne': 'Niger', 'ng': 'Nigeria', \
'ni': 'Nicaragua', 'nl': 'Netherlands', 'no': 'Norway', 'np': 'Nepal', 'nz': 'New', \
'om': 'Oman', 'pa': 'Panama', 'pe': 'Peru', 'pg': 'Papua', 'ph': 'Philippines', \
'pk': 'Pakistan', 'pl': 'Poland', 'pr': 'Puerto', 'ps': 'Palestine,', 'pt': 'Portugal', \
'py': 'Paraguay', 're': 'Reunion', 'ro': 'Romania', 'rs': 'Serbia', 'ru': 'Russian', 'rw': \
'Rwanda', 'sa': 'Saudi', 'sc': 'Seychelles', 'sd': 'Sudan', 'se': 'Sweden', 'sg': 'Singapore', \
'sh': 'Saint', 'si': 'Slovenia', 'sk': 'Slovakia', 'sl': 'Sierra', 'sm': 'San', 'sn': 'Senegal', \
'so': 'Somalia', 'sr': 'Suriname', 'st': 'Sao', 'sv': 'El', 'sy': 'Syrian', 'sz': 'Swaziland', \
'td': 'Chad', 'tg': 'Togo', 'th': 'Thailand', 'tj': 'Tajikistan', 'tl': 'Timor-Leste', \
'tm': 'Turkmenistan', 'tn': 'Tunisia', 'tr': 'Turkey', 'tw': 'Taiwan', 'tz': 'Tanzania,', \
'ua': 'Ukraine', 'ug': 'Uganda', 'us': 'United', 'uy': 'Uruguay', 'uz': 'Uzbekistan', \
'va': 'Holy', 've': 'Venezuela,', 'vn': 'Viet', 'ye': 'Yemen', 'yt': 'Mayotte', \
'za': 'South', 'zm': 'Zambia', 'zw': 'Zimbabwe'}

data = pd.read_csv("esportsplayer.csv") # import file
data_top_list = list(data['CountryCode']) # list Countries all
data_top_set = set(data['CountryCode']) # set Country

for i in data_top_set:
    dic[i] = data_top_list.count(i) # count countries
lis_top_continent_by_player = sorted(dic.items(), key=lambda x: x[1], reverse=True) # sort

worldmap_chart = pg.maps.world.World(legend_at_bottom=True, legend_at_bottom_columns=8)
worldmap_chart.title = 'Top_100_ProPlayer_Prize_by_continent'
for i in lis_top_continent_by_player:
    worldmap_chart.add(dic_conties[i[0]], {i[0]: dic[i[0]]})
worldmap_chart.render_to_file('Top_100_ProPlayer_Prize_by_continent.svg')
