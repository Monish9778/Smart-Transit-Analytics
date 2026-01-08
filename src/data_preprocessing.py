import pandas as pd


def load_and_clean_data(input_path, output_path):
df = pd.read_csv(input_path)


df['date'] = pd.to_datetime(df['date'])


numeric_cols = ['passenger_count', 'route_distance_km', 'travel_time_min', 'fuel_consumed_liters']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')


df.dropna(inplace=True)


df.to_csv(output_path, index=False)
return df
