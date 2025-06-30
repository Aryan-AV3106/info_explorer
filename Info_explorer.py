import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NASA_API_KEY = os.getenv("NASA_API_KEY")

# Printing the Menu

print("Welcome to Info Explorer ")
print("What would you like to do today?")

while True:
    print(" 1. Check City Weather\n 2. Get Country Info\n 3. View NASA Astronomy Picture \n 4. Exit")
    try:
        choice = int(input("Please Enter Your Choice : ").strip())
    except:
        print("Invalid Input!!!")
        continue
    if choice == 1:
        try:
            city = input("Enter the city you want weather for : ").strip()
        except:
            print("City not found!!!")
            continue

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        
        try:
            data = urllib.request.urlopen(url).read().decode()
        except:    
            print("Unable to connect to weather service\n Please try again.")
            continue
        
        info = json.loads(data)
        city_name = info['name']
        temp = info['main']['temp']
        humidity = info['main']['humidity']
        weather_description = info['weather'][0]['description']
        print(f"Weather in {city_name}:\n Temperature : {temp}\n Humidity : {humidity}\n Condition : {weather_description}")
        print("\nThank You!! \n\n")
        print('-'*30)

        with open('sample_output.txt','w') as file:
            file.write(f"Weather in {city_name}:\n Temperature : {temp}\n Humidity : {humidity}\n Condition : {weather_description}")
        


    elif choice == 2:
        try:
            country = input("Enter the country you want info for : ").strip()
        except:
            print("Country not found!!!")
            continue
        
        url = f"https://restcountries.com/v3.1/name/{country}"
        
        try:
            data = urllib.request.urlopen(url).read().decode()
        except:    
            print("Unable to connect to service\n Please try again.")
            continue

        info = json.loads(data)
        country_name = info[0]['name']['common']
        capital = info[0]['capital'][0]
        region = info[0]['region']
        population = info[0]['population']
        
        print(f"Country : {country_name}\n Capital : {capital}\n Region : {region}\n Population : {population}\n")
        print("\nThank You!! \n\n")
        print('-'*30)

        with open('sample_output.txt','w') as file:
            file.write(f"Country : {country_name}\n Capital : {capital}\n Region : {region}\n Population : {population}\n")
        



    elif choice == 3:
        print("Fetching today's Nasa astronomy photo info.........\n....\n")

        url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
        try:
            data = urllib.request.urlopen(url).read().decode()
        except:
            print("NASA service unavailable, please try again later.")
            continue
        info = json.loads(data)

        date = info['date']
        title =info['title']
        explanation = info['explanation']
        image_url = info['hdurl']
        media_type = info['media_type']

        print(f"Date : {date}\n Title : {title}\n Explanation : {explanation}\n Image URL : {image_url}\n Media Type : {media_type}\n\n")
        print("Thank You!!!")
        print('-'*30)

        with open('sample_output.txt','w') as file:
            file.write(f"Date : {date}\n Title : {title}\n Explanation : {explanation}\n Image URL : {image_url}\n Media Type : {media_type}\n\n")

        
    elif choice == 4:
        print("Thank You!!!\n Have a Good Day.")
        break

    else:
        print("Invalid Choice !!! ")
    
