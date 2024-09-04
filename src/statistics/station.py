import pandas as pd

def calculate_station_usage(data):
    """
    计算站点的使用频率
    """
    # 准备起点和终点数据，统计次数，计算经纬度
    start_data = data[['start_station_name', 'start_lat', 'start_lng']]
    end_data = data[['end_station_name', 'end_lat', 'end_lng']]

    # 起点统计
    start_stats = start_data.groupby('start_station_name').agg({
        'start_lat': 'first',  # 取第一个遇到的纬度作为代表值
        'start_lng': 'first',  # 取第一个遇到的经度作为代表值
    }).rename(columns={'start_lat': 'Latitude', 'start_lng': 'Longitude'}).reset_index()

    start_stats['Start Count'] = start_data['start_station_name'].value_counts().reset_index(drop=True)

    # 终点统计
    end_stats = end_data.groupby('end_station_name').agg({
        'end_lat': 'first',
        'end_lng': 'first',
    }).rename(columns={'end_lat': 'Latitude', 'end_lng': 'Longitude'}).reset_index()

    end_stats['End Count'] = end_data['end_station_name'].value_counts().reset_index(drop=True)

    # 合并起点和终点统计
    total_stats = pd.concat([
        start_stats.rename(columns={'start_station_name': 'Station Name'}),
        end_stats.rename(columns={'end_station_name': 'Station Name'})
    ])

    total_stats = total_stats.groupby('Station Name').agg({
        'Start Count': 'sum',
        'End Count': 'sum',
        'Latitude': 'first',
        'Longitude': 'first'
    }).reset_index()

    total_stats['Total Count'] = total_stats['Start Count'] + total_stats['End Count']


    return total_stats[['Station Name', 'Total Count', 'Latitude', 'Longitude']].sort_values(by='Total Count', ascending=False)


import folium

import sys
sys.path.append('src/common')

from color import get_color

def visualize_top_stations(data, top_n=50):
    """
    在地图上可视化使用频率最高的站点
    """
    # 计算站点使用频率，包括地理位置
    station_usage = calculate_station_usage(data)

    print(station_usage.columns)

    # 选取使用频率最高的站点
    top_stations = station_usage.head(top_n)

    # 创建地图，以纽约市为中心
    map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

    # 在地图上添加标记
    for idx, row in top_stations.iterrows():
        color = get_color(row['Total Count'], top_stations['Total Count'].max())
        print(color)
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=9,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"{row['Station Name']} ({int(row['Total Count'])} uses)"
        ).add_to(map)


    return map
