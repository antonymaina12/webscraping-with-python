import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/s/Honululu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Honululu%2C%20HI%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
soup =BeautifulSoup(page.text,'lxml')

#part 2
df = pd.DataFrame({'links':[''], 'Title':[''],'Details':[''],'Price':[''],'Ratings':['']})
while True:

    postings = soup.find_all('div',class_ ='_8ssblpx')
    for post in postings:
    try:
        link = post.find('a',class_ = '_gjfol0').get('href')
        link_full = 'https://www.airbnb.ca'+link
        title = post.find('a',class_ = '_gjfol0').get('aria-label')
        details =post.find_all('div',class_ = '_kqh46o')[0].text
        #description = post.find_all('div',class_ = '_kqh46o')[1].text
        price = post.find('span', class_='_olc9rf0').text
        rating = post.find('span', class_='_10fy1f8').text
        df = df.append({'links':link_full, 'Title':title,'Details':details,'Price':price,
                        'Ratings':rating},ignore_index=True)
    except:
        pass
    
next_page = soup.find('a',{'aria-label':'Next'}).get('href')
next_page_full = 'https://www.airbnb.ca'+next_page

url =next_page_full
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

