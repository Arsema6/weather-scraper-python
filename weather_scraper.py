from datetime import datetime, timedelta
from  meteostat import Point, Daily
import matplotlib.pyplot as plt


#location: Addis Ababa
addis_ababa = Point(9.03, 38.74)

# period: last 7 days
# Today's date
end = datetime.today()
# 7 days ago
start = end - timedelta(days=7)

# Fetch daily data
data = Daily(addis_ababa, start, end)
data = data.fetch()

if data.empty:
    print("No weather data found for the given period.")
else:
    data.to_csv("addis_ababa_weather.csv")
    print(f"Data fetched from {start.date()} to {end.date()} saved successfully!")

# Display the data
print(data)
#visualize the data
data['tavg'].plot(title='Average Temperature in Addis Ababa', ylabel='Temperature (°C)')
plt.xlabel('Date')
plt.tight_layout()
plt.savefig("addis_ababa_weather_chart.png") 
plt.show()