from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def cluster_geo_locations(data, n_clusters=5):
    """
    基于经纬度对数据进行聚类
    """
    start_coords = data[['start_lat', 'start_lng']]
    scaler_start = StandardScaler()
    scaled_start_coords = scaler_start.fit_transform(start_coords)
    kmeans_start = KMeans(n_clusters=n_clusters, random_state=0)
    data['start_geo_cluster'] = kmeans_start.fit_predict(scaled_start_coords)

    end_coords = data[['end_lat', 'end_lng']]
    scaler_end = StandardScaler()
    scaled_end_coords = scaler_end.fit_transform(end_coords)
    kmeans_end = KMeans(n_clusters=n_clusters, random_state=0)
    data['end_geo_cluster'] = kmeans_end.fit_predict(scaled_end_coords)

    original_start_centers = scaler_start.inverse_transform(kmeans_start.cluster_centers_, scaler_start)
    original_end_centers = scaler_end.inverse_transform(kmeans_end.cluster_centers_, scaler_end)

    return data, original_start_centers, original_end_centers

def cluster_ride_durations(data, n_clusters=10):
    """
    Cluster ride durations using K-Means.

    Args:
    data (DataFrame): DataFrame containing 'duration_minutes'.
    n_clusters (int): The number of clusters to form.

    Returns:
    DataFrame, ndarray: The original DataFrame with an additional 'duration_cluster' column and cluster centers.
    """

    durations = data['ride_duration'].values.reshape(-1, 1)
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    data['duration_cluster'] = kmeans.fit_predict(durations)
    return data, kmeans.cluster_centers_