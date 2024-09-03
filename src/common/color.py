import matplotlib.cm as cm
import matplotlib.colors as colors

def get_color(total_count, max_count):
    """
    获取一个颜色值，用于表示站点的使用频率。
    """
    # Normalize the count
    norm = colors.Normalize(vmin=0, vmax=max_count)
    # Choose a colormap
    cmap = cm.get_cmap('YlOrRd')  # Yellow to Orange to Red
    # Get color from colormap
    rgb = cmap(norm(total_count))[:3]  # Get RGB
    return colors.rgb2hex(rgb)