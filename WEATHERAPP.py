import customtkinter as ctk
import requests
from PIL import Image
from customtkinter import CTkImage

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue", etc.

# Create the main application window
app = ctk.CTk()
app.title("Weather App")
app.geometry("400x400")

API_KEY = '2374116c94899336a4c73851cb37d756'  # Replace with your OpenWeatherMap API key

# Create a label and entry for city input
city_label = ctk.CTkLabel(app, text="Enter City:", font=("Arial", 16))
city_label.pack(pady=10)

city_entry = ctk.CTkEntry(app, placeholder_text="City Name", font=("Arial", 16))
city_entry.pack(pady=10)

# Create a button to fetch weather
fetch_button = ctk.CTkButton(app, text="Get Weather", command=lambda: get_weather(), font=("Arial", 14))
fetch_button.pack(pady=10)

# Create a label to display the weather icon
icon_label = ctk.CTkLabel(app, text="")
icon_label.pack(pady=10)

# Create a label to display the current weather result
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14),fg_color="cyan3", corner_radius=10)
result_label.pack(pady=10, padx=10, fill="both")

# Create a label to display the forecast result
forecast_label = ctk.CTkLabel(app, text="", font=("Arial", 12), fg_color="cyan4", corner_radius=10)
forecast_label.pack(pady=10, padx=10, fill="both")

def get_weather():
    city = city_entry.get()
    current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    # Fetch current weather
    current_response = requests.get(current_url)
    current_data = current_response.json()

    if current_response.status_code == 200:
        weather_desc = current_data['weather'][0]['description']
        temperature = current_data['main']['temp']
        humidity = current_data['main']['humidity']
        pressure = current_data['main']['pressure']
        icon_code = current_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        # Load and display the icon
        try:
            icon_image = Image.open(requests.get(icon_url, stream=True).raw)
            icon_image = icon_image.resize((50, 50), Image.LANCZOS)
            icon_photo = CTkImage(light_image=icon_image, dark_image=icon_image)  # Use CTkImage

            icon_label.configure(image=icon_photo)
            icon_label.image = icon_photo  # Keep a reference to avoid garbage collection
        except Exception as e:
            icon_label.configure(text="Icon not available")
            print(f"Error loading icon: {e}")

        result_label.configure(text=f"Weather: {weather_desc.capitalize()}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nPressure: {pressure} hPa")

        # Fetch 5-day forecast
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        if forecast_response.status_code == 200:
            forecast_text = "5-Day Forecast:\n"
            for i in range(0, len(forecast_data['list']), 8):  # Every 8th entry is a new day
                day = forecast_data['list'][i]
                forecast_temp = day['main']['temp']
                forecast_desc = day['weather'][0]['description']
                forecast_date = day['dt_txt'].split(" ")[0]  # Get only the date part
                forecast_text += f"{forecast_date}: {forecast_temp}°C, {forecast_desc.capitalize()}\n"
            forecast_label.configure(text=forecast_text)
        else:
            forecast_label.configure(text="Forecast data not available.")
    else:
        result_label.configure(text="City not found. Please try again.")
        forecast_label.configure(text="")
        icon_label.configure(image='')  # Clear the icon if city is not found

# Run the application
app.mainloop()