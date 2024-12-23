import csv

# Save excel or csv into data structure... list or dictionary???
def read_csv_to_dict(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return data

series_data = read_csv_to_dict(r'.\static\data\Series_Data.csv')

# Create data structure
# List with 10 dictionaries
# Each dictionary has Series key, an Article key with a list of 10 article records
all_series = [{'Series': str(i), 'Articles': []} for i in range(1, 11)]


# Iterate through and process imported data
for i, article in enumerate(series_data):
    # Add rows to corresponding Series Articles
    all_series[int(article['Series_Number']) - 1]['Articles'].append(article)

print(all_series[0]['Articles'][0]['Series_Name'])
print(all_series[0]['Articles'][0]['Series_Desc'])
print(all_series[0]['Articles'][0]['Series_Summary'])
print(all_series[0]['Articles'][0]['Session_Number'])
