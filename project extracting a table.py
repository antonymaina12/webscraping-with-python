import requests
from bs4 import BeautifulSoup
import pandas as pd

url ='https://www.nfl.com/standings/league/2019/reg/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

table =soup.find('table',{'summary':'Standings - Detailed View'})
#extracting the headers
header =[]

for i in table.find_all('th'):
    title = i.text.strip()
    header.append(title)

df =pd.DataFrame(columns = header)

for row in table.find_all('tr')[1:]:
    first_td = row.find_all('td')[0].find('div',class_ = 'd3-o-club-fullname').text.strip()
    data = row.find_all('td')[1:]
    row = [td.text.strip() for td in data]
    row.insert(0,first_td)
    length = len(df)
    df.loc[length] = row

df.to_csv("nfl_table_scraped.csv")
