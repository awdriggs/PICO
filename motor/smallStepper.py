import board
import digitalio
import time

# Define stepper motor control pins
AIN1 = digitalio.DigitalInOut(board.GP16)
AIN2 = digitalio.DigitalInOut(board.GP17)
BIN1 = digitalio.DigitalInOut(board.GP18)
BIN2 = digitalio.DigitalInOut(board.GP19)

# Set all pins to output mode
for pin in [AIN1, AIN2, BIN1, BIN2]:
    pin.direction = digitalio.Direction.OUTPUT

# Stepper motor sequence (Full-step mode)
step_sequence = [
    (1, 0, 1, 0),  # Step 1
    (0, 1, 1, 0),  # Step 2
    (0, 1, 0, 1),  # Step 3
    (1, 0, 0, 1)   # Step 4
]

def step_motor(steps, delay=0.01, reverse=False):
    """Rotate the stepper motor forward or backward."""
    sequence = step_sequence[::-1] if reverse else step_sequence  # Reverse if needed

    for _ in range(steps):
        for step in sequence:
            AIN1.value, AIN2.value, BIN1.value, BIN2.value = step
            time.sleep(delay)


# Run stepper motor forward and backward
while True:
    step_motor(100, delay=0.01, reverse=False)  # Move forward
    time.sleep(1)
    step_motor(100, delay=0.01, reverse=True)  # Move backward
    time.sleep(1)
