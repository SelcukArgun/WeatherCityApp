import tkinter as tk
import requests


api_key = "5e54c926aba2a6649fc722b941a657f1"
latitude = "44.00"
longitude = "53.44"


def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"] - 273.15
    weather_desc = data["weather"][0]["description"]
    result_label.config(text=f"Sıcaklık: {temperature:.2f}°C\nDurum: {weather_desc.capitalize()}")

FONT = ("Arial",16,"italic")
root = tk.Tk()
root.title("Weather App")
root.minsize(width=275, height=200)
root.maxsize(width=275, height=200)


label = tk.Label(root, text="Kırklareli\nHava Durumu", font=FONT)
label.pack(pady=10)


result_label = tk.Label(root, text="", font=FONT)
result_label.pack()

update_button = tk.Button(root, text="Güncelle", command=get_weather, font=FONT)
update_button.pack()


root.mainloop()
