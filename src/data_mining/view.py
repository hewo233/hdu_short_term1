
import folium
from folium.plugins import MarkerCluster

def visualize_clusters_on_map(data):
    map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)
    marker_cluster = MarkerCluster().add_to(map)

    # 只为聚类中心添加标记
    print('visualize_clusters_on_map')
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['lat'], row['lng']],
            popup=f'Cluster: {row["cluster"]}',
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    return map



