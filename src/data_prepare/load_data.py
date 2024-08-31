import pandas as pd

def load_csv_data(file_path):
    """load csv"""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    data = load_csv_data('data/2019-citibike-tripdata/2019-citibike-tripdata/1_January/201901-citibike-tripdata_1.csv')
    print(data.head())
