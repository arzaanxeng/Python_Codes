
import matplotlib.pyplot as plt
import numpy as np

# Define the logistic sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate 200 evenly spaced values from -10 to 10
x = np.linspace(-10, 10, 300)
y = sigmoid(x)

# Configure the plot grid and size
plt.figure(figsize=(8, 5))
plt.grid(True, which='both', linestyle='--', alpha=0.6)

# Plot the sigmoid curve
plt.plot(x, y, color='blue', linewidth=2.5, label='Sigmoid Curve')
plt.savefig("Curve_Sigmoid.png")
plt.show()
