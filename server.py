from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from finance import get_earnings


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        return render_template("error.html")

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

@app.route('/finance')
def finance_graph():
    x = get_earnings()
    stockname = x["meta"]["symbol"]
    earningsdaterevenue = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["raw"]
    earningsdate = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]

    return render_template(
        "finance.html",
        stockName1 = stockname,
        earningsdate1 = earningsdate,
        earningsestimate1 = earningsdaterevenue
    )

# @app.route('/rickroll')
# def rickroll():
#     return render_template('www.youtube.com')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)



