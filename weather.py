import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY_HERE"   
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        result_label.config(
            text=(
                f"City: {city.title()}\n\n"
                f"Weather: {weather}\n"
                f"Temperature: {temp} °C\n"
                f" Feels Like: {feels_like} °C\n"
                f"Humidity: {humidity} %"
            )
        )

    except requests.exceptions.RequestException:
        messagebox.showerror("Network Error", "Unable to fetch weather data.")
#GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.focus()

search_btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
)
search_btn.pack(pady=5)

result_label = tk.Label(
    root,
    text="Enter a city and click 'Get Weather'",
    font=("Arial", 12),
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()
