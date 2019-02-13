import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

led = 18
pir = 24

GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN)

print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"
while True:
   if GPIO.input(pir):
      GPIO.output(led,GPIO.HIGH)
      print "Motion Detected!"
      time.sleep(2)
   GPIO.output(led,GPIO.LOW)
   time.sleep(0.1)
