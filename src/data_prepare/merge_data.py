from clean_data import clean_data
from load_data import load_csv_data

import pandas as pd

data_2021_1 = load_csv_data('data/cleaned/202101-citibike-tripdata_1_cleaned.csv')
data_2021_2 = load_csv_data('data/cleaned/202101-citibike-tripdata_2_cleaned.csv')

data = pd.concat([data_2021_1, data_2021_2])

save_path = 'data/final/2021.csv'
data.to_csv(save_path, index=False)