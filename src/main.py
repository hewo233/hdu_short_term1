import sys
sys.path.append('src/data_prepare')
sys.path.append('src/statistics')
sys.path.append('src/data_mining')

from load_data import load_csv_data

from compare import compare_and_visualize_stats

from clust import cluster_geo_locations
from view import visualize_clusters_on_map

data_2020 = load_csv_data('data/final/2020.csv')
data_2021 = load_csv_data('data/final/2021.csv')

data_2020_clustered, start_centers_2020, end_centers_2020 = cluster_geo_locations(data_2020)

map_2020 = visualize_clusters_on_map(data_2020_clustered, start_centers_2020, end_centers_2020)
map_2020.save('result/html/map_2020.html')
