import sys
sys.path.append('src/data_prepare')
sys.path.append('src/statistics')

from load_data import load_csv_data

from compare import compare_and_visualize_stats

data_2020 = load_csv_data('data/final/2020.csv')
data_2021 = load_csv_data('data/final/2021.csv')

compare_and_visualize_stats(data_2020, data_2021)
