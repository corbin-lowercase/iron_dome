# The Probe class describes a probe's characteristics, heading, and position.

import random

import numpy as np
import matplotlib.pyplot as pyplot


class Probe:

    # Initialize mass, dimesnions, and position with values of 0.
    def __init__(self):

        self.mass = 0
        self.planet = ''

        self.dimension_x = 0  # Positive x is east, negative x is west.
        self.dimension_y = 0  # Positive y is north, negative y is south.
        self.dimension_z = 0  # Positive z is up, negative z is down.

        self.position_x = 0  # Positive x is east, negative x is west.
        self.position_y = 0  # Positive y is north, negative y is south.
        self.position_z = 0  # Positive z is up, negative z is down.

    # The launch method launches the probe at a random trajectory.
    def launch(self):
        # Randomly generate the velocity components to 2 decimal places.
        self.velocity_x_initial = round(random.uniform(0.0, 10.0), 2)
        self.velocity_y_initial = round(random.uniform(0.0, 10.0), 2)
        self.velocity_z_initial = round(random.uniform(0.0, 10.0), 2)

        # Determine the launch angles theta (from horizontal) and phi (on horizontal).
        self.launch_angle_theta = np.tan(self.velocity_z_initial / 
                                         self.velocity_y_initial)
        self.launch_angle_phi = # The angle on the horizontal. 
        # # Store the 3D velocity vector as a tuple.
        # self.velocity_initial = (self.velocity_x_initial, 
        #                         self.velocity_y_initial,
        #                         self.velocity_z_initial)

        # Establish the acceleration vector.
        if self.planet == 'Earth':
            self.acceleration = (0, 0, -9.81)