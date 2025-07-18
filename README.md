# 🌐 Info Explorer – Python CLI Project

Info Explorer is a simple Python project I built to practice working with real-world data using public APIs. It’s a command-line app where you can:

- Check the weather in any city 🌦️
- Get details about any country 🌍
- View NASA’s Astronomy Picture of the Day 🚀

I also added a basic database to keep track of what I searched, so I can view it later.

---

## 📌 What I Used

- **Python** (basics, classes, functions)
- **APIs** (OpenWeatherMap, RESTCountries, NASA APOD)
- **SQLite** (to save weather, country, and NASA logs)
- **`.env` file** (to keep my API keys safe)

---

## 🧪 How It Works

When you run the app, it shows you a simple menu:

🌐 Info Explorer Menu:
 1. Check City Weather
 2. Get Country Info
 3. View NASA Astronomy Picture 
 4. View Previous Data
 5.Exit

Please Enter Your Choice :     


You can type the number, and it will ask you for a city or country, then show results from the internet. Everything gets saved in a small local database.

---

## 🚀 Setup

1. Clone or download this project
2. Install Python (if you don’t have it)
3. Create a `.env` file like this:
    WEATHER_API_KEY=your_openweathermap_key
    NASA_API_KEY=your_nasa_api_key

 
4. Run the project:

```bash
python main.py

🙋‍♂️ Why I Made This
- As a CS student learning Python, I wanted to build something practical. This project helped me understand:
- How to work with external APIs
- How to store and retrieve data with SQLite
- How to organize Python code using multiple files and classes

✍️ Made by Aryan Vakharia
Student at University at Albany
Learning Python | Exploring APIs | Aspiring ML Engineer
