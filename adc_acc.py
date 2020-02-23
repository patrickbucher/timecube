#!/usr/bin/env python3

import time

from Adafruit_ADS1x15 import ADS1115

GAIN = 1
DATA_RATE = 128
VOLTAGE = 4.096
RESOLUTION = 32768.0

adc = ADS1115()

while True:
    values = [0, 0, 0]
    for i in range(3):
        measurement = adc.read_adc(i, gain=GAIN, data_rate=DATA_RATE)
        normalized = round(float(measurement) * VOLTAGE / RESOLUTION)
        values[i] = normalized
    print(values)
    time.sleep(1.0)
