# object-oriented-1
This program simulates an Iron Dome system.

There are three systems:
	1) The threat generator launches a projectile at a random trajectory.
	2) The tracking system calculates and predicts the trajectory of the threat.
	3) The interceptor calculates the trajectory required for a defense
		projectile to meet the threat at a specified time/coordinate.

Advanced implementations:
	- Include air restistance and wind variables.
	- Interceptor could have the ability to change trajectory depending on
		conditions.
	- Display a real-time animation using pygame or Turtle.
	- Implement multiple simulataneous targets or evasive maneuvering.
	- Implement a defense map that calculates where threat will land, if
		striking uninhabited area, ignore threat.
		- Allow user to select land area (country?) and place defense points.
		- Give budget allowance for number of defense points or optimize
			placement of points based on defense area.
	- Implement cost-benefit analysis between using projectile or laser to
		counter the threat. Laser is overall upgrade but expensive to implement.
	- Allow multiple projectile launch points, determine which one should
		eliminate the threat.

The Iron Dome system identifies projectile threats over a defense zone.
Using radar, the threat is identified, its direction and velocity is measured,
and its trajectory is calculated. If the threat poses a high enough risk, the system launches an interceptor projectile which explodes in close proximity to 
the threat to eliminate it.