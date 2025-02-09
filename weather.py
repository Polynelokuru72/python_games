import requests

def weather_app():
    api_key = "YOUR_API_KEY"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city = input("Enter city name: ")
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found.")

weather_app()
