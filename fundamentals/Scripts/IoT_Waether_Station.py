"""
Problem Statement: IoT Weather Station Data Manager

You are building a system to manage data from various IoT Weather Stations across a city.
 Each station sends a report containing its location and temperature.

Your task is to:
Store the incoming data in a list of dictionaries.
Iterate through the data using loops.

Use conditionals to categorize each station based on its temperature:
Cold: Below 15°C
Moderate: 15°C to 30°C
Hot: Above 30°C
Calculate the average temperature of all reporting stations.
"""

# 1. Data Structure: List of Dictionaries
weather_reports = [
    {"station_id": "ST-001", "location": "Downtown", "temp": 32},
    {"station_id": "ST-002", "location": "North Hills", "temp": 12},
    {"station_id": "ST-003", "location": "East Lake", "temp": 24},
    {"station_id": "ST-004", "location": "West Park", "temp": 35},
    {"station_id": "ST-005", "location": "South Bay", "temp": 14}
]

total_temp = 0
station_count = len(weather_reports)

print("--- IoT Weather Station Report Analysis ---")

for report in weather_reports:
    loc = report["location"]
    temp = report["temp"]
    total_temp += temp

    if temp < 15:
        category = "Cold"
    elif 15 <= temp <= 30:
        category = "Moderate"
    else:
        category = "Hot"

    print(f"Station: {loc:<12} | Temp: {temp}°C | Status: {category}")

average_temp = total_temp / station_count

print("-" * 48)
print(f"Total Stations: {station_count}")
print(f"Average City Temperature: {average_temp:.2f}°C")