from __future__ import division
import math

from skyfield.api import load

def flip_and_burn(acceleration, distance):
    """
    given a constant acceleration and a distance,
    how long would it take to accelerate halfway,
    then decelerate the remainer of the distance.
    assumes intial 0 velocity, not other forces,
    and an instantanious 'flip-and-burn'
    p(x) = a*t^2 + v*t + h
    """
    t_halfway = math.sqrt((distance/2) * (1/acceleration))
    return t_halfway * 2


def acceleration_g_to_km_sec_sqr(g):
    return g*0.0016


def compute_flight_time(planets, start_name, destination_name, g):
    start = planets[start_name + ' barycenter']
    destination = planets[destination_name + ' barycenter']
    ts = load.timescale()
    t = ts.now()
    astrometric = start.at(t).observe(destination)
    distance = astrometric.distance().km
    acceleration = acceleration_g_to_km_sec_sqr(g)
    time_of_flight = flip_and_burn(acceleration, distance)
    return time_of_flight


def velocity(time, acceleration, initial_velocity):
    return acceleration*time + initial_velocity


def percent_of_c(velocity, units='km/sec'):
    c = {'km/sec': 299792 }
    return velocity/c[units]
