import numpy as np
import time
from datetime import datetime


class EdgeDataProcessor:
    """Simulates an Edge AI data pipeline for IoT sensors."""

    def __init__(self, sensor_name):
        self.sensor_name = sensor_name
        print(f"--- {self.sensor_name} Node Initialized ---")

    def read_simulated_data(self):
        # Simulating raw voltage/temp data typical in EE projects
        return np.random.normal(loc=25.0, scale=2.0)

    def process_data(self, raw_value):
        # Basic threshold logic often used in Edge AI
        status = "NORMAL" if raw_value < 28.0 else "ALERT"
        return round(raw_value, 2), status

    def run_stream(self, samples=5):
        for _ in range(samples):
            val = self.read_simulated_data()
            processed_val, status = self.process_data(val)

            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Sensor: {processed_val}°C | Status: {status}")
            time.sleep(1)


if __name__ == "__main__":
    # Example usage for your portfolio
    pipeline = EdgeDataProcessor(sensor_name="Thermal_Node_Alpha")
    pipeline.run_stream()