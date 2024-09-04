import sys
sys.path.append('src/data_prepare')
sys.path.append('src/statistics')
sys.path.append('src/data_mining')

from load_data import load_csv_data

from compare import compare_and_visualize_stats

from clust import cluster_ride_durations
from view import plot_duration_clusters
from station import visualize_top_stations