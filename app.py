# save this as app.py
from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route("/")
def map_link():
    response_longitude = requests.get("https://Blynk.cloud/external/api/get?token=qIpqgPqk7Zpw7L6juManzZs7SujZSngS&V1")
    response_latitude = requests.get("https://Blynk.cloud/external/api/get?token=qIpqgPqk7Zpw7L6juManzZs7SujZSngS&V2")
    
    if response_longitude.ok and response_latitude.ok:
        longitude = response_longitude.text  # تأكد من أن الناتج هو قيمة نصية صحيحة
        latitude = response_latitude.text    # تأكد من أن الناتج هو قيمة نصية صحيحة

        map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        return redirect(map_url)
    else:
        return "Error fetching data", 500
