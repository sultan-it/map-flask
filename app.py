from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route("/")
def map_lin():
    longitude = requests.get("https://Blynk.cloud/external/api/get?token=qIpqgPqk7Zpw7L6juManzZs7SujZSngS&V1").text
    print(longitude)
    latitude = requests.get("https://Blynk.cloud/external/api/get?token=qIpqgPqk7Zpw7L6juManzZs7SujZSngS&V2").text

    map_url = redirect(f"https://www.google.com/maps/search/?api=1&query={longitude},{latitude}")
    return map_url
