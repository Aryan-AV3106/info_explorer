import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
import sqlite3
from datetime import datetime


class CountryExplorer:
    def __init__(self):
        self.conn = sqlite3.connect("info_explorer.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS country_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT,
                capital TEXT,
                population INTEGER,
                region TEXT,
                timestamp TEXT
            )
        ''')     
    def get_country_info(self,country):
        url = f"https://restcountries.com/v3.1/name/{country}"
        
        try:
            data = urllib.request.urlopen(url).read().decode()
        except:    
            print("Unable to connect to service\n Please try again.")
            return

        info = json.loads(data)
        country_name = info[0]['name']['common']
        capital = info[0]['capital'][0]
        region = info[0]['region']
        population = info[0]['population']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"Country : {country_name}\n Capital : {capital}\n Region : {region}\n Population : {population}\n")
        print("\nThank You!! \n\n")
        print('-'*30)
        with open('sample_output.txt','w') as file:
            file.write(f"Country : {country_name}\n Capital : {capital}\n Region : {region}\n Population : {population}\n")
        
         # Log to database
        self.cur.execute('''
            INSERT INTO country_logs (country, capital, population, region, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (country_name, capital, population, region, timestamp))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

        