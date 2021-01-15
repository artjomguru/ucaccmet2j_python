#Part 1
import json

stations = 'stations.csv'
station_code = 'GHCND:US1WAKG0038' # To get it from station.csv

# Identify and choose the measurenents from Seattle station code
with open('precipitation.json', encoding ='utf8') as file:
    precipitation_data = json.load(file)

measurement_sum = 0
measurement_monthly_sum = [0]*12

for measurement in precipitation_data:
    station = measurement['station']
    date = measurement['date']
    value = measurement['value']
    if station == station_code:
        date = date.split('-') #to get year, month, day separately in a dictionary