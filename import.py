#pip install datadotworld[pandas]
#dw configure
#token =    eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJwcm9kLXVzZXItY2xpZW50Om1lZ3JhIiwiaXNzIjoiYWdlbnQ6bWVncmE6OjNhYjlhY2MwLTQxMzktNGQ4MS1hOWZiLTMzMmU4YmU4NGZkZSIsImlhdCI6MTc0Mzk2NzUxMywicm9sZSI6WyJ1c2VyX2FwaV9hZG1pbiIsInVzZXJfYXBpX3JlYWQiLCJ1c2VyX2FwaV93cml0ZSJdLCJnZW5lcmFsLXB1cnBvc2UiOnRydWUsInN2Yy1hY2NvdW50IjpmYWxzZX0.MbD5163zt1E4s_tNib7LSeJmHGd9Y6JeU0VwH1Q7WFWB8oob0ozqX3BRU5ir76PsDsKRdt9cYiFvmfyezBHMhA

import datadotworld as dw
import pandas as pd
import folium

# Load dataset into pandas
dataset = dw.load_dataset('datamil/vietnam-war-thor-data')

# Check available dataframes
print(dataset.dataframes.keys())

df = dataset.dataframes['thor_data_vietnam']

print(df)
# Basic exploration
print(df.head())
print(df.info())
print(df.describe())

df['total_weight'] = df['numweaponsdelivered'] * df['weapontypeweight']
print(df.groupby('takeofflocation')['total_weight'].sum())


# Sample 500 points to map
sample = df[['tgtlatdd_ddd_wgs84', 'tgtlonddd_ddd_wgs84']].dropna().sample(500)

# Create a map
m = folium.Map(location=[15, 105], zoom_start=5)
for _, row in sample.iterrows():
    folium.CircleMarker(
        location=[row['tgtlatdd_ddd_wgs84'], row['tgtlonddd_ddd_wgs84']],
        radius=2,
        color='red',
        fill=True,
    ).add_to(m)

m.save('map.html')

