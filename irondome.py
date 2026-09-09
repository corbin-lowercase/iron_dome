"""Iron Dome Module.

The Iron Dome identifies projectile threats via radar over a defense
zone, measures their direction/velocity, calculates trajectory,
assesses risk, and launches an interceptor that detonates in close
proximity to eliminate the threat. Designed in 3D.
"""

__author__ = 'Corbin Eckles'

import math
import random

import numpy as np
import matplotlib.pyplot as plt


class Vector3:
    """This handles position/velocity math for trajectory.
    
    Methods are Python operator overloads: allow simple vector
    operations without having to add .x and .z fields.
    """

    def __init__(self, x, y, z):
        """Vector components can be position or velocity.
        
        Negative x is west, positive x is east.
        Negative y is down, positive y is up.
        Negative z is south and positive z is north.
        """
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        # Enables vector * scalar operation.
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__ (self, scalar):
        # Enables scalar * vector operation.
        return self.__mul__(scalar)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self):
        return f'Vector3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'

class Environment:
    """The Environment sets the value of gravity for the system."""

    def __init__(self, gravity=9.81):
        self.gravity = Vector3(0, -gravity, 0)

class Projectile:
    """The Projectile object possesses 3D motion behavior."""

    def __init__(self, position_object: Vector3, velocity_object: Vector3):
        self.position = position_object
        self.velocity = velocity_object

    def update(self, environment, dt):
        """IronDomeSystem calls update on each projecitle."""

        self.velocity = self.velocity + environment.gravity * dt        
        self.position = self.position + self.velocity * dt

class Threat(Projectile):
    """This is an extension of the Projectile object.
    
    The Threat object initially exists without a trajectory until the
    TrajectoryCalculator assigns trajectory.
    """

    def __init__(self, position_object: Vector3, velocity_object: Vector3):
        super().__init__(position_object, velocity_object)
    
class Interceptor(Projectile):
    """This is an extension of the Projectile object.

    The Launcher creates the Interceptor object and is handed its
    targets position each tick without storing it. The Interceptor
    checks its proximity to its target each tick.
    """

    def __init__(self, position_object: Vector3, velocity_object: Vector3):
        super().__init__(position_object, velocity_object)

    def check_proximity():
        return
    
class Radar:
    """This detects Projectile objects with spherical readings."""

    def __init__(self):
        pass
    
class ThreatDetector:
    """This converts raw data from Radar into Cartesian coordinates.
    It builds Threat objects.
    """
    
    def __init__(self):
        pass

class TrajectoryCalculator:
    """This computes and assigns trajectory to a Threat object."""
    
    def __init__(self):
        pass

class DefenseZone:
    """Defines the area the IronDomeSystem covers and holds risk-weight
    interface.
    """
    
    def __init__(self):
        pass

class DomeZone:
    """A hemisphere shape that supports priority sub-areas."""
    
    def __init__(self):
        pass

class PolygonZone:
    """A future implementation to allow IronDomeSystem to defend
    any shape.
    """
    
    def __init__(self):
        pass

class RiskEvaluator:
    """This takes Threat and DefenseZone data to produce risk score."""
    
    def __init__(self):
        pass

class Launcher:
    """Constructs and launches Interceptor instances."""
    
    def __init__(self):
        pass

class IronDomeSystem:
    """Holds the main loop.
    
    Tracks active Threats/Interceptors, pairs them, ranks risk,
    and decides launches.
    """
    
    def __init__(self):
        pass

class Projectile2:
    """This class is used to calculate the actual trajectory."""

    GRAVITY = 9.81  # m/s^2

    # Initialize mass, dimensions, and position with values of 0.
    def __init__(self, *, x0, y0, z0, vx0=0, vy0=0, vz0=0):
        # self.mass = 0
        # self.dimension_x = 0
        # self.dimension_y = 0
        # self.dimension_z = 0

        self.position_x_initial = x0
        self.position_y_initial = y0
        self.position_z_initial = z0
        self.velocity_x_initial = vx0
        self.velocity_y_initial = vy0
        self.velocity_z_initial = vz0


    # The launch method launches the projectile at a random trajectory.
    def launch_random(self):
        # Randomly generate the initial position - Removed because want
        # to set pass positions as parameters to methods.
        # self.position_x_initial = random.uniform(-1000, 1000)
        # self.position_y_initial = random.uniform(0, 1000)
        # self.position_z_initial = random.uniform(-1000, 1000)

        # Set desired landing height.
        # self.position_y_final = 0  # Don't really need, could calc
        # x, z pos at any desired y if needed.

        # # Randomly generate the velocity components.
        # self.velocity_x_initial = random.uniform(-1000, 1000)
        # self.velocity_y_initial = random.uniform(100, 1000)
        # self.velocity_z_initial = random.uniform(-1000, 1000)
        
        # Calculate magnitude of velocity vector.
        self.velocity_initial = math.hypot(self.velocity_x_initial,
                                          self.velocity_y_initial,
                                          self.velocity_z_initial) 

        # Calculate the angle theta above the horizontal.
        self.launch_angle_theta = math.acos(self.velocity_y_initial 
                                            / self.velocity_initial)

        # Calculate the angle phi on the horizontal.
        self.launch_angle_phi = math.atan2(self.velocity_z_initial, 
                                           self.velocity_x_initial)

        # Calculate the total flight time.
        y_vel = self.velocity_y_initial
        delta_y = self.position_y_initial  # - self.position_y_final
        y_dis = 2 * self.GRAVITY * (delta_y)
        discriminant = (y_vel**2) + y_dis
        # Prevent imaginary numbers.
        try:
            self.flight_time = (y_vel + math.sqrt(discriminant)) / self.GRAVITY
        except ValueError:
            print('Discriminant is negative.')
            return
        flight_time = self.flight_time
        print(f'Flight time: {round(flight_time, 2)} seconds')

        # Calculate the max x and y displacement of the projectile.
        self.max_x_displacement = (
            self.position_x_initial
            + self.velocity_x_initial * flight_time
        )
        self.max_z_displacement = (
            self.position_z_initial
            + self.velocity_z_initial * flight_time
        )

        # Calculate the max z displacement of the projectile.
        time_to_apex = y_vel / self.GRAVITY
        self.max_y_displacement = (
            self.position_y_initial
            + (y_vel * time_to_apex)
            - (0.5 * self.GRAVITY * (time_to_apex)**2)
        )

        # Calculate the apex of flight path.
        x_vel = self.velocity_x_initial
        z_vel = self.velocity_z_initial
        self.apex = (
            self.position_x_initial + x_vel * time_to_apex,
            self.max_y_displacement,
            self.position_z_initial + z_vel * time_to_apex
            )
        
        # Generate the time steps with dt=0.05 and append last step.
        time_steps = np.arange(0, flight_time, 0.05)
        time_steps = np.append(time_steps, flight_time)

        # Calculate 3D positional coordinates for x, y, z. 
        # NumPy arrays are calculated all at once for each variable.
        x_displacement = self.velocity_x_initial * time_steps
        self.x = (self.position_x_initial + x_displacement)

        y_displacement = self.velocity_y_initial * time_steps
        y_displacement_gravity = 0.5 * self.GRAVITY * (time_steps)**2
        self.y = abs(self.position_y_initial + y_displacement - y_displacement_gravity)

        z_displacement = self.velocity_z_initial * time_steps
        self.z = (self.position_z_initial + z_displacement)

        # Combine 1D positional arrays with dt array.
        self.projectile_coords = np.column_stack(
            (self.x, self.y, self.z, time_steps)
        )

    # The plot method takes values from launch method and plots
    # the projectile's trajectory in 3D space.
    def plot(self):

        # Plot the 3D path.
        fig = plt.figure(figsize=(7, 7))
        # 111 means 1 row in the grid, 1 column in the grid, and the
        # index(1) of subplot being activated.
        ax = fig.add_subplot(111, projection='3d')

        # Convert from m to km if displacement is sufficiently large.
        if any(d >= 1000 for d in (
            self.max_x_displacement,
            self.max_y_displacement,
            self.max_z_displacement
            )
        ):
            x = self.x / 1000
            y = self.y / 1000
            z = self.z / 1000
            apex = tuple(val / 1000 for val in self.apex)
        else:
            x = self.x
            y = self.y
            z = self.z
            apex = self.apex
        # Graph the trajectory and plot launch point and landing point.
        ax.plot(x, y, z, label='Trajectory', color='crimson', lw=1.5, alpha=0.5)
        ax.scatter(
            x[0], y[0], z[0], color = 'crimson', marker='^', s=30, 
            label='Launch Point'
        )
        ax.scatter(
            x[-1], y[-1], z[-1], color='crimson', marker='x', s=50, 
            label='Landing Point'
        )

        # Plot the apex of the trajectory.
        ax.scatter(
            *apex,
            color = 'crimson', 
            marker = 'o',
            s=30,
            label='Apex'
        )

        ax.view_init(elev=15, azim=150, vertical_axis='y')

        # Set labels and adjust styling of plots.
        x_intitial = f'{round(x[0], 3):,}'
        y_intitial = f'{round(y[0], 3):,}'
        z_intitial = f'{round(z[0], 3):,}'
        labels = [
            f"({x[0]:,.3f}, {y[0]:,.3f}, {z[0]:,.3f})",
            f"({x[-1]:,.3f}, {y[-1]:,.3f}, {z[-1]:,.3f})",
            f"({apex[0]:,.3f}, {apex[1]:,.3f}, {apex[2]:,.3f})",
        ]
        
        # Store launch point, landing point, and apex.
        x_points = [x[0], x[-1], apex[0]]
        y_points = [y[0], y[-1], apex[1]]
        z_points = [z[0], z[-1], apex[2]]

        # Loop through launch and landing point to label them on plot.
        for x_point, y_point, z_point, label in zip(
            x_points, y_points, z_points, labels
        ):
            # This sets label position and style. Commented out code
            # only works when point values are relatively similar.
            ax.text(
                x_point,# + abs(x[-1]/20),  # After operator is offset.
                y_point,# - y[-1]/10, 
                z_point,# + z[-1]/10, 
                label, 
                fontsize=10, color='black')
            
        # Set plot styles. Change units from m to km if displacement is
        # sufficiently large.
        if any(d >= 1000 for d in (
            self.max_x_displacement,
            self.max_y_displacement,
            self.max_z_displacement
            )
        ):
            ax.set_xlabel('x Distance (km)', alpha=0.5)
            ax.set_ylabel('y Altitude (km)', alpha=0.5)
            ax.set_zlabel('z Distance (km)', alpha=0.5)
        else:
            ax.set_xlabel('x Distance (m)', alpha=0.5)
            ax.set_ylabel('y Altitude (m)', alpha=0.5)
            ax.set_zlabel('z Distance (m)', alpha=0.5)

        ax.set_title('3D Projectile Motion')
        ax.tick_params(axis='both', colors=(0, 0, 0, 0.5))
        ax.legend()
        ax.grid(True)

        plt.show()
