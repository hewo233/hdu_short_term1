import pandas as pd

def describe_data(name, data):
    # 计算描述性统计量
    total_rides = len(data)
    average_duration = data['ride_duration'].mean()
    std_duration = data['ride_duration'].std()
    member_rides = data[data['member_casual'] == 'member'].shape[0]
    casual_rides = data[data['member_casual'] == 'casual'].shape[0]

    # print(f'{name} 数据可视化')

    # # 会员与非会员骑行次数对比
    # plot_membership_type_rides(name, data)

    # # 骑行时间分布
    # plot_duration(name, data)

    # 返回结果
    return {
        'Total Rides': total_rides,
        'Average Duration (min)': average_duration,
        'Duration Std Dev (min)': std_duration,
        'Member Rides': member_rides,
        'Casual Rides': casual_rides
    }

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


font_list = ['Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'SimSun', 'Microsoft YaHei']
available_fonts = set(f.name for f in fm.fontManager.ttflist)
font_name = next((font for font in font_list if font in available_fonts), None)

if font_name:
    print(f"Using font: {font_name}")
    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False 
else:
    print("No suitable Chinese font found. Please install one of the fonts.")


def plot_membership_type_rides(name, data):       # 会员与非会员骑行次数对比
    member_counts = data['member_casual'].value_counts()

    plt.figure(figsize=(8, 5))
    member_counts.plot(kind='bar', color=['blue', 'green'])
    plt.title('会员与非会员骑行次数对比')
    plt.xlabel('会员类型')
    plt.ylabel('骑行次数')
    plt.xticks(rotation=0)
    #plt.show()

    plt.savefig(f'result/photos/{name}_membership.png')

def plot_duration(name, data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['ride_duration'], bins=5000, color='skyblue', rwidth=0.6)
    plt.title('骑行时间分布')
    plt.xlabel('时间(min) - 对数尺度')
    plt.ylabel('骑行次数')
    plt.xscale('log')
    
    # 自定义 x 轴的刻度
    ticks = [1, 2, 5, 10, 20, 50, 100, 200]
    plt.xticks(ticks, labels=[str(tick) for tick in ticks])
    
    plt.grid(True)
    #plt.show()
    plt.savefig(f'result/photos/{name}_duration.png')