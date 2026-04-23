"""
You are working for a biotech startup. You have received a raw text file containing
nurse observations for different patients. The data is messy and mixed with prose. You
must extract the Heart Rate (BPM) and Oxygen Saturation (SpO2%) metrics and plot
them to identify health trends. Define a function named parse_medical_logs(logs).
Use the following as the input data:
medical_logs = [
"Time 1: Patient_A - HR: 72bpm, SpO2: 98%. Patient is stable.",
"Time 2: Patient_A - HR: 75bpm, SpO2: 97%. Slightly elevated.",
"Time 3: Patient_A - HR: 82bpm, SpO2: 95%. Monitoring required.",
"Time 4: Patient_A - HR: 90bpm, SpO2: 92%. Alert triggered."
]
Use regular expressions to find bpm and SpO2 values. Return a dictionary structured
like this: {"HR": [72, 75...], "SPO2": [98, 97...]}. Next, define a function named
visualize_vitals(data_dict). Plot the HR list with a red line and a marker. Also, plot
the SpO2 list with a blue line and a marker. Add the title “Clinical Trial: Patient A
Vitals Trend”. Add a background grid for readability. Use plt.legend() to show which
color represents which metric.
Main Program Flow:
1. Call parse_medical_logs(medical_logs) and store the dictionary.
2. Pass that dictionary into visualize_vitals()
3. Print a confirmation message: “Analysis complete”. Show the plots.

"""

medical_logs = [
"Time 1: Patient_A - HR: 72bpm, SpO2: 98%. Patient is stable.",
"Time 2: Patient_A - HR: 75bpm, SpO2: 97%. Slightly elevated.",
"Time 3: Patient_A - HR: 82bpm, SpO2: 95%. Monitoring required.",
"Time 4: Patient_A - HR: 90bpm, SpO2: 92%. Alert triggered."
]
import re
import matplotlib.pyplot as plt
def parse_medical_logs(logs):
    data = dict()

    hr_pattern = re.compile(r"HR:\s+(\d+)bpm")
    spo2_pattern = re.compile(r"SpO2:\s+(\d+)%")
    logs_string = " , ".join(logs)

    hr_raw = hr_pattern.findall(logs_string)
    spo2_raw = spo2_pattern.findall(logs_string)

    data["HR"] = [int(x) for x in hr_raw]
    data["SPO2"] = [int(x) for x in spo2_raw]
    return data

def visualize_vitals(data):
    plt.figure(figsize=(10, 10))
    plt.plot(data["HR"], label="HR" , color = "red" , marker = "o")
    plt.plot(data["SPO2"], label="SpO2" , color = "blue" , marker = "d")

    plt.title("Clinical Trial: Patient-A Vitals Trend")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Clinical_Trial.png")
    plt.show()

data = parse_medical_logs(medical_logs)
visualize_vitals(data)

















