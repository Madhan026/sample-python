import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Load and preprocess the dataset
df = pd.read_csv("weather.csv")  # Make sure this file exists in the same directory
df['Date'] = pd.to_datetime(df['Date'])

# Extract year, month for analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Handle missing values (mean imputation)
df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())
df['Rainfall'] = df['Rainfall'].fillna(df['Rainfall'].mean())
df['Humidity'] = df['Humidity'].fillna(df['Humidity'].mean())

# --------------------------
# PLOT 1: Temperature Trends Over Years
# --------------------------
avg_temp_by_year = df.groupby('Year')['Temperature'].mean().reset_index()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(avg_temp_by_year['Year'], avg_temp_by_year['Temperature'], marker='o', color='red', label="Temperature (°C)")
plt.title("Temperature Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# --------------------------
# PLOT 2: Yearly Rainfall Distribution
# --------------------------
rainfall_by_year = df.groupby('Year')['Rainfall'].sum().reset_index()

plt.subplot(2, 2, 2)
plt.bar(rainfall_by_year['Year'], rainfall_by_year['Rainfall'], color='blue', label='Rainfall (mm)')
plt.title("Yearly Rainfall Distribution")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.grid(True)

# --------------------------
# PLOT 3: Humidity vs Temperature Correlation
# --------------------------
plt.subplot(2, 2, 3)
plt.scatter(df['Temperature'], df['Humidity'], color='green', marker='x')
plt.title("Humidity vs Temperature Correlation")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid(True)

# --------------------------
# PLOT 4: Temperature Prediction using Linear Regression
# --------------------------
X = avg_temp_by_year[['Year']]
y = avg_temp_by_year['Temperature']

model = LinearRegression()
model.fit(X, y)

# Predict future years
future_years = pd.DataFrame({'Year': range(X['Year'].min(), X['Year'].max() + 5)})
future_temp = model.predict(future_years)

plt.subplot(2, 2, 4)
plt.scatter(X, y, color='purple', label='Actual Temperature')
plt.plot(future_years['Year'], future_temp, color='orange', linestyle='--', label='Predicted Trend')
plt.title("Temperature Prediction for Next Years")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

# Final layout and display
plt.tight_layout()
plt.savefig("weather_analysis_summary.png")  # Optional: Save the plot
plt.show()
