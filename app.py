# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def map_link():

        return "Error fetching data"

if __name__ == '_main_':

    app.run()
