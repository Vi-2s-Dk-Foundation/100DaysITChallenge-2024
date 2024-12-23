from flask import Flask, render_template
import csv

app = Flask(__name__)

# Save excel or csv into data structure... list or dictionary???
def read_csv_to_dict(filepath):
    with open(filepath, "r", encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

# Process Data
all_series_data = read_csv_to_dict(r'.\static\data\Series_Data.csv')

#Dictionary of series
# Create data structure
# List with 10 dictionaries
# Each dictionary has Series key & corresponding Series #, an Article key with a list of 10 article records
all_series = [{'Series': str(i), 'Articles': []} for i in range(1, 11)]


# Iterate through and process imported data
for i, article in enumerate(all_series_data):
    # Add rows to corresponding Series Articles
    all_series[int(article['Series_Number']) - 1]['Articles'].append(article)

@app.route("/")
def index():
    return render_template("index.html", all_series=all_series)

@app.route("/series/<int:series_number>")
def series(series_number):
    series_info = all_series[series_number-1]
    #print(series_info)
    return render_template("series.html", series_info=series_info)

if __name__ == "__main__":
    app.run(debug=True)
