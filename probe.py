# The Probe class describes a probe's characteristics, heading, and position.

import random
import math

import numpy as np
import matplotlib.pyplot as plt


class Probe:

    GRAVITY = 9.81

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
        # Randomly generate the velocity components.
        self.velocity_x_initial = random.uniform(-10000.0, 10000.0)
        self.velocity_y_initial = random.uniform(-10000.0, 10000.0)
        self.velocity_z_initial = random.uniform(0.01, 100000.0)

        # Calculate magnitude of velocity vector.
        self.velocity_initial = math.hypot(self.velocity_x_initial,
                                          self.velocity_y_initial,
                                          self.velocity_z_initial)

        # Calculate the angle theta above the horizontal.
        self.launch_angle_theta = math.acos(self.velocity_z_initial / 
                                            self.velocity_initial)

        # Calculate the angle phi on the horizontal.
        self.launch_angle_phi = math.atan2(self.velocity_y_initial, 
                                           self.velocity_x_initial)

        # Calculate the total flight time.
        flight_time = (2 * self.velocity_z_initial) / self.GRAVITY
        print(f'Flight time: {round(flight_time, 2)} seconds')

        # Generate time steps
        dt = flight_time / 1000
        print(dt)
        time_steps = np.linspace(0, flight_time, 1000)

        # Calculate 3D trajectory with numpy arrays.
        x = (self.position_x + self.velocity_x_initial * time_steps)
        y = (self.position_y + self.velocity_y_initial * time_steps)
        # The final z position should be zero.
        z = abs(self.position_z + (self.velocity_z_initial * time_steps) - (
            0.5 * self.GRAVITY * (time_steps)**2))

        # Plot the 3D path.
        fig = plt.figure(figsize=(8, 8))
        # 111 means 1 row in the grid, 1 column in the grid, and the
        # index(1) of subplot being activated.
        ax = fig.add_subplot(111, projection='3d')

        # Plot the trajectory
        ax.plot(x, y, z, label='Trajectory', color='black', lw=1.5, alpha=0.5)
        ax.scatter(x[0], y[0], z[0], color = 'green', marker='o', s=30, 
                   label='Launch Point')
        ax.scatter(x[-1], y[-1], z[-1], color='crimson', marker='x', s=50, 
                   label='Landing Point')

        # Set labels and adjust styling of plots.
        labels = [f'({round(x[0], 2)}, {round(y[0], 2)}, {round(z[0], 2)})', 
                  f'({round(x[-1], 2)}, {round(y[-1], 2)}, {round(z[-1], 2)})']

        x_points = [x[0], x[-1]]
        y_points = [y[0], y[-1]]
        z_points = [z[0], z[-1]]

        for x_point, y_point, z_point, label in (
            zip(
                x_points, 
                y_points, 
                z_points, 
                labels
                )
        ):
            ax.text(
                x_point + abs(x[-1]/20),
                y_point - y[-1]/10, 
                z_point + z[-1]/10, 
                label, 
                fontsize=10, color='black')

        ax.set_xlabel('x Distance (m)', alpha=0.5)
        ax.set_ylabel('y Distance (m)', alpha=0.5)
        ax.set_zlabel('z Altitude (m)', alpha=0.5)
        ax.set_title('3D Projectile Motion')
        ax.tick_params(axis='both', colors=(0, 0, 0, 0.5))
        ax.legend()
        ax.grid(True)

        
        plt.show()


