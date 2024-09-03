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
            popup='Start Point'
        ).add_to(start_marker_cluster)

    # 在地图上添加终点标记
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['end_lat'], row['end_lng']],
            icon=folium.Icon(color='red', icon='stop'),
            popup='End Point'
        ).add_to(end_marker_cluster)

    # 添加图层控制器
    folium.LayerControl().add_to(map)

    return map

# 使用示例
# data = pd.read_csv("your_data.csv")
# map = visualize_start_end_points(data)
# map.save('NYC_Bike_Rides.html')  # 保存到HTML文件，可以用浏览器打开查看
