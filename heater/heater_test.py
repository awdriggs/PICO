
"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""
import time
import board
import digitalio

heater = digitalio.DigitalInOut(board.GP9)  # sets led to be line 14
heater.direction = digitalio.Direction.OUTPUT  #

while True:  # infinite loop here
    heater.value = True  # on
    print("heating?");
    time.sleep(0.25)
    # led.value = False  # off
    # time.sleep(0.25)

