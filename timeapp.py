from flask import Flask, render_template
from datetime import datetime
# from the py Time Zone module we are importing the timezone function
from pytz import timezone

# initiating Flask application
app = Flask(__name__)


@app.route("/")
def time():
    now = datetime.now(timezone('America/New_York'))
    # "now." is a datetime object representing the current time and date
    # "strftime" is a method that formats the "datetime" object into a string
    # "%d-%m-%Y" is the format string where %Y, %m and %d represents the year time and date respectively
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")
    year = now.strftime("%Y")
    return render_template("index.html", date=date, time=time, year=year)
