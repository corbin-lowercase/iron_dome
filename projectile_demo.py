# Demo for launching a probe on the planet Earth
import projectile

def main():
    # Create an object from the Probe class
    my_projectile = projectile.Projectile()

    # User inputs probe variables
    # my_probe.mass = input('Probe mass: ')
    # my_probe.dimension_x = input('Probe size (x): ')
    # my_probe.dimension_y = input('Probe size (y): ')
    # my_probe.dimension_z = input('Probe size (z): ')

    # Launch probe
    my_projectile.launch()
    my_projectile.plot()

    # Display intial velocities
    # print(f'Vx: {my_probe.velocity_x_initial}')
    # print(f'Vy: {my_probe.velocity_y_initial}')
    # print(f'Vz: {my_probe.velocity_z_initial}')

if __name__ == '__main__':
    main()