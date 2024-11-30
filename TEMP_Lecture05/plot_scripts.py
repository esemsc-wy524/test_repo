import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 1000)

# Calculate y values for sine, cosine, and tangent
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot sine, cosine, and tangent functions
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='green')
plt.plot(x, y_tan, label='tan(x)', color='red')

# Set y limits to avoid large values for tan(x)
plt.ylim(-5, 5)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x), cos(x), and tan(x)')
plt.legend()

# Add grid
plt.grid(True)

# Save plot as PNG file
plt.savefig("trig_functions.png")
plt.savefig("trig_functions.pdf")

# Show plot on the screen
plt.show()