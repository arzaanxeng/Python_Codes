"""
The Weather Station Trend Analyzer
You are a data analyst at a meteorological department. You have received raw sensor logs
containing temperature and humidity readings as messy prose. Extract the numeric values
using regular expressions and visualize the environmental trends.
Input data
weather_logs = [
    "Reading 1: Station_B - Temp: 22C, Humidity: 60%. Morning clear.",
    "Reading 2: Station_B - Temp: 25C, Humidity: 58%. Sun increasing.",
    "Reading 3: Station_B - Temp: 30C, Humidity: 52%. Peak afternoon.",
    "Reading 4: Station_B - Temp: 27C, Humidity: 55%. Evening cooling."]

Tasks:
Define parse_weather_logs(logs): use regular expressions to extract temperature (before "C")
and humidity (before "%") values. Return a dictionary structured as {"TEMP": [22, 25, ...],
"HUMIDITY": [60, 58, ...]}.
Define visualize_weather(data_dict): plot temperature with an orange line and markers, and
humidity with a green line and markers. Add the title "Station B: Weather Trend Analysis" and a legend.
Main program flow
1. Call parse_weather_logs() and store the result.
2. Pass the result to visualize_weather().
3. Print the confirmation message below. Show the plot.
"""

import re
import matplotlib.pyplot as plt

weather_logs = [
    "Reading 1: Station_B - Temp: 22C, Humidity: 60%. Morning clear.",
    "Reading 2: Station_B - Temp: 25C, Humidity: 58%. Sun increasing.",
    "Reading 3: Station_B - Temp: 30C, Humidity: 52%. Peak afternoon.",
    "Reading 4: Station_B - Temp: 27C, Humidity: 55%. Evening cooling."
]

def parse_weather_logs(logs):
    hum_pattern  = re.compile(r"Humidity:\s(\d{2,3})%")
    temp_pattern = re.compile(r"Temp:\s(\d{2,3})C")

    joined = " , ".join(logs)

    humidity    = [int(i) for i in hum_pattern.findall(joined)]
    temperature = [int(i) for i in temp_pattern.findall(joined)]

    print("--- WEATHER DATA PROCESSOR ---")
    print(f"Analysing {len(logs)} sensor readings...")
    print(f"Extracted Temperature Data: {temperature}")
    print(f"Extracted Humidity Data: {humidity}")

    return {"TEMP": humidity, "HUMIDITY": temperature}  # ✓ correct keys

def visualize_weather(data_dict):
    print("Generating weather trend visualization...")
    plt.figure(figsize=(10, 5))
    plt.title("Station B: Weather Trend Analysis")
    plt.plot(data_dict["TEMP"],     label="Temperature (C)", color="orange", marker="o" )
    plt.plot(data_dict["HUMIDITY"], label="Humidity (%)",    color="green",  marker="s")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

data = parse_weather_logs(weather_logs)
visualize_weather(data)
print("Analysis complete.")