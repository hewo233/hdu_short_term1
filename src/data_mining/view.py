import folium
from folium.plugins import MarkerCluster

def visualize_start_end_points(data):
    """
    Visualize start and end points of bike rides on a map using different colors.

    Args:
    data (DataFrame): DataFrame with 'start_lat', 'start_lng', 'end_lat', 'end_lng'.

    Returns:
    Folium Map: A map with start and end points plotted.
    """
    # 创建地图，中心位于纽约市
    map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

    # 为起点创建一个标记群组
    start_marker_cluster = MarkerCluster(name='Start Points').add_to(map)
    # 为终点创建一个标记群组
    end_marker_cluster = MarkerCluster(name='End Points').add_to(map)

    # 在地图上添加起点标记
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['start_lat'], row['start_lng']],
            icon=folium.Icon(color='green', icon='play'),
            popup='起始点' + str(idx)
        ).add_to(start_marker_cluster)

    print('start finish')

    # 在地图上添加终点标记
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['end_lat'], row['end_lng']],
            icon=folium.Icon(color='red', icon='stop'),
            popup='终点' + str(idx)
        ).add_to(end_marker_cluster)

    print('end finish')

    # 添加图层控制器
    folium.LayerControl().add_to(map)

    return map

def visualize_cluster_centers(start_centers, end_centers):
    """
    Visualize cluster centers for start and end points on a map using Folium.

    Args:
    start_centers (array): Array of start cluster centers from KMeans.
    end_centers (array): Array of end cluster centers from KMeans.

    Returns:
    Folium Map: A map with cluster centers plotted.
    """
    map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

    # 添加起点聚类中心
    for center in start_centers:
        folium.Marker(
            location=[center[0], center[1]],
            icon=folium.Icon(color='green', icon='info-sign'),
            popup='Start Center'
        ).add_to(map)

    # 添加终点聚类中心
    for center in end_centers:
        folium.Marker(
            location=[center[0], center[1]],
            icon=folium.Icon(color='red', icon='info-sign'),
            popup='End Center'
        ).add_to(map)

    return map


import matplotlib.pyplot as plt


def plot_duration_clusters(data, centers, name):
    """
    可视化骑行持续时间的聚类结果。
    """
    plt.figure(figsize=(10, 6))
    max_duration = 60 
    bins = range(0, int(max_duration + 1), 2)  

    for cluster in sorted(data['duration_cluster'].unique()):
        cluster_data = data.loc[data['duration_cluster'] == cluster, 'ride_duration']
        plt.hist(cluster_data, bins=bins, alpha=0.4)

    for center in sorted(centers):
        if center < max_duration: 
            plt.axvline(x=center, color='r', linestyle='dashed', linewidth=2, label=f'Center at {center[0]:.2f} min')
    
    plt.title(f'{name} 的骑行时间')
    plt.xlabel('时间 (min)')
    plt.ylabel('骑行次数')
    plt.legend()
    plt.xlim(0, max_duration)
    plt.grid(True)
    plt.savefig(f'result/photos/{name}_duration_clusters.png')
