# irondome.py

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


IRON DOME OOP DESIGN
=====================

PROJECT DESCRIPTION
--------------------
Iron Dome identifies projectile threats via radar over a defense zone,
measures their direction/velocity, calculates trajectory, assesses risk,
and if risky enough, launches an interceptor that detonates in close
proximity to eliminate the threat. Designed in 3D.


PIPELINE
--------
ThreatSpawner
  -> spawns a projectile object on the boundary of Radar hemisphere
Radar
  -> raw spherical/polar sensor readings (range, azimuth, elevation, Doppler velocity)

ThreatDetector
  -> converts raw readings to Cartesian Vector3
  -> constructs Threat (no trajectory yet)

TrajectoryCalculator
  -> fills in Threat.trajectory

RiskEvaluator(Threat, DefenseZone)
  -> uses DefenseZone.risk_weight(landing_point) as one factor
  -> returns a risk score (not a bool)

IronDomeSystem
  -> ranks all active Threats by score
  -> decides which to launch interceptors at
  -> maintains Interceptor<->Threat pairing

Launcher
  -> constructs Interceptor, launches it

Each tick:
  -> IronDomeSystem feeds each Interceptor its paired Threat's current
     position (not stored, just passed in)
  -> Interceptor.check_proximity(threat_position)
  -> On success: Threat marked destroyed, Interceptor marked success


CLASS BREAKDOWN
----------------

Vector3
    Position/velocity/trajectory math (add, subtract, scale, magnitude)

Projectile (base class)
    Shared motion behavior

Threat (extends Projectile)
    Detected object; two-stage lifecycle (exists without trajectory,
    then gets one filled in)

Interceptor (extends Projectile)
    Launched object; stateless guidance (handed target position each
    tick, doesn't store it); checks proximity

Radar
    Pure sensor - raw polar/spherical readings only, knows nothing
    about "Threat" as a concept

ThreatDetector
    Converts raw readings -> Cartesian -> builds Threat objects

TrajectoryCalculator
    Computes and assigns trajectory to a Threat

DefenseZone (abstract)
    Defines risk_weight(point) interface

DomeZone / CircularZone (concrete)
    First implementation - sphere/hemisphere shape; supports priority
    sub-areas

PolygonZone (future / long-term goal)
    Arbitrary shape (e.g., a country border)

RiskEvaluator
    Takes Threat + DefenseZone -> produces risk score

Launcher
    Constructs and launches Interceptor instances

IronDomeSystem
    Owns main loop; tracks active Threats/Interceptors; pairs them;
    ranks risk; decides launches


KEY DESIGN DECISIONS MADE (AND WHY)
-------------------------------------

1. Radar knows nothing about Threat
   - Stays a pure sensor, only raw readings.

2. ThreatDetector is the translation layer
   - Raw data -> Cartesian -> Threat object.

3. Threat exists before it has a trajectory
   - Two-stage lifecycle, filled in later by TrajectoryCalculator.

4. Interceptor has no stored reference to its target
   - Kept "dumb," symmetric with how Threat/Radar were designed;
     guidance data is passed in per-tick instead of stored.

5. RiskEvaluator returns a score, not a bool
   - Supports ranking/prioritizing multiple simultaneous threats.

6. DefenseZone is an abstract interface (risk_weight(point))
   - So shape can change (circle -> country polygon) later without
     rewriting RiskEvaluator.

7. Inheritance retained for Projectile -> Threat/Interceptor
   - Despite behavioral divergence, motion fundamentals are shared.

8. Multiple threats supported
   - IronDomeSystem manages collections, not single instances, and
     handles Interceptor<->Threat pairing itself.