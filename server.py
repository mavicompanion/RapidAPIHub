from flask import Flask, render_template, request, send_file, redirect, url_for
from weather import get_current_weather
from waitress import serve
from finance import get_earnings
from ytvideo import get_video
from werkzeug.utils import secure_filename
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')

@app.route('/acceptweather')
def accept_weather():
    return render_template("index.html")

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
    st1 = request.args.get('stock1')
    st2 = request.args.get('stock2')
    st3 = request.args.get('stock3')
    x = get_earnings(st1)
    y = get_earnings(st2)
    z = get_earnings(st3)

    stockname1 = x["meta"]["symbol"]
    earningsdaterevenue1 = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["raw"]
    earningsdate1 = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]

    stockname2 = y["meta"]["symbol"]
    earningsdaterevenue2 = y["body"]["earnings"]["earningsChart"]["earningsDate"][0]["raw"]
    earningsdate2 = y["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]

    stockname3 = z["meta"]["symbol"]
    earningsdaterevenue3 = z["body"]["earnings"]["earningsChart"]["earningsDate"][0]["raw"]
    earningsdate3 = z["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]

    return render_template(
        "finance.html",
        stockName1 = stockname1,
        earningsdate1 = earningsdate1,
        earningsestimate1 = earningsdaterevenue1,
        stockName2 = stockname2,
        earningsdate2 = earningsdate2,
        earningsestimate2 = earningsdaterevenue2,
        stockName3 = stockname3,
        earningsdate3 = earningsdate3,
        earningsestimate3 = earningsdaterevenue3
    )

@app.route('/acceptf')
def accept_stock():
    return render_template("acceptstock.html")

@app.route('/error')
def error_page():
    #Separate error page
    return render_template("error.html")

@app.route('/ytdown')
def yt_video_downloader():
    video_url = request.args.get('youtube-link')
    responses = get_video(video_url)
    video_path = responses["adaptiveFormats"][0]["url"]
    audio_path = responses["adaptiveFormats"][-1]["url"]
    return render_template(
        "ytplay.html",
        videoLink = video_path,
        audioLink = audio_path
    )

@app.route('/ytaccept')
def get_yt_page():
    return render_template("youTube.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        img = cv2.imread(filepath)

        if img is None:
            return 'Error: Could not open the uploaded image.'

        processed_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        processed_filename = 'processed_' + filename
        processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
        cv2.imwrite(processed_filepath, processed_image)

        return render_template('opencv.html', uploaded_image=filename, processed_image=processed_filename)

    return redirect(request.url)

@app.route('/trialupload')
def opencvpage():
    return render_template('opencv.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)



