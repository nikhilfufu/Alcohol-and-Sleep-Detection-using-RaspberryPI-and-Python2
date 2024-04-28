import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
ALCOHOL_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(ALCOHOL_PIN, GPIO.IN)

# Set up the gpio pin for motor
ENA = 17
IN1 = 27
IN2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)


def forward():
    GPIO.output(ENA,GPIO.HIGH)
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
def stop():
    GPIO.output(ENA,GPIO.LOW)
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)

# Main loop
while True:
    # Read the digital signal from the alcohol sensor
    alcohol_value = GPIO.input(ALCOHOL_PIN)
    
    # Check the alcohol concentration level and take appropriate action
    if alcohol_value == 0:
        forward()
        print("No alcohol detected")
    else:
        stop()
        print("Alcohol detected!")
        
    # Wait for a short time before taking the next measurement
    time.sleep(0.1)
# for buzzer 
# Check the alcohol concentration level and take appropriate action
if alcohol_value == 0:
    forward()
    GPIO.output(BUZZER_PIN, GPIO.LOW) # Turn off the buzzer
    print("No alcohol detected")
else:
    stop()
    GPIO.output(BUZZER_PIN, GPIO.HIGH) # Turn on the buzzer
    print("Alcohol detected!")
