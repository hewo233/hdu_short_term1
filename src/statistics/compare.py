from describe import describe_data

import matplotlib.pyplot as plt
import numpy as np

def compare_and_visualize_stats(data1, data2):
    stats1 = describe_data('2020', data1)
    stats2 = describe_data('2021', data2)

    # 设置数据
    labels = list(stats1.keys())
    data1_values = list(stats1.values())
    data2_values = list(stats2.values())

    # 创建一个图表和多个子图
    fig, axes = plt.subplots(nrows=len(labels), ncols=1, figsize=(5, 15))

    chinese_labels = ['总骑行次数', '平均骑行时间(分钟)', '骑行时间标准差(分钟)', '会员骑行次数', '非会员骑行次数']

    for ax, label, data1_val, data2_val in zip(axes, chinese_labels, data1_values, data2_values):

        x = np.arange(1)  # 只有一组数据
        width = 0.01  # 设置较小的条形宽度

        spacing = 0.05  # 设置柱子之间的间隔（可以根据需要调整）

        rects1 = ax.bar(x - (width + spacing) / 4, data1_val, width, label='2020', color='blue')
        rects2 = ax.bar(x + (width + spacing) / 4, data2_val, width, label='2021', color='green')

        ax.set_xticks(x)
        ax.set_xticklabels([label], rotation=0)  # 标签水平放置
        ax.legend()

        ax.bar_label(rects1, padding=3, label_type='edge')  # 将数值显示在条形的上方
        ax.bar_label(rects2, padding=3, label_type='edge')  # 将数值显示在条形的上方

    fig.tight_layout()
    #plt.show()
    plt.savefig('result/photos/compare.png')

