import board
import adafruit_rgbled
import time

# Pin the Red LED is connected to
RED_LED = board.GP2

# Pin the Green LED is connected to
GREEN_LED = board.GP3

# Pin the Blue LED is connected to
BLUE_LED = board.GP4

# Create a RGB LED object
led = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)

while True:
    led.color = (107, 235, 52) #greenish blue
    print("trying");
    time.sleep(1)



