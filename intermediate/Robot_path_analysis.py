"""
Problem Statement: The Robot Heatmap System

Objective:

Build a Python class RobotTracker that manages a robot's coordinates,
parses movement strings, and visualizes visit frequency.

Key Requirements:
State: The robot must store its name, a path (list of coordinates), and its current_pos.

Parsing: A method must use Regex to turn strings like "R5U12" into a sequence of (x,y) coordinates.

Logic: Every individual step must be recorded (e.g., "R2" adds two points to the path)
to track time spent in a sector.

Visuals: A plot_heatmap() method must use matplotlib to show:
Size: Larger points for more frequent visits.

Color: Darker/brighter colors for "hotspots."

Persistence: The plot must be saved as {name}_path.png before being shown.

Constraint:
The system must support multiple independent robot instances simultaneously.

"""
import matplotlib.pyplot as plt
from collections import Counter
import re


class RobotTracker:
    def __init__(self, name):
        self.name = name
        self.path = []
        self.current_pos = [0, 0]

    def move(self, x, y):
        self.path.append((x, y))
        self.current_pos = [x, y]

    def process_string_path(self, compressed_path):

        pattern = r"([RULD])(\d+)"
        moves = re.findall(pattern, compressed_path)

        for direction, distance in moves:
            dist = int(distance)
            for _ in range(dist):
                if direction == 'R':
                    self.current_pos[0] += 1
                elif direction == 'L':
                    self.current_pos[0] -= 1
                elif direction == 'U':
                    self.current_pos[1] += 1
                elif direction == 'D':
                    self.current_pos[1] -= 1

                self.path.append(tuple(self.current_pos))

    def plot_heatmap(self):
    #Visualizes the robot's history
        if not self.path:
            print(f"Robot {self.name} hasn't moved yet!")
            return

        counts = Counter(self.path)
        coords = list(counts.keys())
        freq = list(counts.values())

        x = [c[0] for c in coords]
        y = [c[1] for c in coords]

        plt.figure(figsize=(6, 5))
        plt.scatter(x, y, s=[f * 100 for f in freq], c=freq, cmap='plasma')
        plt.title(f"Movement Heatmap: {self.name}")
        plt.colorbar(label="Frequency")
        plt.savefig(f"{self.name}_path.png")
        plt.show()


my_bot = RobotTracker("Wall-E")
my_bot.process_string_path("R5U3L2D1R5U10")
my_bot.plot_heatmap()