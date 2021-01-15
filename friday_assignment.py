#Part 1
import json

#Open the stations.csv file
with open ('stations.csv') as file:
    print('stations.csv')

stations = 'stations.csv'
#station_code = 'GHCND:US1WAKG0038' # To get it from station.csv for parts I-II

#Identify and choose the measurenents a station code
with open('precipitation.json', encoding ='utf8') as file:
    precipitation_data = json.load(file)

#Creating a list with all the station codes for each location

station_codes = ['GHCND:USW00093814', 'GHCND:US1WAKG0038', 'GHCND:USC00513317', 'GHCND:US1CASD0032']

#Part 3: Sum precipitation and relative precipitation for each location
#For each location it splits the date measurement into months and then measures the relative precipitation per month and for 12 months

for station_code in station_codes:
    measurement_sum = 0
    measurement_monthly_sum = [0]*12
    for measurement in precipitation_data:
        station = measurement['station']
        date = measurement['date']
        value = measurement['value']
        if station == station_code:
            date = date.split('-') #to get year, month, day separately in a dictionary
            #Sum of measurements per month
            month = int(date[1])-1
            measurement_monthly_sum[month] += value
            #Sum of precipitation for 12 months
            measurement_sum += measurement['value']


#Part 2 - Sum precipitation and relative precipitation per month
percentage_month = []
for month in measurement_monthly_sum:
    percentage = (month/measurement_sum)*100
    percentage_month.append(percentage)

    print(f'The relative precipitation per month is {measurement_monthly_sum}')
    print(f'The relative precipitation over 12 months is {measurement_sum}')
    print(f'The yearly relative percentage of precepitation in each location is {percentage_month}')

# shows reults in a list of dictionaries with new measurements/variables that we gained in parts 1-3
results = precipitation_data.append(measurement_monthly_sum, measurement_sum, percentage, percentage_month)
print(results)

#Save a .json file (I'm not sure if that works or not.)
# with open ('friday_assignment.json', 'w', encoding ='utf8') as file
#     json.dump(measurement_monthly_sum)
#     json.dump(percentage_month)

"""
Expected output:
A list of relative percipitation per month and over year
"""
