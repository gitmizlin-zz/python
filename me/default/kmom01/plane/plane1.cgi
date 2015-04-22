#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""hight in feet"""

hight_meter = 1100 # Mata in höjd över havet (meter).
speed_kmh = 1000 # Mata in hastighet (km/h).
temperature_c = -50 # Mata in temperatur utanför flygplanet (Celsius).

hight_feet = hight_meter * 3.28084
speed_miles = speed_kmh * 0.62137
temperature_f = temperature_c * 9 / 5 + 32 

print("Height (in feet): ", hight_feet)
print("Speed (in mph): ", speed_miles)
print("Temperature (in farenheit): ", temperature_f)
