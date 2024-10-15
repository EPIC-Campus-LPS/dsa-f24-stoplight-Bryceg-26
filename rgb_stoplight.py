import RPi.GPIO as GPIO
import time
while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        print("RED LIGHT")
        GPIO.output(18,GPIO.HIGH)
        time.sleep(4)
        GPIO.output(18,GPIO.LOW)

        GPIO.setup(25,GPIO.OUT)
        print("GREEN LIGHT")
        GPIO.output(25,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(25,GPIO.LOW)

        print("YELLOW LIGHT")
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)

