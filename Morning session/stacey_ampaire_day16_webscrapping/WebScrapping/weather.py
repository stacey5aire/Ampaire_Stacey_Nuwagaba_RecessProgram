#Exercise1 : Scrape data from the http://openweathermap.org
# Current weather data 
# Libraries for web scraping
import requests
from bs4 import BeautifulSoup
import csv
import json

# Step 2: Fetch the web pages with API key as query parameter
api_key = 'b66248ba53216292ef33a11cc1511b5c' 
city = 'kampala'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


response = requests.get(url)
weather_data = response.json()


# Step 3: Parse the JSON response
data = [{
    'city': weather_data['name'],
    'temperature': weather_data['main']['temp'],
    'weather': weather_data['weather'][0]['description'],
    'humidity': weather_data['main']['humidity'],
    'pressure': weather_data['main']['pressure'],
    'wind_speed': weather_data['wind']['speed']
}]
# Step 4: Save the data to a CSV file
csv_file = 'weather_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerow(data[0])

# Step 5: Save the data to a JSON file
json_file = 'weather_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Step 6: Save successfully to csv and json format
print(f'Data saved successfully to {csv_file} and {json_file} format!')