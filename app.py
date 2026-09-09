from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route("/")
def home():
    year = 2026
    month = 9

    month_name = calendar.month_name[month]
    month_days = calendar.monthcalendar(year, month)

    return render_template(
        "index.html",
        year=year,
        month_name=month_name,
        month_days=month_days
    )


if __name__ == "__main__":
    app.run(debug=True)
