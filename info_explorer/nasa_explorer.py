import urllib.error,urllib.parse,urllib.request
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
import sqlite3
from datetime import datetime
# Load environment variables from .env file
load_dotenv()

class NasaExplorer:
    def __init__(self):
        # Get API keys from environment3
        self.NASA_API_KEY = os.getenv("NASA_API_KEY")
        print(f"NASA_API_KEY loaded: {self.NASA_API_KEY}")

        self.conn = sqlite3.connect("info_explorer.db")
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS nasa_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                date TEXT,
                url TEXT,
                timestamp TEXT
            )
        ''')
        self.conn.commit()
    
    def get_apod(self):
        print("Fetching today's Nasa astronomy photo info.........\n....\n")

        url = f'https://api.nasa.gov/planetary/apod?api_key={self.NASA_API_KEY}'
        try:
            data = urllib.request.urlopen(url).read().decode()
        except Exception as e:
            print("NASA service unavailabl",e)
            return
        info = json.loads(data)

        date = info['date']
        title =info['title']
        explanation = info['explanation']
        image_url = info.get('hdurl') or info.get('url')
        media_type = info['media_type']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Date : {date}\n Title : {title}\n Explanation : {explanation}\n Image URL : {image_url}\n Media Type : {media_type}\n\n")
        print("Thank You!!!")
        print('-'*30)

        with open('sample_output.txt','w') as file:
            file.write(f"Date : {date}\n Title : {title}\n Explanation : {explanation}\n Image URL : {image_url}\n Media Type : {media_type}\n\n")
        
         # Log to database
        self.cur.execute('''
            INSERT INTO nasa_logs (title, date, url, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (title, date, image_url, timestamp))
        self.conn.commit()
    
    def close(self):
        self.cur.close()
        self.conn.close()

