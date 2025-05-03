import requests
from gitignore import API_KEY

url = "https://www.numbeo.com/api/"
country = "Switzerland"
fields = {"api_key": API_KEY}


r = requests.get(url + "/cities",params=fields)
data1 = r.json()
print(data1)

swiss_cities = []

if 'cities' in data1:
    for city in data1['cities']:
        if city['country'] == country:
           swiss_cities.append(city['city'])

totalPrice = 0
cityCount = 0

f = open("swiss_milk_prices.txt", "w")


for city in swiss_cities:

    fields2 = {"api_key": API_KEY,"city": city,"country": country}
    p = requests.get(url + "/city_prices", params=fields2)
    data2 = p.json()
    prices = data2.get("prices", [])

    for item in prices:
        if "Milk" in item["item_name"]:
            price = round(item['average_price'], 2)
            f.write(city + ",$" + str(price) + "\n")
            print(city + ": $" + str(price))
            totalPrice += price
            cityCount += 1
            break  
f.close()

SwitzerlandPrice = totalPrice/cityCount

print("\n" + "Average milk price in Switzerland: $" + str(round(SwitzerlandPrice, 2)))
