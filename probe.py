# The Probe class describes a probe's characteristics, heading, and position.

# Positive x is east, negative x is west.
# Positive y is north, negative y is south.
# Positive z is up, negative z is down.

import random
import math

import numpy as np
import matplotlib.pyplot as plt


class Probe:

    GRAVITY = 9.81

    # Initialize mass, dimensions, and position with values of 0.
    def __init__(self):
        self.mass = 0
        self.dimension_x = 0
        self.dimension_y = 0
        self.dimension_z = 0

        self.position_x = 0
        self.position_y = 0
        self.position_z = 0

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
        self.launch_angle_theta = math.acos(self.velocity_z_initial 
                                            / self.velocity_initial)

        # Calculate the angle phi on the horizontal.
        self.launch_angle_phi = math.atan2(self.velocity_y_initial, 
                                           self.velocity_x_initial)

        # Calculate the total flight time from launch to landing.
        flight_time = (2 * self.velocity_z_initial) / self.GRAVITY
        print(f'Flight time: {round(flight_time, 2)} seconds')

        # Generate the time steps with dt=0.05 and append last step.
        time_steps = np.arange(0, flight_time, 0.05)
        time_steps = np.append(time_steps, flight_time)

        # Calculate 3D trajectory for x, y, z. NumPy arrays are
        # calculated all at once for each variable.
        x_displacement = self.velocity_x_initial * time_steps
        x = (self.position_x + x_displacement)

        y_displacement = self.velocity_y_initial * time_steps
        y = (self.position_y + y_displacement)

        z_displacement = self.velocity_z_initial * time_steps
        z_displacement_gravity = 0.5 * self.GRAVITY * (time_steps)**2
        z = abs(self.position_z + z_displacement - z_displacement_gravity)

        return x, y, z, flight_time

    def plot(x, y, z, flight_time):

        # Plot the 3D path.
        fig = plt.figure(figsize=(8, 8))
        # 111 means 1 row in the grid, 1 column in the grid, and the
        # index(1) of subplot being activated.
        ax = fig.add_subplot(111, projection='3d')

        # Graph the trajectory and plot launch and landing point.
        ax.plot(x, y, z, label='Trajectory', color='black', lw=1.5, alpha=0.5)
        ax.scatter(
            x[0], y[0], z[0], color = 'green', marker='o', s=30, 
            label='Launch Point'
        )
        ax.scatter(
            x[-1], y[-1], z[-1], color='crimson', marker='x', s=50, 
            label='Landing Point'
        )

        # Set labels and adjust styling of plots.
        labels = [
            f'({round(x[0], 2)}, {round(y[0], 2)}, {round(z[0], 2)})',
            f'({round(x[-1], 2)}, {round(y[-1], 2)}, {round(z[-1], 2)})'
            ]
        # Store launch and landing point.
        x_points = [x[0], x[-1]]
        y_points = [y[0], y[-1]]
        z_points = [z[0], z[-1]]
        # Loop through launch and landing point to label them on plot.
        for x_point, y_point, z_point, label in zip(
            x_points, y_points, z_points, labels
        ):
            # This sets label position and style.
            ax.text(
                x_point + abs(x[-1]/20),
                y_point - y[-1]/10, 
                z_point + z[-1]/10, 
                label, 
                fontsize=10, color='black')
        # Set plot styles.
        ax.set_xlabel('x Distance (m)', alpha=0.5)
        ax.set_ylabel('y Distance (m)', alpha=0.5)
        ax.set_zlabel('z Altitude (m)', alpha=0.5)
        ax.set_title('3D Projectile Motion')
        ax.tick_params(axis='both', colors=(0, 0, 0, 0.5))
        ax.legend()
        ax.grid(True)

        plt.show()
