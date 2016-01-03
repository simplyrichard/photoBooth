import subprocess
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(18):
			print("ON", end=" ")
			subprocess.call(" /var/www/capture.sh", shell=True)
		else:
			print("Port 25 is 0/low/false - LED OFF", end=" ")
			sleep(0.7)
finally:
	GPIO.cleanup()

