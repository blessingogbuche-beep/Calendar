from flask import Flask, render_template

import calendar
from datetime import date, timedelta 

app = Flask(__name__)

@app.route("/")
def home():
    year = 2026
    month = 9

    current_date = date(year, month, 1)

    previous_month = current_date.replace(day=1) - timedelta(days=1)
    next_month = current_date.replace(day=28) + timedelta(days=4)


    month_name = calendar.month_name[month]
    month_days = calendar.monthcalendar(year, month)

    return render_template(
        "index.html",
        year=year,
        month=month,
        month_name=month_name,
        month_days=month_days,
        previous_month=previous_month,
        next_month=next_month
    )


@app.route("/calendar/<int:year>/<int:month>")
def show_calendar(year, month):

    current_date = date(year, month, 1)

    previous_month = current_date.replace(day=1) - timedelta(days=1)
    next_month = current_date.replace(day=28) + timedelta(days=4)

    month_name = calendar.month_name[month]
    month_days = calendar.monthcalendar(year, month)

    return render_template(
        "index.html",
        year=year,
        month=month,
        month_name=month_name,
        month_days=month_days,
        previous_month=previous_month,
        next_month=next_month
    )


if __name__ == "__main__":
    app.run(debug=True)
