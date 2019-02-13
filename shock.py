import RPi.GPIO as GPIO
import time

sensor = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

print "Shock sensor set up."

while True:
   if GPIO.input(sensor):
      time.sleep(0.1)
   else:
      print "Shock Sensed!"
      time.sleep(2)

