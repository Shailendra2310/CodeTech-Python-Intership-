import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.gridspec as gridspec
import numpy as np

# API Config
API_KEY = '6c1b13154c7dfd27fa8232280c74c4aa'
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch Data
response = requests.get(URL)
data = response.json()

if data.get("cod") != "200":
    print("Failed to fetch data:", data.get("message", "Unknown error"))
    exit()

# Extract values
dates, temps, humidity = [], [], []

for item in data['list']:
    dt = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
    dates.append(dt)
    temps.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])

# Dashboard Layout
sns.set(style="whitegrid")
plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(3, 2, height_ratios=[0.3, 1, 1])

# Header
ax_title = plt.subplot(gs[0, :])
ax_title.axis('off')
ax_title.text(0.5, 0.5, f"Weather Dashboard - {CITY}", fontsize=20, fontweight='bold', ha='center', va='center')

# Temperature Line Chart
ax1 = plt.subplot(gs[1, 0])
sns.lineplot(x=dates, y=temps, marker='o', color='dodgerblue', ax=ax1)
ax1.set_title('Temperature Over Time')
ax1.set_ylabel('Temp (°C)')
ax1.set_xlabel('')
ax1.tick_params(axis='x', rotation=45)

# Humidity Line Chart
ax2 = plt.subplot(gs[1, 1])
sns.lineplot(x=dates, y=humidity, marker='o', color='seagreen', ax=ax2)
ax2.set_title('Humidity Over Time')
ax2.set_ylabel('Humidity (%)')
ax2.set_xlabel('')
ax2.tick_params(axis='x', rotation=45)

# Summary Boxplots
ax3 = plt.subplot(gs[2, 0])
sns.boxplot(y=temps, color='lightblue', ax=ax3)
ax3.set_title('Temperature Distribution')
ax3.set_ylabel('Temp (°C)')

ax4 = plt.subplot(gs[2, 1])
sns.boxplot(y=humidity, color='lightgreen', ax=ax4)
ax4.set_title('Humidity Distribution')
ax4.set_ylabel('Humidity (%)')

plt.tight_layout()
plt.show()
