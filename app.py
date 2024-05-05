from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route("/")
def map_lin():
    longitude = requests.get("https://shorturl.at/jwAQ5").text
    print(longitude)
    latitude = requests.get("https://shorturl.at/etJM8").text

    map_url = redirect(f"https://www.google.com/maps/search/?api=1&query={longitude},{latitude}")
    return map_url
