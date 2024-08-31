import pandas as pd

def clean_data(data):
    # 删除含有缺失值的行
    data.dropna(inplace=True)

    # 转换日期时间格式
    data['started_at'] = pd.to_datetime(data['started_at'])
    data['ended_at'] = pd.to_datetime(data['ended_at'])

    # 计算骑行时间并添加为新列（单位：分钟）
    data['ride_duration'] = (data['ended_at'] - data['started_at']).dt.total_seconds() / 60

    # 删除骑行时间小于1分钟或超过24小时的行
    data = data[(data['ride_duration'] >= 1) & (data['ride_duration'] <= 1440)]
    
    return data

if __name__ == "__main__":
    file_path = 'data/2021-citibike-tripdata/202101-citibike-tripdata/202101-citibike-tripdata_2.csv'
    from load_data import load_csv_data
    data = load_csv_data(file_path)
    clean_data = clean_data(data)
    save_path = 'data/cleaned/202101-citibike-tripdata_2_cleaned.csv'
    clean_data.to_csv(save_path, index=False)
    print(clean_data.head())