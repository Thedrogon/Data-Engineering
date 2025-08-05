#A simple data pipeline based on the country_full data set
import pandas as pd

def extract(file_path : str) -> str:
    raw_data = pd.read_csv(file_path)
    return raw_data

#transforming to clean the data
def transform(raw_data):
    empty_data = raw_data.loc[raw_data["intermediate-region"].isnull() , : ]
    return empty_data

#load the cleaned data in a csv file
def load():
    pass

raw_data = extract("./Data sets/country_full.csv")

print(transform(raw_data))