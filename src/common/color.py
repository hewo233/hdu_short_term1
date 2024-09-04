import matplotlib.colors as mcolors
import matplotlib.cm as cm

def get_color(count, max_count):
    """
    根据使用频率计算颜色。

    """

    cmap = mcolors.LinearSegmentedColormap.from_list("custom_lime_red", ["#00FF00", "#FF0000"], N=256)
    norm = mcolors.Normalize(vmin=0, vmax=max_count)

    rgb = cmap(norm(count))
    return mcolors.rgb2hex(rgb)