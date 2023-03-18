import numpy as np
import matplotlib.pyplot as plt

# Define the function to plot
def f(x):
    return np.sin(x)

# Define the range of x values to plot
x = np.linspace(-np.pi, np.pi, 100)

# Compute the y values for the function
y = f(x)

# Create the plot
plt.plot(x, y)

# Add axis labels and a title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = sin(x)')

# Display the plot
plt.show()
