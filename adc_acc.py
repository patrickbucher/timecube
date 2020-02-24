#!/usr/bin/env python3

import time

from Adafruit_ADS1x15 import ADS1115

GAIN = 1
DATA_RATE = 128
RESOLUTION = float(32768)

LOW = 0.3
MED = 0.4
HIGH = 0.5

adc = ADS1115()

def upper_side(values):
    """
    default position (all values 0):
        top:    1
        south:  2
        east:   3
        west:   4
        north:  5
        bottom: 6
    """
    key = '{:d}{:d}{:d}'.format(values[0], values[1], values[2])
    position_values = {
        '112': 1,
        '101': 2,
        '211': 3,
        '011': 4,
        '121': 5,
        '110': 6,
    }
    if key in position_values:
        return position_values[key]
    return -1


def round_to(value, granularity):
    return round(value * 1/granularity) * granularity


def normalize(measurement):
    return int(round_to(float(measurement) / RESOLUTION - 0.3, 0.1) * 10)


while True:
    values = [0, 0, 0]
    for i in range(3):
        try:
            measurement = adc.read_adc(i, gain=GAIN, data_rate=DATA_RATE)
            values[i] = normalize(measurement)
        except OSError as err:
            print(err)
            continue
    position = upper_side(values)
    print(position)
    time.sleep(1.0)

