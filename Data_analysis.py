data = open('apartments.csv')

cities = []
for row in data:
    if row.split(',')[0] not in cities:
        cities.append(row.split(',')[0])

average_prices = {}
city_counts = {}
total_city_price = {}
for city in cities:
    for row in data:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
        if row.split(',')[0] == city:
            total_city_price[city] += int(row.split(',')[1])

print(total_city_price)