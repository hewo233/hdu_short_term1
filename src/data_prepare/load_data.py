import pandas as pd

def load_csv_data(file_path):
    dtype_dict = {
        'ride_id': str,
        'rideable_type': str,
        'started_at': str,
        'ended_at': str,
        'start_station_name': str,
        'end_station_name': str,
        'start_station_id': str,  # 假设为字符串，需要根据数据实际情况调整
        'end_station_id': str,    # 假设为字符串，需要根据数据实际情况调整
        'start_lat': float,
        'start_lng': float,
        'end_lat': float,
        'end_lng': float,
        'member_casual': str
    }
    return pd.read_csv(file_path, dtype=dtype_dict)

if __name__ == "__main__":
    data = load_csv_data('data/2020-citibike-tripdata/202001-citibike-tripdata/202001-citibike-tripdata_1.csv')
    print(data.head())
