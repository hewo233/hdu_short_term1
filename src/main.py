import sys
sys.path.append('src/data_prepare')
sys.path.append('src/statistics')
sys.path.append('src/data_mining')

from load_data import load_csv_data

from compare import compare_and_visualize_stats

from clust import cluster_ride_durations
from view import plot_duration_clusters
from station import visualize_top_stations
from describe import describe_data, plot_membership_type_rides

data_2020 = load_csv_data('data/final/2020.csv')
data_2021 = load_csv_data('data/final/2021.csv')

plot_membership_type_rides('2020', data_2020)
plot_membership_type_rides('2021', data_2021)