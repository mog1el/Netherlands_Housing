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

        address = listing.find('div', class_="listing-search-item__sub-title'").get_text(strip=True)
        address_parts = address.split()
        city = address_parts[2]
        cities.append(city)

        price_whole = listing.find('div', class_='listing-search-item__price').get_text(strip=True)
        price_parts = price_whole.split()
        price = price_parts[0]
        prices.append(price)

        area = listing.find('li', class_='illustrated-features__item--surface-area').get_text(strip=True)
        areas.append(area)

        room = listing.find('li', class_='illustrated-features__item--number-of-rooms').get_text(strip=True)
        rooms.append(room)

#%%
#Create a dataframe
df = pd.DataFrame({
    'City': cities,
    'Price': prices,
    'Area': areas,
    'Rooms': rooms
})

print(df)

#Export to CSV
df.to_csv('apartments.csv')