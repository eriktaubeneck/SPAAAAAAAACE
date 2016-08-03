from __future__ import print_function

from skyfield.api import load
from humanfriendly import format_timespan

from flightpath import (flip_and_burn, acceleration_g_to_km_sec_sqr,
                        compute_flight_time, velocity, percent_of_c)


if __name__ == '__main__':
    planets = load('de421.bsp')

    g = 1.4
    start_name = 'Earth'
    destination_name = 'Jupiter'
    time_of_flight = compute_flight_time(planets, start_name, destination_name, g)

    print(
        '{} is currently {} from {} using a flip and burn '
        'flight path at a constant {}g burn'.format(
            destination_name, start_name, format_timespan(time_of_flight), g)
    )
    max_speed = velocity(time_of_flight/2, acceleration_g_to_km_sec_sqr(g), 0)
    p_of_c = percent_of_c(max_speed)
    print(
        'Max speed on the trip from {} to {} using a flip and burn '
        'flight path at a constant {}g burn is {}, {}% c.'.format(
            start_name, destination_name, g, max_speed, p_of_c*100)
    )
