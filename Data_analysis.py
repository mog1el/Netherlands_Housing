data = open('apartments.csv')

cities = []
average_prices = {}
city_counts = {}
total_city_price = {}
meters_sq = {}
average_per_meter = {}

for row in data:
    city = row.split(',')[0]
    price = int(row.split(',')[1])
    area = int(row.split(',')[2])
    if city not in city_counts:
        city_counts[city] = 0
        total_city_price[city] = 0
        meters_sq[city] = 0
    else:
        city_counts[city] += 1
        total_city_price[city] += price
        meters_sq[city] += area
    
    if city not in cities:
        cities.append(city)

for city in cities:
    if city_counts[city] != 0:
        average_prices[city] = total_city_price[city]/city_counts[city]
        average_per_meter[city] = total_city_price[city]/meters_sq[city]

average_per_meter = (dict(sorted(average_per_meter.items(), key=lambda item: item[1])))
print(average_per_meter)