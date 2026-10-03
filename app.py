from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "c513ce4a526165288be6fd2a392bfc77"

API_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."

        else:

            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            try:

                response = requests.get(
                    API_URL,
                    params=params,
                    timeout=10
                )

                if response.status_code == 200:

                    data = response.json()

                    weather = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data["wind"]["speed"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"]
                    }

                elif response.status_code == 404:

                    error = "City not found. Please enter a valid city."

                elif response.status_code == 401:

                    error = "Invalid API key."

                else:

                    error = "Unable to fetch weather data."

            except requests.exceptions.RequestException:

                error = "Network error. Please check your internet connection."

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)