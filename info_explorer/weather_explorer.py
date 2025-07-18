import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
import sqlite3
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

class WeatherExplorer:
    def __init__(self):
        # Get API keys from environment
        self.WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

         #creating sql database
        self.conn = sqlite3.connect("info_explorer.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS weather_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity TEXT,
            condition TEXT,
            timestamp TEXT
            )""")
        self.conn.commit()
            
            
    def get_weather(self,city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.WEATHER_API_KEY}&units=metric" 
        try:
            data = urllib.request.urlopen(url).read().decode()
        except:    
            print("Unable to connect to weather service\n Please try again.")
            return  
        info = json.loads(data)
        city_name = info['name']
        temp = info['main']['temp']
        humidity = info['main']['humidity']
        weather_description = info['weather'][0]['description']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        print(f"Weather in {city_name}:\n Temperature : {temp}\n Humidity : {humidity}\n Condition : {weather_description}")
        print("\nThank You!! \n\n")
        print('-'*30)

        with open('sample_output.txt','w') as file:
            file.write(f"Weather in {city_name}:\n Temperature : {temp}\n Humidity : {humidity}\n Condition : {weather_description}")
        
       
        self.cur.execute("""
                            INSERT INTO weather_logs (city, temperature, humidity, condition, timestamp) VALUES (?,?,?,?,?)
                         """,(city_name,temp,humidity,weather_description,timestamp))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
