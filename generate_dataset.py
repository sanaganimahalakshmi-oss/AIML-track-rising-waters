import numpy as np
import pandas as pd

np.random.seed(42)

rows = 10000

annual_rainfall = np.random.randint(500, 4000, rows)
seasonal_rainfall = np.random.randint(200, 3000, rows)
temperature = np.random.randint(15, 40, rows)
humidity = np.random.randint(40, 100, rows)
river_level = np.random.uniform(1, 10, rows)
soil_moisture = np.random.randint(20, 100, rows)
wind_speed = np.random.randint(5, 80, rows)
pressure = np.random.randint(950, 1030, rows)
visibility = np.random.randint(1, 10, rows)
cloud_cover = np.random.randint(20, 100, rows)

risk = (
    annual_rainfall > 2500
) & (
    seasonal_rainfall > 1500
) & (
    humidity > 75
)

flood = risk.astype(int)

df = pd.DataFrame({
    "AnnualRainfall": annual_rainfall,
    "SeasonalRainfall": seasonal_rainfall,
    "Temperature": temperature,
    "Humidity": humidity,
    "RiverLevel": river_level,
    "SoilMoisture": soil_moisture,
    "WindSpeed": wind_speed,
    "Pressure": pressure,
    "Visibility": visibility,
    "CloudCover": cloud_cover,
    "Flood": flood
})

df.to_csv("data/flood_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())