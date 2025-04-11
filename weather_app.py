import requests
API_KEY = "3bd36fed57c6154eacc62ca171ef0e13"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        print(f"\n📍 Weather Report for {city.title()}")
        print("------------------------------------")
        print(f"🌡️ Temperature: {main['temp']}°C")
        print(f"💧 Humidity: {main['humidity']}%")
        print(f"🌬️ Wind Speed: {wind['speed']} m/s")
        print(f"☁️ Condition: {weather['description'].title()}")
    else:
        print("\n❌ City not found or API limit reached. Please try again.")

if __name__ == "__main__":
    print("=== Simple Weather Forecast App ===")
    city = input("Enter city name: ")
    get_weather(city)
