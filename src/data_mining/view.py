import folium

def visualize_clusters_on_map(data, start_centers, end_centers):
    """
    在地图上可视化聚类结果
    """
    # 创建一个地图对象，中心设定为纽约市中心
    map = folium.Map(location=[40.7128, -74.0060], zoom_start=12, tiles='CartoDB positron')

    # 在地图上标注起点聚类
    for idx, row in data.iterrows():
        folium.CircleMarker(
            location=[row['start_lat'], row['start_lng']],
            radius=5,
            color='green',
            fill=True,
            fill_color='green',
            fill_opacity=0.7,
            popup=f"Start Cluster: {row['start_geo_cluster']}"
        ).add_to(map)

    # 在地图上标注终点聚类
    for idx, row in data.iterrows():
        folium.CircleMarker(
            location=[row['end_lat'], row['end_lng']],
            radius=5,
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7,
            popup=f"End Cluster: {row['end_geo_cluster']}"
        ).add_to(map)

    # 标注起点聚类中心
    for center in start_centers:
        folium.Marker(
            location=[center[0], center[1]],
            icon=folium.Icon(color='green', icon='info-sign'),
            popup='Start Center'
        ).add_to(map)

    # 标注终点聚类中心
    for center in end_centers:
        folium.Marker(
            location=[center[0], center[1]],
            icon=folium.Icon(color='red', icon='info-sign'),
            popup='End Center'
        ).add_to(map)

    return map

