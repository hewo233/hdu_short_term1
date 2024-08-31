import pandas as pd

def clean_data(data):
    """进行数据清洗和预处理."""
    # 转换时间字段为 datetime 类型
    data['starttime'] = pd.to_datetime(data['starttime'])
    data['stoptime'] = pd.to_datetime(data['stoptime'])

    # 规范化文本字段
    data['start station name'] = data['start station name'].str.strip().str.title()
    data['end station name'] = data['end station name'].str.strip().str.title()

    # 处理出生年份异常值
    current_year = pd.to_datetime('today').year
    data = data[(data['birth year'] > 1940) & (data['birth year'] < current_year - 16)]  # 筛选合理的出生年份范围

    # 处理骑行时间异常值
    data = data[(data['tripduration'] > 60) & (data['tripduration'] < 24 * 60 * 60)]  # 限制骑行时间在1分钟到24小时之间

    # 填补缺失值，这里以众数填充示例
    data.dropna(subset=['start station id', 'end station id'], inplace=True)

    # 去除重复记录
    data.drop_duplicates(inplace=True)

    # 重置索引
    data.reset_index(drop=True, inplace=True)

    return data

if __name__ == "__main__":
    file_path = 'path/to/your/datafile.csv'
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    # 保存清洗后的数据
    cleaned_data.to_csv('path/to/your/cleaned_data.csv', index=False)
    print("Data cleaning completed and saved to 'path/to/your/cleaned_data.csv'")
