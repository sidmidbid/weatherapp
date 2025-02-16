import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "0cff01a1f8c71b1f41eb32ea487b45b8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = f"Weather: {data['weather'][0]['description']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Wind Speed: {data['wind']['speed']} m/s"
        result_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
