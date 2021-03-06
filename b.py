df = pd.DataFrame({'links':[''], 'Title':[''],'Details':[''],'Price':[''],'Ratings':['']})

for post in postings:

            link = post.find('a', class_ = '_gjfol0').get('href')
            link_full = 'https://www.airbnb.ca' + link
            title = post.find('a', class_ = '_gjfol0').get('aria-label')
            try:
                price = post.find('span', class_ = '_1p7iugi').text
            except:
                price = " "
            try:
                rating = post.find('span',class_ = '_10fy1f8').text
            except:
                rating = ''
            try:
                details = post.find_all('div', class_ = '_kqh46o')[0].text
            except:
                details = ''
            df = df.append({'Links':link_full, 'Title':title, 'Details':details,
                            'Price':price,'Rating':rating}, ignore_index = True)