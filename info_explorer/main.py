from weather_explorer  import WeatherExplorer
from country_explorer import CountryExplorer
from nasa_explorer import NasaExplorer
import sqlite3


def main():
    #calling all the classes
    weather = WeatherExplorer()
    country = CountryExplorer()
    nasa = NasaExplorer()

    try:
        while True:
            #printing Menu
            print("\n🌐 Info Explorer Menu:")
            print("1. Check City Weather\n2. Get Country Info\n3. View NASA Astronomy Picture \n4. View Previous Weather logs\n5.View Previous Country logs\n6.View previous Nasa logs\n7. EXIT\n\n")
            try:
                    choice = int(input("Please Enter Your Choice : ").strip())
            except:
                print("Invalid Input!!!\n")
                continue

            if choice == 1:

                try:
                    city = input("Enter the city you want weather for : ").strip().lower().title()
                except:
                    print("City not found!!!\n")
                    continue
                weather.get_weather(city)

            elif choice == 2:

                try:
                    country_name = input("Enter the country you want info for : ").strip().lower().title()
                except:
                    print("Country not found!!!")
                    continue    
                country.get_country_info(country_name)
            
            elif choice == 3:
                nasa = NasaExplorer()
                nasa.get_apod()
                    
            elif choice == 4:

                conn = sqlite3.connect("info_explorer.db")
                cur = conn.cursor()
                cur.execute("SELECT city, temperature, humidity, condition, timestamp FROM weather_logs ORDER BY id DESC LIMIT 5")
                rows = cur.fetchall()
                print("\n🕘 Last 5 Weather Searches:")
                for row in rows:
                    print(f"{row[4]} — {row[0]} | Temp: {row[1]}°C | Humidity: {row[2]}% | Condition: {row[3]}")
                print('-' * 40)
                cur.close()
                conn.close()
            
            elif choice == 5:

                conn = sqlite3.connect("info_explorer.db")
                cur = conn.cursor()
                cur.execute("SELECT country, capital, population, region, timestamp FROM country_logs ORDER BY id DESC LIMIT 5")
                rows = cur.fetchall()
                print("\n🕘 Last 5 Country Searches:")
                for row in rows:
                    print(f"{row[4]} — Country : {row[0]} | Capital : {row[1]} | Population: {row[2]} | Region: {row[3]}")
                cur.close()
                conn.close()

            elif choice == 6:

                conn = sqlite3.connect("info_explorer.db")
                cur = conn.cursor()
                cur.execute("SELECT title, date, url, timestamp FROM nasa_logs ORDER BY id DESC LIMIT 5")
                rows = cur.fetchall()
                print("\n🕘 Last 5 NASA Searches:")
                for row in rows : 
                    print(f"{row[3]} — Title : {row[0]} | Date : {row[1]} | Image URL: {row[2]}")
                cur.close()
                conn.close()
            
            elif choice == 7 :
                print("Thank You!!!\n Have a Good Day.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.\n")
    finally:
        weather.close()
        country.close()
        nasa.close()

# calling main 
if __name__ == "__main__":
    main()
