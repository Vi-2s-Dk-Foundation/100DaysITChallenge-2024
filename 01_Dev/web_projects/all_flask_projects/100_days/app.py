from flask import Flask, render_template
import csv #Standard builtin

# Get and Clean Data

# function to get file and return data as dictionary
def read_csv_to_dict(filepath):
    with open(filepath, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data
    
# Process the file (with 100 articles)
file_data = read_csv_to_dict(r"./static/data/Series_Data.csv")

# Data Structure in the form of a list with 10 series, each series has 10 articles.
all_series= [{"Series": str(i), "Articles":[] } for i in range(1,11)]

# Iterate through csv data and add corresponding articles to series
for i, article in enumerate(file_data):
    all_series[int(article["Series_Number"])-1]["Articles"].append(article)

#print(all_series)

# Create App Structure
app = Flask(__name__)

# functions which return templates
# routing to home
@app.route("/")
def index():
    return render_template("index.html", all_series = all_series)

# Pass argument to use for all 10 series
# Dynamic routing?? Security!!! converter!
@app.route("/series/<int:series_number>")
def series(series_number):
    series_info = all_series[series_number - 1]
    return render_template("series.html", series_info = series_info)

# Make code Modular
if __name__ == "__main__":
    app.run(debug=True)


# Add Authentication
# Continue enforacing Security
# Optimize... compress, minify etc...
# Data structures to Databases... Scalable!!!
# Flask to Django???