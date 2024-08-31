import sys
sys.path.append('src/data_prepare')
sys.path.append('src/statistics')

from load_data import load_csv_data
from clean_data import clean_data

from describe import describe_data

data_2020 = load_csv_data('data/final/2020.csv')
data_2021 = load_csv_data('data/final/2021.csv')

describe_data('2020', data_2020)

describe_data('2021', data_2021)
