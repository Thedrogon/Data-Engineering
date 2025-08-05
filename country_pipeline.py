#A simple data pipeline based on the country_full data set
import pandas as pd

def extract(file_path : str):
    raw_data = pd.read_csv("./Data sets/country_full.csv")