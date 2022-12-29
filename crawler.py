from urllib.request import urlopen
import urllib
import time
import http.cookiejar as cookiejar
import pandas as pd
import numpy as np
import os.path
import bs4 as bs
import re
import json
import os
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import stats


def get_soup(source_address):
    hdr = {'User-Agent': 'Mozilla/5.0'}

    try:
        req = urllib.request.Request(source_address, headers=hdr)
    except:
        print('Could not complete urllib request.')
        pass
    try:
        source = urllib.request.urlopen(req, timeout=10).read()
    except:
        print('Could not create soup.')
        pass
    try:
        soup = bs.BeautifulSoup(source, 'lxml')
        return soup
    except:
        print('Could not create soup.')
        pass
    return


df = pd.DataFrame()


url_dict = {
'2005':'https://www.fifaindex.com/teams/fifa05_1/?type=1',
'2006':'https://www.fifaindex.com/teams/fifa06_2/?type=1',
'2007':'https://www.fifaindex.com/teams/fifa07_3/?type=1',
'2008':'https://www.fifaindex.com/teams/fifa08_4/?type=1',
'2009':'https://www.fifaindex.com/teams/fifa09_5/?type=1',
'2010':'https://www.fifaindex.com/teams/fifa10_6/?type=1',
'2011':'https://www.fifaindex.com/teams/fifa11_7/?type=1',
'2012':'https://www.fifaindex.com/teams/fifa12_9/?type=1',
'2013':'https://www.fifaindex.com/teams/fifa13_10/?type=1',
'2014':'https://www.fifaindex.com/teams/fifa14_13/?type=1',
'2015':'https://www.fifaindex.com/teams/fifa15_14/?type=1',
'2016':'https://www.fifaindex.com/teams/fifa16_73/?type=1',
'2017':'https://www.fifaindex.com/teams/fifa17_173/?type=1',
'2018':'https://www.fifaindex.com/teams/fifa18_278/?type=1',
'2019':'https://www.fifaindex.com/teams/fifa19_353/?type=1',
'2020':'https://www.fifaindex.com/teams/fifa20_419/?type=1',
'2021':'https://www.fifaindex.com/teams/fifa21_486/?type=1',
'2022':'https://www.fifaindex.com/teams/fifa22_528/?type=1'
}

countries = []
for year in url_dict:

	page1 = url_dict[year]
	page2 = page1.split('?')[0] + '?page=2&' + page1.split('?')[1] 
	pages = [page1, page2]

	for page in pages:
		
		try:
			soup = get_soup(page)

			for s in soup.findAll("td", attrs={"data-title": "Name"}):				

				att = s.find_next('td').find_next('td')
				mid = att.find_next('td')
				dif = mid.find_next('td')
				ovr = dif.find_next('td')

				df2 = {'country': s.text,
						'year': year,
						'att': att.text,
						'mid': mid.text,
						'def': dif.text,
						'ovr': ovr.text
						}

				df = df.append(df2, ignore_index = True)

		except:
			print("page not found", page)

df.to_csv('data/country_rating.csv')