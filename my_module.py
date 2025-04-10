import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap
from PIL import Image, ImageTk

# Huge thanks to Alina Chudnova for the main application

# Create a window in ttkbootstrap
root = ttkbootstrap.Window(themename="morph")
# Give the window a name
root.title("WWeather")
# Sets the resolution that the window will open at
root.geometry("1024x768")
# Set the minimum resolution or 'size' of the window
root.minsize(width=800, height=500)

# Function for getting the weather for the entererd location
def get_weather(city):
    """ Uses the API key to fetch and output the data from the url, making a request in the process
    
    Args: 
        icon_id (str): the identification for the icon that represents the weather
        temperature (float): the temperature of the entered location
        city (str): the entered location
        country (str): country the location is in
        description (str): weather description

    Returns: 
        .json file: includes the weather, an icon_id associated with the weather, temperature, city and country
    """
    api_key_one = "8f19c2c2e8a325a07b2c35bfe43d861b"
    url_one = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key_one}'
    res_one = requests.get(url_one)
    
    # If the user enters error, the program will output 'City Not Found'
    if res_one.status_code == 404:
        messagebox.showerror("Error", "City Not Found")
        return None
    
    ### Below is for the other, more accurate WeatherAPI which did not work for this program
    # api_key_two = "ce6207a53a45475db3c90051252703"
    # url_two = f'http://api.weatherapi.com/v1/forecast.json?key={api_key_two}&q={city}&days=1&aqi=no&alerts=no'
    # res_two = requests.get(url_two)
    # if res_two.status_code == 404:
        # messagebox.showerror("Error", "City Not Found")
        # return None
    
    weather_one = res_one.json()
    # weather_two = res_two.json()
    icon_id = weather_one["weather"][0]["icon"]
    temperature = weather_one["main"]["temp"]
    description = weather_one["weather"][0]["description"]
    city = weather_one["name"]
    country = weather_one["sys"]["country"]

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Function to fetch weather from user entered location
def search():
    """ A search button that allows the user to actually search for the weather

        Args:
            city (str): the entered location
        
        Returns:
            a visual display of the results from the .json file. 
    """
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

# Function to change the theme
def change_theme(event):
    selected_theme = theme_menu.get()
    root.style.theme_use(selected_theme)

def resize_text(event):
    # Calculate font size based on window width
    new_font_size = int(event.width/20)
    if new_font_size < 36:  # Set a minimum font size
        new_font_size = 36
    title_text.config(font=("Helvetica", new_font_size))

# Display the Name of the weather application
title_text = tk.Label(root, text="WWeather", font=("Helvetica", 36))
title_text.pack(expand=True, fill=tk.BOTH, pady=5)

# Bind the <Configure> event to adjust text size dynamically
root.bind("<Configure>", resize_text)

# Give the user a space to enter their city of choice
city_entry = ttkbootstrap.Entry(root, font= "Helvetica, 18")
city_entry.pack(pady=10)

# Make the user able to simply press the ENTER key to fetch weather data (does not work yet)
root.bind('<Return>', get_weather)

# Create and display a search button in order to fetch the weather
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Outputs the location entered by the user
location_label = tk.Label(root, font= "Helvetica, 25")
location_label.pack(pady=20)

# Create the icon for the weather description and place it in the GUI
icon_label = tk.Label(root)
icon_label.pack()

# This will output the temperature of the entered location
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# This will be the output of the description of the weather
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

#This uses the style.themenames function in Combobox in ttkbootstrap
theme_menu = ttkbootstrap.Combobox(root, values=root.style.theme_names(), state="readonly") # make it so that the user cannot add any themes that do not exist
theme_menu.set("Select Theme")  # Default text
theme_menu.bind("<<ComboboxSelected>>", change_theme)  # Bind the selection of the theme menu to a function that changes the theme
theme_menu.pack(pady=5)

root.mainloop()