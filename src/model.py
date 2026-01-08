from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans




def train_efficiency_model(df):
features = df[['passengers_per_km', 'fuel_efficiency', 'time_efficiency']]


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


kmeans = KMeans(n_clusters=3, random_state=42)
df['efficiency_cluster'] = kmeans.fit_predict(scaled_features)


return df
