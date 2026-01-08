import pandas as pd


def calculate_efficiency(df):
df['passengers_per_km'] = df['passenger_count'] / df['route_distance_km']
df['fuel_efficiency'] = df['route_distance_km'] / df['fuel_consumed_liters']
df['time_efficiency'] = df['route_distance_km'] / df['travel_time_min']


return df
