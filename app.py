# save this as app.py
from flask import Flask, render_template
import datetime

app = Flask(__name__)

_responses = {
    "Sunday":{"Main": "No","Sub":"But this is his day to himself"},
    "Saturday":{"Main":"No","Sub":"Possibly he usually works 6 hours this day"},
    "weekday":{"Main":"Yes","Sub":"Kyle is free all day :))))"},
}
def timing(time):
    if time.isoweekday() == 6:
        return "Saturday"
    if time.isoweekday() == 7:
        return "Sunday"
    if time.isoweekday() in range(1,6):
        return "weekday"
    return None

@app.route("/")
def home():
    now = datetime.datetime.now()
    response = timing(now)
    context = _responses[response]
    return render_template('home.html', context=context)


if __name__ == "__main__":
    app.run()