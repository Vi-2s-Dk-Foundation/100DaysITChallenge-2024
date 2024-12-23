from flask import Flask, render_template
import csv #Builtin standard python library

# Function to read csv into dictionary
def read_csv_to_dict(filepath):
    with open(filepath, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

# Get and Process Data
all_data = read_csv_to_dict(r"./static/data/Series_Data.csv")

# Data structure 10 series... Each series has 10 articles/sessions
# We will populate the articles
all_series = [{"Series": str(i), "Articles": []} for i in range(1,11)]

# Iterate through all data and populate all_series
for i, article in enumerate(all_data):
    all_series[int(article["Series_Number"])-1]["Articles"].append(article)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", all_series=all_series) # Pass all series data to use in index.html

@app.route("/series/<int:series_number>")
def series(series_number):
    # We only need data for 1 series
    series_info = all_series[series_number - 1]
    return render_template("series.html", series_info = series_info) # Pass single series info

if __name__ == "__main__":
    app.run(debug=True)