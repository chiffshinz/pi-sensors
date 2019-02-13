import RPi.GPIO as GPIO
import time

sens = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(sens,GPIO.IN)

print "Detecting sound..."
time.sleep(2)
print "Speak!"

while True:
   if GPIO.input(sens):
      time.sleep(0.01)
   else:
      print "Sound Detected!"
      time.sleep(2)
