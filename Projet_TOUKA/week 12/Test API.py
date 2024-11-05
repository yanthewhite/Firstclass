import requests


def get_weather_data(city, api_key):
    """
    This function retrieves weather data for a given city
    using the OpenWeatherMap API.
    :param city: str : The city for which to get the weather data
    :param api_key: str : Your OpenWeatherMap API key
    :return: dict : The weather data retrieved from the API
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather_data(data):
    """
    This function displays the weather data in a readable format.
    :param data: dict : The weather data
    """
    if data:
        city = data['name']
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} m/s")
    else:
        print("Unable to retrieve weather data. Please check the city name or your internet connection.")


def main():
    """
    The main function of the program.
    It asks the user for the city name and displays the weather forecast.
    """
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    city = input("Enter the name of your city: ")

    data = get_weather_data(city, api_key)
    display_weather_data(data)


if __name__ == "__main__":
    main()
