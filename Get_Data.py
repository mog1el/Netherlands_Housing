import requests
from bs4 import BeautifulSoup
import pandas as pd
#%%
#defining the urls
urls = [f"https://www.pararius.com/apartments/nederland/page-{i}" for i in range (1, 67)]
cities = []
prices = []
areas = []
rooms = []
#%%
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = soup.find_all('section', class_='listing-search-item')

    for listing in listings:
        #the true price only the first word. Important to know that price is per month
        price_whole = listing.find('div', class_='listing-search-item__price').get_text(strip=True)
        price_parts = price_whole.split()
        price = price_parts[0]
        price = price.replace('€', '').replace(',', '')
        prices.append(price)

        #city is the 3rd word of an address and I'm only interested in this data
        address = listing.find('div', class_="listing-search-item__sub-title'").get_text(strip=True)
        address_parts = address.split()
        city = address_parts[2]
        cities.append(city)

        areas_whole = listing.find('li', class_='illustrated-features__item--surface-area').get_text(strip=True)
        areas_parts = areas_whole.split()
        area = areas_parts[0]
        areas.append(area)

        room_whole = listing.find('li', class_='illustrated-features__item--number-of-rooms').get_text(strip=True)
        room_parts = room_whole.split()
        room = room_parts[0]
        rooms.append(room)

#%%
#Creating a dataframe and exporting it
df = pd.DataFrame({
    'City': cities,
    'Price': prices,
    'Area': areas,
    'Rooms': rooms
})
df = df.drop(df[df.Price == 'Price'].index)
print(df)

df.to_csv('apartments.csv', header = False, index = False)