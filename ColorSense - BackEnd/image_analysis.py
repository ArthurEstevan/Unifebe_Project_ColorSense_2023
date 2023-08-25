from PIL import Image
import cv2
import requests
import pyttsx3

image_path = "../ColorSense/assets/BackgroundBlue.jpg"

image = Image.open(image_path)

image_width, image_height = image.size
center_point = (image_width // 2, image_height // 2)

import numpy as np

image_cv = cv2.imread(image_path)
hsv_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2HSV)
h_values = hsv_image[:, :, 0].flatten()
histogram, _ = np.histogram(h_values, bins=np.arange(0, 180), density=True)
dominant_hue = np.argmax(histogram)
dominant_color_rgb = cv2.cvtColor(np.uint8([[[dominant_hue, 255, 255]]]), cv2.COLOR_HSV2RGB)[0][0]

# Convert RGB to BGR
dominant_color_bgr = (dominant_color_rgb[2], dominant_color_rgb[1], dominant_color_rgb[0])

# Define the endpoint for the "Name that Color" API
api_url = f"https://www.thecolorapi.com/id?rgb={dominant_color_rgb[0]},{dominant_color_rgb[1]},{dominant_color_rgb[2]}"

# Make an API request to get the color name
response = requests.get(api_url)
color_data = response.json()
color_name = color_data["name"]["value"]

# Initialize the speech synthesis engine
engine = pyttsx3.init()

# Define speech rate (optional)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

# Speak the color name
print(f"Predominant Color {color_name} (RGB): {dominant_color_rgb}")
engine.say(f"The predominant color is {color_name}")
engine.runAndWait()
