import matplotlib.pyplot as plt
from IPython import display
import time

# Sample x values
x_values = [1, 2, 3, 4, 5]

plt.ion()

# Create an initial plot
fig, ax = plt.subplots()
line, = ax.plot(x_values, [0]*len(x_values), label='Dynamic Plot')  # Initialize with zeros

# Add labels and title
ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.set_title('Dynamic Plot of X and Y Values')

# Add a legend
ax.legend()

# Display the plot
display.display(fig)

# Dynamic plot update in a loop
for i in range(10):  # Adjust the number of iterations as needed
    # Simulate calculating y values in a loop
    y_values = [2 * x + i for x in x_values]

    # Update the y values in the plot
    line.set_ydata(y_values)

    # Pause to create a dynamic effect
    plt.pause(0.5)  # Adjust the pause duration as needed
    
    # Clear the previous plot and display the updated plot
    display.clear_output(wait=True)
    display.display(fig)

# Keep the plot open until closed by the user
plt.ioff()
