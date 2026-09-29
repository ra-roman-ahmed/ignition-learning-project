"""
Day 07 - Using requests to pull live data from a public API.
Example: weather data for a plant site (no API key needed).
"""

import requests


def get_weather(latitude, longitude):
    """Fetch current weather for a location using Open-Meteo (free, no key)."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

    if response.status_code != 200:
        print(f"API error: status code {response.status_code}")
        return None

    return response.json()


def main():
    # Dhaka, Bangladesh - real project e ei value tumi plant site-er lat/long diye replace korbe
    latitude, longitude = 23.8103, 90.4125

    data = get_weather(latitude, longitude)

    if data is None:
        print("Could not fetch weather data.")
        return

    current = data["current"]
    temp = current["temperature_2m"]
    wind = current["wind_speed_10m"]

    print(f"Location: {latitude}, {longitude}")
    print(f"Temperature: {temp} C")
    print(f"Wind speed: {wind} km/h")


if __name__ == "__main__":
    main()