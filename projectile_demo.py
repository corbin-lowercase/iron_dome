# Demo for launching a probe on the planet Earth
import random

import irondome



def main():

    position = irondome.Vector3(0, 0, 0)
    velocity = irondome.Vector3(1, 11, 1)

    env = irondome.Environment()

    trajectory = []
    time = 0.0
    dt = 0.01

    projectile = irondome.Projectile(position, velocity)
    while True:
        projectile.update(env, dt)
        time += dt
        trajectory.append((time, projectile.position.y))
        print((time, projectile.position.y))
        if projectile.position.y <= 0 and time > dt:
            break
    


    # # Create an object from the Probe class
    # my_projectile2 = irondome.Projectile2(x0=0, y0=0, z0=0)

    # User inputs probe variables
    # my_probe.mass = input('Probe mass: ')
    # my_probe.dimension_x = input('Probe size (x): ')
    # my_probe.dimension_y = input('Probe size (y): ')
    # my_probe.dimension_z = input('Probe size (z): ')

    # # Launch probe
    # try:
    #     my_projectile2.launch_random()
    #     # print(f'[x pos   y pos   z pos   flight time]\n'
    #     #     f'{my_projectile2.projectile_coords}')
    #     my_projectile2.plot()
    # except Exception as exception:
    #     print(exception)


    # Display intial velocities
    # print(f'Vx: {my_probe.velocity_x_initial}')
    # print(f'Vy: {my_probe.velocity_y_initial}')
    # print(f'Vz: {my_probe.velocity_z_initial}')

if __name__ == '__main__':
    main()