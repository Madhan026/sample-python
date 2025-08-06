import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('weather.csv')


print(df.head())


df.fillna(method='ffill', inplace=True)


df['Date'] = pd.to_datetime(df['Date'])


df['Month'] = df['Date'].dt.month


print("Average Temperature:", df['Temperature'].mean())
print("Average Rainfall:", df['Rainfall'].mean())


max_rain_day = df[df['Rainfall'] == df['Rainfall'].max()]
print("Day with max rainfall:\n", max_rain_day[['Date', 'Rainfall']])


monthly_avg_temp = df.groupby('Month')['Temperature'].mean()
monthly_total_rain = df.groupby('Month')['Rainfall'].sum()


plt.figure(figsize=(10, 5))
plt.plot(monthly_avg_temp, label='Avg Temperature (°C)', marker='o')
plt.plot(monthly_total_rain, label='Total Rainfall (mm)', marker='s')
plt.title('Monthly Temperature and Rainfall Trends')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 5))
monthly_total_rain.plot(kind='bar', color='skyblue')
plt.title('Total Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(axis='y')
plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(df[['Temperature', 'Humidity', 'Rainfall']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation between Temperature, Humidity, Rainfall")
plt.show()
