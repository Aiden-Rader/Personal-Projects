import requests
import json
import tkinter as tk
from io import BytesIO
from geopy.geocoders import GoogleV3
from PIL import Image, ImageTk
from datetime import datetime

GOOGLE_API_KEY = 'AIzaSyALrYCy2EhTUhIvi4Pkb9ukyjtvtP9VeA0'

def get_iss_location():
    # API endpoint for ISS location
    url = 'http://api.open-notify.org/iss-now.json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        iss_data = response.json()
        
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        
        date_time = datetime.now()
        run_time = date_time.strftime('%I:%M:%S %p')

        country = get_country_from_coordinates(latitude, longitude)

        display_info(latitude, longitude, run_time, country)
        update_map(latitude, longitude)
        
    except (requests.exceptions.RequestException, json.JSONDecodeError) as error:
        print(f"Error fetching ISS data: {error}")
        label.config(text='Error fetching data')

    # Schedule the next refresh after 5 seconds
    root.after(5000, get_iss_location)

def get_country_from_coordinates(latitude, longitude):
    geolocator = GoogleV3(api_key=GOOGLE_API_KEY)

    try:
        location = geolocator.reverse((latitude, longitude), language='en', exactly_one=True)

        # Look for a component with type 'country' in address_components
        country_component = next((component for component in location.raw['address_components'] if 'country' in component['types']),None)

        if country_component:
           
            # Extract the country name from the component
            country = country_component.get('long_name', '')
            return country
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def display_info(latitude, longitude, run_time, country):
    info_text = f"ISS Location\nLatitude: {latitude}\nLongitude: {longitude}\nTimestamp: {run_time}\nCountry: {country}"
    label.config(text=info_text, font=("Arial", 12))

def get_static_map(latitude, longitude):

    # Construct the URL for the static map
    static_map_url = f'https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom=12&size=400x300&key={GOOGLE_API_KEY}'
    
    # Make a GET request to the static map API
    response = requests.get(static_map_url)

    if response.status_code == 200:
        # Open the image using PIL
        image = Image.open(BytesIO(response.content))
        return ImageTk.PhotoImage(image)  

def update_map(latitude, longitude):
    # Get the static map image
    map_image = get_static_map(latitude, longitude)

    # Update the Tkinter canvas with the new map image
    canvas.itemconfig(map_canvas, image=map_image)
    canvas.map_image = map_image  # Keep a reference to prevent garbage collection

# Create the main window
root = tk.Tk(baseName="ISS Tracker")
root.title("ISS Tracker")

# Create a label to display information
label = tk.Label(root, text='', font=('Arial', 12))
label.pack(pady=20)

# Create a Tkinter canvas for displaying the map
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Initial setup for the Tkinter canvas
initial_map_image = get_static_map(0, 0)
map_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=initial_map_image)

# Call the get_iss_location function initially
get_iss_location()

# Run the application
root.mainloop()