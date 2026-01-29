from flask import Flask, render_template, request
import os
import requests


# Initialize Flask app
app = Flask(__name__)

API_KEY = os.getenv("WEATHER")


def fetch_weather(city: str):
    
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )
    if response.status_code != 200:
        try:
            data = response.json()
            message = data.get("message", "City not found or API error")
        except ValueError:
            message = "City not found or API error"

        return {"error": message}

    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "decs": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["icon"],
    }


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()

        if city:
            weather = fetch_weather(city)
        else:
            weather = {"error": "please enter a city name"}

    return render_template("index.html", weather=weather)


if __name__ == "__main__":

    app.run("0.0.0.0", port=8080, debug=True)
