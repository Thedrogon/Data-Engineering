#A simple data pipeline based on the country_full data set
import pandas as pd

def extract(file_path : str) -> str:
    raw_data = pd.read_csv(file_path)
    return raw_data

#transforming to clean the data
def transform(raw_data):
    empty_data = raw_data.loc[raw_data["intermediate-region"].isnull() , : ] #getting nan related rows
    empty_data["intermediate-region"] = "Empty"
    empty_data["intermediate-region-code"] = "Empty"
    return empty_data

#load the cleaned data in a csv file
def load(cleaned_data):
    cleaned_data.to_csv("./Data sets/cleaned_country.csv", header = True , sep = ';')

raw_data = extract("./Data sets/country_full.csv")

cleaned_data = transform(raw_data)
load(cleaned_data)