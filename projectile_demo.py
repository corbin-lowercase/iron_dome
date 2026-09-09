# Demo for launching a porjectile.
import random

import irondome


def main():

    # Iron Dome system trajectory calculations.
    position = irondome.Vector3(0, 0, 0)
    velocity = irondome.Vector3(3, 5, 1)

    env = irondome.Environment()

    trajectory = []
    time = 0.0
    dt = 0.01

    projectile = irondome.Projectile(position, velocity)
    while True:
        step = (time, projectile.position.x, projectile.position.y,
                projectile.position.z)
        trajectory.append(step)

        if projectile.position.y <= 0 and time > dt:
            break
        projectile.update(env, dt)
        time += dt
    print(f'(time, x, y, z) {trajectory}')



    # # Model the actual trajectory.
    # traj = irondome.Projectile2(x0=0, y0=0, z0=0, vx0=3, vy0=5, vz0=1)


    # # Launch probe
    # try:
    #     traj.launch_random()
    #     # print(f'[x pos   y pos   z pos   flight time]\n'
    #     #     f'{my_projectile2.projectile_coords}')
    #     traj.plot()
    # except Exception as exception:
    #     print(exception)

if __name__ == '__main__':
    main()