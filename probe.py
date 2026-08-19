# The Probe class describes a probe's characteristics, heading, and position.

import random
import math

import numpy as np
import matplotlib.pyplot as plt


class Probe:

    GRAVITY = -9.81

    # Initialize mass, dimensions, and position with values of 0.
    def __init__(self):

        self.mass = 0
        self.dimension_x = 0  # Positive x is east, negative x is west.
        self.dimension_y = 0  # Positive y is north, negative y is south.
        self.dimension_z = 0  # Positive z is up, negative z is down.

        self.position_x = 0  # Positive x is east, negative x is west.
        self.position_y = 0  # Positive y is north, negative y is south.
        self.position_z = 0  # Positive z is up, negative z is down.

    # The launch method launches the probe at a random trajectory.
    def launch(self):
        # Randomly generate the velocity components to 2 decimal places.
        self.velocity_x_initial = round(random.uniform(-10.0, 10.0), 2)
        self.velocity_y_initial = round(random.uniform(-10.0, 10.0), 2)
        self.velocity_z_initial = round(random.uniform(0.01, 10.0), 2)

        # Calculate magnitude of velocity vector.
        self.velocity_initial = round(math.hypot(self.velocity_x_initial,
                                          self.velocity_y_initial,
                                          self.velocity_z_initial), 2)

        # Calculate the angle theta above the horizontal.
        self.launch_angle_theta = math.acos(self.velocity_z_initial / 
                                            self.velocity_initial)

        # Calculate the angle phi on the horizontal.
        self.launch_angle_phi = math.atan2(self.velocity_y_initial, 
                                           self.velocity_x_initial)

        # Calculate the total flight time.
        flight_time = round(-(2 * self.velocity_z_initial) / self.GRAVITY, 2)
        print(f'Flight time: {flight_time} seconds')

        # Generate 100 time steps.
        time_steps = np.linspace(0, flight_time, 100)

        # Calculate 3D trajectory with numpy arrays.
        x = (self.position_x + self.velocity_x_initial * time_steps)
        print(x)
        y = (self.position_y + self.velocity_y_initial * time_steps)
        print(y)
        # The final z position should be zero.
        z = (0.5 * self.GRAVITY * (time_steps)**2 -
             self.position_z + self.velocity_z_initial * (time_steps))
        print(z)

        # Plot the 3D path.
        fig = plt.figure(figsize=(8, 8))
        # 111 means 1 row in the grid, 1 column in the grid, and the
        # index(1) of subplot being activated.
        ax = fig.add_subplot(111, projection='3d')

        # Plot the trajectory
        ax.plot(x, y, z, label='Projectile Path', color='black', lw=2)
        ax.scatter(x[0], y[0], z[0], color = 'green', marker='o', s=30, 
                   label='Launch Point')
        ax.scatter(x[-1], y[-1], z[-1], color='crimson', marker='x', s=50, 
                   label='Landing Point')

        # Set labels and adjust styling of plots.
        labels = [f'({x[0]}, {y[0]}, {z[0]})', f'({x[-1]}, {y[-1]}, {z[-1]})']
        for i in range(2):
            plt.annotate(
                labels[i],

            )
        ax.set_xlabel('x Distance (m)')
        ax.set_ylabel('y Distance (m)')
        ax.set_zlabel('z Altitude (m)')
        ax.set_title('3D Projectile Motion')
        ax.legend()
        ax.grid(True)

        
        plt.show()


# # 1. Define coordinates for two points
# x = [2, 5]
# y = [4, 9]
# labels = ['Point A', 'Point B']

# # 2. Plot the points
# plt.scatter(x, y, color='red', s=100)

# # 3. Label each point using a loop
# for i in range(2):
#     plt.annotate(
#         labels[i],                      # Text label
#         (x[i], y[i]),                   # (x, y) coordinates of the point
#         textcoords="offset points",     # How to interpret xytext
#         xytext=(10, 10),                # Distance from point (x offset, y offset)
#         ha='center'                     # Horizontal alignment ('center', 'left', 'right')
#     )

# # Set window limits to view labels clearly
# plt.xlim(0, 8)
# plt.ylim(0, 12)