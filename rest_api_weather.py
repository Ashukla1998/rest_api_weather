import requests

API_KEY = 'f5857f5577a6fa59271adbef5ecf7b10'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('main', {}).get('temp'), data.get('wind', {}).get('speed'), data.get('main', {}).get('pressure')
    else:
        print(f"Error: {response.json().get('message', 'Unknown error')}")
        return None

def user_option():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return int(input("Enter your choice: "))

def main():
    while True:
        option = user_option()

        if option == 0:
            print("Terminating the program.")
            break

        elif option in [1, 2, 3]:
            city = input("Enter the city name: ")

            weather_data = weather_data(city)
            if weather_data is not None:
                if option == 1:
                    temp, _, _ = weather_data
                    print(f"The temperature in {city} is {temp}°C.")
                elif option == 2:
                    _, wind_speed, _ = weather_data
                    print(f"The wind speed in {city} is {wind_speed} m/s.")
                elif option == 3:
                    _, _, pressure = weather_data
                    print(f"The pressure in {city} is {pressure} hPa.")
        else:
            print("Invalid option. Please choose a valid option (1, 2, 3, or 0).")

if __name__ == "__main__":
    main()
