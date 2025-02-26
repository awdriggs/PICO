
# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries
# SPDX-License-Identifier: Unlicense

import time
import board
import busio  # Use busio for I2C communication
import adafruit_bh1750

# Define I2C using specific pins for the Raspberry Pi Pico
i2c = busio.I2C(scl=board.GP17, sda=board.GP16)  # Replace with the correct pins

# Initialize the sensor
sensor = adafruit_bh1750.BH1750(i2c)

print("hello")

while True:
    try:
        lux = sensor.lux
        print("%.2f Lux" % lux)
    except OSError:
        print("Sensor read error")
    time.sleep(1)
